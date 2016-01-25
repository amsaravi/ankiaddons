# -*- coding: utf-8 -*-
# Author:  Nicolò Valigi
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
#
#   systray plugin
#
# Adds a simple tray icon menu to create a new card, raise anki, or quit.
# "Add new card" by default opens a new window. If an "add card" window is already
# active (receiving user input) it doesn't do anything. If an "add card"
# windows is already open with data, it raises it. If an empty "add card"
# windows is already open, it closes it and reopens a new one. This works
# around OSX's behaviour of switching Spaces when the same window is opened somewhere
# else.

from PyQt4.QtGui import *
from PyQt4 import QtCore
import aqt
import os, time
from anki.hooks import addHook

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

def showCardAdder():
    (creator, instance) = aqt.dialogs._dialogs["AddCards"]
    if instance:
        if instance.isActiveWindow():
            return
        if instance.editor.fieldsAreBlank():
            #closing an existing empty editor
            instance.close() #it's safe, I've already checked the fields
            aqt.dialogs.close("AddCards")
    #The second "open" I run raises the add card window even if the main one isn't
    aqt.mw.onAddCard()
    aqt.dialogs.open("AddCards", aqt.mw)

def click_trap(value):
    if value == QSystemTrayIcon.Trigger: #left click!
        aqt.mw.app.emit(QtCore.SIGNAL("appMsg"), "raise")
        aqt.mw.showNormal()
        aqt.mw.activateWindow()

def createSysTray():
    self = aqt.mw
    trayIcon = QSystemTrayIcon(self)
    
    ankiLogo = QIcon()
    ankiLogo.addPixmap(QPixmap(_fromUtf8(":/icons/anki.png")), QIcon.Normal, QIcon.Off)
    trayIcon.setIcon(ankiLogo)
    
    trayMenu = QMenu(self)
    trayIcon.setContextMenu(trayMenu)

    trayIcon.activated.connect(click_trap)
      
    addNewAction = QAction("Create new card", self)
    addNewAction.triggered.connect(showCardAdder)
    trayMenu.addAction(addNewAction)
    
    raiseWindowAction = QAction("Raise Anki Window", self)
    raiseWindowAction.triggered.connect(lambda: aqt.mw.app.emit(QtCore.SIGNAL("appMsg"), "raise"))
    trayMenu.addAction(raiseWindowAction)
    
    trayMenu.addSeparator()
    
    quitAction = QAction("Quit Anki", self)
    self.connect(quitAction, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("close()"))
    trayMenu.addAction(quitAction)
    
    trayIcon.setVisible(True)
    trayIcon.show()


addHook("profileLoaded", createSysTray)
#aqt.editor.Editor.setupFields = wrap (aqt.editor.Editor.setupButtons, addXournalButton, "after")
#def raiseWindow(self):
#    aqt.mw.app.emit(QtCore.SIGNAL("appMsg"), "raise")
#addNewAction.triggered.connect(lambda: aqt.dialogs.open("AddCards", self))
