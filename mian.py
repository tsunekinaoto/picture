# -*- coding: utf-8 -*-
import sys
import PySide.QtGui
import PySide.QtCore
import PySide.QtUiTools
import os.path

class MainForm(PySide.QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = PySide.QtUiTools.QUiLoader().load('./MainDialog.ui')
        self.establishConnection()

    def openFile(self):
        filename = PySide.QtGui.QFileDialog.getOpenFileName(self,'Open file',os.path.expanduser('~')+'/Desktop')
        

    def establishConnection(self):
        self.ui.pushButton.clicked.connect(self.openFile)


if __name__ == '__main__':
    app = PySide.QtGui.QApplication(sys.argv)
    # app = PySide.QtGui.QApplication.instance()

    main_fome = MainForm()
    main_fome.ui.show()

    sys.exit(app.exec_())