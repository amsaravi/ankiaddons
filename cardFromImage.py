from PyQt4 import QtGui  # Import the PyQt4 module we'll need
from PyQt4.QtGui import QDialog, QAction
import sys
from aqt import mw
from aqt.qt import *
from aqt.utils import tooltip
from anki import notes


from folderdialog.get_folder_dlg  import Ui_PickFolderDlg  # This file holds our MainWindow and all design related things


import os  # For listing directory methods
from os import listdir
from os.path import isfile, join
import shutil
import uuid

_CHECK_MOVE_FILES = True
_CHECL_RENAME_FILES = True
_DEFAULT_DECK="Default"
_DEFAULT_DIR=""
class addonDialog(Ui_PickFolderDlg):
    def __init__(self):
        Ui_PickFolderDlg.__init__(self)
        
        self.setupUi(self)  # This is defined in GetFolderDlg.py file automatically
        self.txtDeckName.setText(_DEFAULT_DECK)
        self.btnPickFolder.clicked.connect(self.browse_folder)
        self.chkMoveFiles.setChecked(_CHECK_MOVE_FILES)
        self.chkRenameFiles.setChecked(_CHECL_RENAME_FILES)
        self.txtFolderName.setText(_DEFAULT_DIR) 
        # It sets up layout and widgets that are defined
        # self.btnPickFolder.clicked.connect(self.browse_folder)  # When the button is pressed
         # Execute browse_folder function
    def browse_folder(self):
        # self.lstFolderContent.clear() # In case there are any existing elements in the list
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder",self.txtFolderName.text())

        if directory:  # if user didn't pick a directory don't continue
            files = [f for f in os.listdir(directory) if isImageFile(f, directory) ]
            for f in files:
                pass
                # for all files, if any, in the directory
                # self.lstFolderContent.addItem(f)  # add file to the lstFolderContent
            self.lblImagesCount.setText("Images count: {0}".format(len(files)))
            self.txtFolderName.setText(directory)
            
    
    def get_dec(self):
        pass


def createNewName(f):
    # generate unique file name and combine it with old file name
    lst_tmp = list(os.path.splitext(f))
    lst_tmp.insert(1, str(uuid.uuid4()))
    return "".join(lst_tmp)

def getFileNames(directory, f, newFileName):
    # combines file name with directory name
    return join(directory, f), join(mw.col.media.folder(), newFileName)
  
def import_images(directory, decName, tags, move, rename):
    # first of all, copy all images into anki's media directory
    getName = lambda x: x if not rename else createNewName(x)
    copy_move = shutil.move if move else shutil.copy
    files = [(new_fName, getFileNames(directory, f, new_fName))  # generates filename as ky and old and new adress as a tuple 
             for f in sorted(os.listdir(directory))     
             for new_fName in [getName(f)]  # generate new name or use old name
              if isImageFile(f, directory) ]
    filesCount = len(files)
    if not filesCount:
        return
    
    # create new deck and custom model
    model  = mw.col.models.byName("Basic2")
    did=mw.col.decks.id(decName)

    txt = u"""
    <div><img src="{0}" /></div>
    """
    
    for f, path in files:
        note = notes.Note(mw.col, model)
        note.model()['did'] = did
        note["Front"] = txt.format(f)
        note["Back"] = ""
        
        tagList = mw.col.tags.split(tags)
        for tag in tagList:
            note.addTag(tag)
        
        mw.app.processEvents()
        mw.col.addNote(note)
        copy_move(*path)
    mw.col.reset()
    mw.reset()
        
    tooltip("{0} images Imported...".format(filesCount))
    
def isImageFile(fileName, filePath):
    return os.path.isfile(join(filePath, fileName)) and fileName.endswith((".jpg", ".jpeg", ".gif", ".png", ".bmp"))
    
def importFromImages():
    global __window
    __window = addonDialog()
    if __window.exec_():
        if(__window.selectedFolder):
            import_images(*__window.getData())     
    

action = QAction("Images to Cards", mw)
mw.connect(action, SIGNAL("triggered()"), importFromImages)
mw.form.menuTools.addAction(action)
