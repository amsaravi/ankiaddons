# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetFolderDlg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PickFolderDlg(QDialog):
    
    def __init__(self):
        QDialog.__init__(self)
        self.selectedFolder=""
        self.deckName=""
        self.tags=""
        
    def setupUi(self, PickFolderDlg):
        PickFolderDlg.setObjectName(_fromUtf8("PickFolderDlg"))
        PickFolderDlg.resize(350, 130)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PickFolderDlg.sizePolicy().hasHeightForWidth())
        PickFolderDlg.setSizePolicy(sizePolicy)
        PickFolderDlg.setMinimumSize(QtCore.QSize(100, 12))
        self.gridLayout = QtGui.QGridLayout(PickFolderDlg)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayoutInputs = QtGui.QGridLayout()
        self.gridLayoutInputs.setObjectName(_fromUtf8("gridLayoutInputs"))
        self.lblImageFolder = QtGui.QLabel(PickFolderDlg)
        self.lblImageFolder.setObjectName(_fromUtf8("lblImageFolder"))
        self.gridLayoutInputs.addWidget(self.lblImageFolder, 0, 0, 1, 1)
        self.txtFolderName = QtGui.QLineEdit(PickFolderDlg)
        self.txtFolderName.setObjectName(_fromUtf8("txtFolderName"))
        self.gridLayoutInputs.addWidget(self.txtFolderName, 0, 1, 1, 1)
        self.btnPickFolder = QtGui.QPushButton(PickFolderDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPickFolder.sizePolicy().hasHeightForWidth())
        self.btnPickFolder.setSizePolicy(sizePolicy)
        self.btnPickFolder.setMinimumSize(QtCore.QSize(75, 23))
        self.btnPickFolder.setSizeIncrement(QtCore.QSize(0, 0))
        self.btnPickFolder.setObjectName(_fromUtf8("btnPickFolder"))
        self.gridLayoutInputs.addWidget(self.btnPickFolder, 0, 2, 1, 1)
        self.lblDeckName = QtGui.QLabel(PickFolderDlg)
        self.lblDeckName.setObjectName(_fromUtf8("lblDeckName"))
        self.gridLayoutInputs.addWidget(self.lblDeckName, 1, 0, 1, 1)
        self.txtDeckName = QtGui.QLineEdit(PickFolderDlg)
        self.txtDeckName.setObjectName(_fromUtf8("txtDeckName"))
        self.gridLayoutInputs.addWidget(self.txtDeckName, 1, 1, 1, 2)
        self.lblTagName = QtGui.QLabel(PickFolderDlg)
        self.lblTagName.setObjectName(_fromUtf8("lblTagName"))
        self.gridLayoutInputs.addWidget(self.lblTagName, 2, 0, 1, 1)
        self.txtTagName = QtGui.QLineEdit(PickFolderDlg)
        self.txtTagName.setObjectName(_fromUtf8("txtTagName"))
        self.gridLayoutInputs.addWidget(self.txtTagName, 2, 1, 1, 2)
        self.gridLayout.addLayout(self.gridLayoutInputs, 0, 0, 1, 1)
        
        self.lblImagesCount = QtGui.QLabel(PickFolderDlg)
        self.lblImageFolder.setObjectName(_fromUtf8("lblImagesCount"))
        self.gridLayout.addWidget(self.lblImagesCount)
        
        
        self.btnbxDialogButtons = QtGui.QDialogButtonBox(PickFolderDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnbxDialogButtons.sizePolicy().hasHeightForWidth())
        self.btnbxDialogButtons.setSizePolicy(sizePolicy)
        self.btnbxDialogButtons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnbxDialogButtons.setObjectName(_fromUtf8("btnbxDialogButtons"))
        self.gridLayout.addWidget(self.btnbxDialogButtons, 1, 0, 1, 1)

        self.retranslateUi(PickFolderDlg)
        
        QtCore.QObject.connect(self.btnbxDialogButtons, QtCore.SIGNAL(_fromUtf8("accepted()")), self.importSelected)
        QtCore.QObject.connect(self.btnbxDialogButtons, QtCore.SIGNAL(_fromUtf8("rejected()")), PickFolderDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(PickFolderDlg)

    def retranslateUi(self, PickFolderDlg):
        PickFolderDlg.setWindowTitle(_translate("PickFolderDlg", "Form", None))
        self.lblImageFolder.setText(_translate("PickFolderDlg", "Images Folder", None))
        self.btnPickFolder.setText(_translate("PickFolderDlg", "Brows...", None))
        self.lblDeckName.setText(_translate("PickFolderDlg", "Deck Name", None))
        self.lblTagName.setText(_translate("PickFolderDlg", "Tag", None))
        self.lblImagesCount.setText(_translate("PickFolderDlg", "Images count: ", None))
        
    def importSelected(self):
        self.selectedFolder=self.txtFolderName.text()
        self.deckName=self.txtDeckName.text()
        self.tags=self.txtTagName.text()
        self.accept()
        
    def getData(self):
        return (self.selectedFolder,self.deckName, self.tags)