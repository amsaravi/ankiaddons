# -*- coding: utf-8 -*-
# Copyright 2013 Oleg Loewen <loewen.oleg@gmail.com>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

from anki.hooks import wrap
from aqt.editor import Editor
from anki.utils import json

def toggleList(self):
	html_list = "".join(["<ul><li>",
                               self.web.selectedText(),
                               "</li></ul>"])
	self.web.eval("document.execCommand('inserthtml', false, %s);"
                  % json.dumps(html_list))

def toggleBullet(self):
	html_blt = "".join(["<ol><li>",
                               self.web.selectedText(),
                               "</li></ol>"])
	self.web.eval("document.execCommand('inserthtml', false, %s);"
                  % json.dumps(html_blt))

def togglefarsi(self):
	html_div = "".join(["<div class='f'>",
                               self.web.selectedText(),
                               "</div>"])
	self.web.eval("document.execCommand('inserthtml', false, %s);"
                  % json.dumps(html_div))

def clearboth(self):
	self.note.fields[self.currentField] = "".join(["<div class='clear'>",
                              self.note.fields[self.currentField], "</div>"])
	self.loadNote()
	# focus field so it's saved
	self.web.setFocus()
	self.web.eval("focusField(%d);" % self.currentField)

def setupButtons(self):
    self._addButton("listButton", lambda s=self: toggleList(self),
                    text=u"o", tip="List (Ctrl+Shift+U)", key="Ctrl+Shift+u")
    self._addButton("bulletButton", lambda s=self: toggleBullet(self),
                    text=u"1", tip="List (Ctrl+Shift+o)", key="Ctrl+Shift+o")
    self._addButton("farsiButton", lambda s=self: togglefarsi(self),
                    text=u"F", tip="List (Ctrl+Shift+f)", key="Ctrl+Shift+f")
    self._addButton("clearbtn", lambda s=self: clearboth(self),
                    text=u"Clr", tip="List (Ctrl+Shift+c)", key="Ctrl+Shift+c")

Editor.toggleList = toggleList
Editor.toggleBullet=toggleBullet
Editor.togglefarsi=togglefarsi
Editor.clearboth=clearboth
Editor.setupButtons = wrap(Editor.setupButtons, setupButtons)
