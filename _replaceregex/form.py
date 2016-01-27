# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_ReplaceRegexDialog(object):
    def setupUi(self, ReplaceRegexDialog):
        ReplaceRegexDialog.setObjectName(_fromUtf8("ReplaceRegexDialog"))
        ReplaceRegexDialog.resize(400, 284)
        self.verticalLayout = QtGui.QVBoxLayout(ReplaceRegexDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fieldLabel = QtGui.QLabel(ReplaceRegexDialog)
        self.fieldLabel.setObjectName(_fromUtf8("fieldLabel"))
        self.gridLayout.addWidget(self.fieldLabel, 0, 0, 1, 1)
        self.searchEdit = QtGui.QTextEdit(ReplaceRegexDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy)
        self.searchEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.gridLayout.addWidget(self.searchEdit, 1, 1, 1, 1)
        self.searchLabel = QtGui.QLabel(ReplaceRegexDialog)
        self.searchLabel.setObjectName(_fromUtf8("searchLabel"))
        self.gridLayout.addWidget(self.searchLabel, 1, 0, 1, 1)
        self.replaceLabel = QtGui.QLabel(ReplaceRegexDialog)
        self.replaceLabel.setObjectName(_fromUtf8("replaceLabel"))
        self.gridLayout.addWidget(self.replaceLabel, 2, 0, 1, 1)
        self.replaceEdit = QtGui.QTextEdit(ReplaceRegexDialog)
        self.replaceEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.replaceEdit.setObjectName(_fromUtf8("replaceEdit"))
        self.gridLayout.addWidget(self.replaceEdit, 2, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fieldEdit = QtGui.QLineEdit(ReplaceRegexDialog)
        self.fieldEdit.setObjectName(_fromUtf8("fieldEdit"))
        self.horizontalLayout.addWidget(self.fieldEdit)
        self.anyFieldCheckBox = QtGui.QCheckBox(ReplaceRegexDialog)
        self.anyFieldCheckBox.setObjectName(_fromUtf8("anyFieldCheckBox"))
        self.horizontalLayout.addWidget(self.anyFieldCheckBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(ReplaceRegexDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ReplaceRegexDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ReplaceRegexDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ReplaceRegexDialog)

    def retranslateUi(self, ReplaceRegexDialog):
        ReplaceRegexDialog.setWindowTitle(_translate("ReplaceRegexDialog", "Replace Regex", None))
        self.fieldLabel.setText(_translate("ReplaceRegexDialog", "Field (Regex)", None))
        self.searchEdit.setHtml(_translate("ReplaceRegexDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;img[^&gt;]+src=&quot;(.+)&quot;[^&gt;]+/?&gt;</p></body></html>", None))
        self.searchLabel.setText(_translate("ReplaceRegexDialog", "Search (Regex)", None))
        self.replaceLabel.setText(_translate("ReplaceRegexDialog", "Replace (Regex)", None))
        self.replaceEdit.setHtml(_translate("ReplaceRegexDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Image-URL: \\1</p></body></html>", None))
        self.fieldEdit.setText(_translate("ReplaceRegexDialog", "(Expression|Reading)", None))
        self.anyFieldCheckBox.setText(_translate("ReplaceRegexDialog", "Any Field", None))

