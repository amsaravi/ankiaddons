from PyQt4 import QtGui  # Import the PyQt4 module we'll need
from PyQt4.QtGui import QDialog,QAction
import sys
from aqt import mw
from aqt.qt import *
from aqt.utils import tooltip

from GetFolderDlg import Ui_PickFolderDlg  # This file holds our MainWindow and all design related things


import os  # For listing directory methods
from os import listdir
from os.path import isfile, join
import shutil

class addonDialog(Ui_PickFolderDlg):
    def __init__(self):
        Ui_PickFolderDlg.__init__(self)
        
        self.setupUi(self)  # This is defined in GetFolderDlg.py file automatically
        self.txtDeckName.setText("Deafault")
        self.btnPickFolder.clicked.connect(self.browse_folder)
       
        # It sets up layout and widgets that are defined
        #self.btnPickFolder.clicked.connect(self.browse_folder)  # When the button is pressed
         # Execute browse_folder function
    def browse_folder(self):
        #self.lstFolderContent.clear() # In case there are any existing elements in the list
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")

        if directory: # if user didn't pick a directory don't continue
            files = [f for f in os.listdir(directory) if isImageFile(f, directory) ]
            for f in files:
                pass
                # for all files, if any, in the directory
                #self.lstFolderContent.addItem(f)  # add file to the lstFolderContent
            self.lblImagesCount.setText("Images count: {0}".format(len(files)))
            self.txtFolderName.setText(directory)
            
    
    def get_dec(self):
        pass
    
def import_images(directory,decName,tags):
    #create new deck and custom model
    deck = mw.col.decks.get(mw.col.decks.id(decName))
    model  = mw.col.models.byName("Basic")

    #assign custom model to new deck
    mw.col.decks.select(deck["id"])
    mw.col.decks.get(deck)["mid"] = model["id"]
    mw.col.decks.save(deck)

    #assign new deck to custom model
    mw.col.models.setCurrent(model)
    mw.col.models.current()["did"] = deck["id"]
    mw.col.models.save(model)        
    txt=u"""
    <div><img src="{0}" /></div>
    """
    files = {f:(join(directory, f),join(os.getcwd(), f)) for f in os.listdir(directory) if isImageFile(f, directory) }
    for f, path in files.items():
        shutil.move(*path)
        note = mw.col.newNote()
        note["Front"] = txt.format(f)
        note["Back"] = ""
        
        tagList = mw.col.tags.split(tags)
        for tag in tagList:
            note.addTag(tag)
        
        mw.app.processEvents()
        mw.col.addNote(note)
        
    mw.col.reset()
    mw.reset()
        
    tooltip("{0} images Imported...".format(len(files)))
    
def isImageFile(fileName,filePath):
    return os.path.isfile(join(filePath, fileName)) and fileName.endswith((".jpg",".jpeg",".gif",".png",".bmp"))
    
def importFromImages():
    global __window
    __window = addonDialog()
    if __window.exec_():
        if(__window.selectedFolder):
            import_images(*__window.getData())     
    

action = QAction("Images to Cards", mw)
mw.connect(action, SIGNAL("triggered()"), importFromImages)
mw.form.menuTools.addAction(action)