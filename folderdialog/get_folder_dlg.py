# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetFolderDlg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog

class Ui_PickFolderDlg(QDialog):
    
    def __init__(self):
        QDialog.__init__(self)
        self.selectedFolder=""
        self.deckName=""
        self.tags=""
        self.moveFiles=False
        self.renameFiles=False
        
    def setupUi(self, PickFolderDlg):
        PickFolderDlg.setObjectName("PickFolderDlg")
        PickFolderDlg.resize(350, 146)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PickFolderDlg.sizePolicy().hasHeightForWidth())
        PickFolderDlg.setSizePolicy(sizePolicy)
        PickFolderDlg.setMinimumSize(QtCore.QSize(100, 12))
        self.gridLayout = QtGui.QGridLayout(PickFolderDlg)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutInputs = QtGui.QGridLayout()
        self.gridLayoutInputs.setObjectName("gridLayoutInputs")
        self.lblImageFolder = QtGui.QLabel(PickFolderDlg)
        self.lblImageFolder.setObjectName("lblImageFolder")
        self.gridLayoutInputs.addWidget(self.lblImageFolder, 0, 0, 1, 1)
        self.txtFolderName = QtGui.QLineEdit(PickFolderDlg)
        self.txtFolderName.setObjectName("txtFolderName")
        self.gridLayoutInputs.addWidget(self.txtFolderName, 0, 1, 1, 1)
        self.btnPickFolder = QtGui.QPushButton(PickFolderDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPickFolder.sizePolicy().hasHeightForWidth())
        self.btnPickFolder.setSizePolicy(sizePolicy)
        self.btnPickFolder.setMinimumSize(QtCore.QSize(75, 23))
        self.btnPickFolder.setSizeIncrement(QtCore.QSize(0, 0))
        self.btnPickFolder.setObjectName("btnPickFolder")
        self.gridLayoutInputs.addWidget(self.btnPickFolder, 0, 2, 1, 1)
        self.lblDeckName = QtGui.QLabel(PickFolderDlg)
        self.lblDeckName.setObjectName("lblDeckName")
        self.gridLayoutInputs.addWidget(self.lblDeckName, 1, 0, 1, 1)
        self.txtDeckName = QtGui.QLineEdit(PickFolderDlg)
        self.txtDeckName.setObjectName("txtDeckName")
        self.gridLayoutInputs.addWidget(self.txtDeckName, 1, 1, 1, 2)
        self.lblTagName = QtGui.QLabel(PickFolderDlg)
        self.lblTagName.setObjectName("lblTagName")
        self.gridLayoutInputs.addWidget(self.lblTagName, 2, 0, 1, 1)
        self.txtTagName = QtGui.QLineEdit(PickFolderDlg)
        self.txtTagName.setObjectName("txtTagName")
        self.gridLayoutInputs.addWidget(self.txtTagName, 2, 1, 1, 2)
        self.chkMoveFiles = QtGui.QCheckBox(PickFolderDlg)
        self.chkMoveFiles.setObjectName("chkMoveFiles")        
        self.gridLayoutInputs.addWidget(self.chkMoveFiles, 3, 0, 1, 1)
        self.chkRenameFiles = QtGui.QCheckBox(PickFolderDlg)
        self.chkRenameFiles.setObjectName("chkRenameFiles")
        self.gridLayoutInputs.addWidget(self.chkRenameFiles, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayoutInputs, 0, 0, 1, 1)
        
        self.lblImagesCount = QtGui.QLabel(PickFolderDlg)
        self.lblImageFolder.setObjectName("lblImagesCount")
        self.gridLayout.addWidget(self.lblImagesCount)
        
        
        self.btnbxDialogButtons = QtGui.QDialogButtonBox(PickFolderDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnbxDialogButtons.sizePolicy().hasHeightForWidth())
        self.btnbxDialogButtons.setSizePolicy(sizePolicy)
        self.btnbxDialogButtons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnbxDialogButtons.setObjectName("btnbxDialogButtons")
        self.gridLayout.addWidget(self.btnbxDialogButtons, 1, 0, 1, 1)

        self.retranslateUi(PickFolderDlg)
        
        QtCore.QObject.connect(self.btnbxDialogButtons, QtCore.SIGNAL("accepted()"), self.importSelected)
        QtCore.QObject.connect(self.btnbxDialogButtons, QtCore.SIGNAL("rejected()"), PickFolderDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(PickFolderDlg)

    def retranslateUi(self, PickFolderDlg):
        PickFolderDlg.setWindowTitle("Form")
        self.lblImageFolder.setText("Images Folder")
        self.btnPickFolder.setText("Brows...")
        self.lblDeckName.setText("Deck Name")
        self.lblTagName.setText("Tag")
        self.lblImagesCount.setText("Images count: ")
        self.chkMoveFiles.setText("Move files")
        self.chkRenameFiles.setText("Rename Files")
        
    def importSelected(self):
        self.selectedFolder=self.txtFolderName.text()
        self.deckName=self.txtDeckName.text()
        self.tags=self.txtTagName.text()
        self.moveFiles=self.chkMoveFiles.isChecked()
        self.renameFiles=self.chkRenameFiles.isChecked()
        self.accept()
        
    def getData(self):
        return (self.selectedFolder,self.deckName, self.tags,self.moveFiles, self.renameFiles)