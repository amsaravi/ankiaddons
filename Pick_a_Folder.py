from PyQt4 import QtGui  # Import the PyQt4 module we'll need
from PyQt4.QtGui import QDialog
import sys  # We need sys so that we can pass argv to QApplication

from folderDialog.GetFolderDlg  import Ui_PickFolderDlg # This file holds our MainWindow and all design related things

# it also keeps events etc that we defined in Qt Designer
import os
import shutil
from os import listdir
from os.path import isfile, join
#from test.test_decimal import directory
import uuid

class ExampleApp(Ui_PickFolderDlg):
    def __init__(self):
        Ui_PickFolderDlg.__init__(self)
        
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        self.txtDeckName.setText("Deafault")
        self.btnPickFolder.clicked.connect(self.browse_folder)  # When the button is pressed
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
            
def isImageFile(fileName,filePath):
    return os.path.isfile(join(filePath, fileName)) and fileName.endswith((".jpg",".jpeg",".gif",".png",".bmp"))



def createNewName(f):
    #generate unique file name and combine it with old file name
    lst_tmp = list(os.path.splitext(f))
    lst_tmp.insert(1, str(uuid.uuid4()))
    return "".join(lst_tmp)

def getFileNames(directory, f,newFileName):
    #combines file name with directory name
    return join(directory, f), join(os.getcwd(),newFileName)

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)

    if form.exec_():
        directory,deck,tag,move,rename=form.getData()
        getName=lambda x: x if not rename else createNewName(x)
        copy_move= shutil.move if move else shutil.copy
        files = [(new_fName,getFileNames(directory,f, new_fName)) #generates filename as ky and old and new adress as a tuple 
                 for f in sorted(os.listdir(directory))     
                 for new_fName in [getName(f)]      #generate new name or use old name
                  if isImageFile(f, directory) ] #just image files
        for f, paths in files:

            #expands the tuple the contains src and dest file path
            #and copies or moves it based on flags that has bean set            
            copy_move(*paths)

    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function