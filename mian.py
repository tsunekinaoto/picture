# -*- coding: utf-8 -*-
import sys
import PySide.QtGui
# import PySide.QtCore
import PySide.QtUiTools
import os.path
import re

class MainForm(PySide.QtGui.QMainWindow,PySide.QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = PySide.QtUiTools.QUiLoader().load('./MainDialog02.ui')
        self.establish()
        self.open_file_bottun = PySide.QtGui.QPushButton('pushButton')

    def pushButton(self):
        filename = PySide.QtGui.QFileDialog.getOpenFileName(self,'Open file',os.path.expanduser('~')+'/Desktop')
        self.x = filename[0]
        self.pic(self.x)
        

    def establish(self):
        self.ui.pushButton.clicked.connect(self.pushButton)

    def pic(self,x):
        pixmap = PySide.QtGui.QPixmap()
        pixmap.load(self.x)
        self.scene = PySide.QtGui.QGraphicsScene(self)
        item = PySide.QtGui.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.graphicsView.setScene(self.scene)

        __width = item.boundingRect().width()
        __height = item.boundingRect().height()
        
        """画像配置用ウィジットのデフォルトサイズ値を採取"""
        __x = 441
        __y = 341
        """画像に合わせてウィジットのサイズを変更"""
        self.graphicsView.setGeometry(QtCore.QRect(__x, __y, __width, __height))
        
        __main_x = int(__x + __width + 20)
        __main_y = int(__y + __height + 50)
        
        """画像に合わせてメインウィンドウのサイズ変更"""
        self.resize(__main_x,__main_y)
        """ウィジットに画像を配置"""
        scene.addItem(item)
        """前回作成したフォームとの関連付け"""
        self.graphicsView.setScene(scene)


if __name__ == '__main__':
    app = PySide.QtGui.QApplication(sys.argv)
    # app = PySide.QtGui.QApplication.instance()

    main_fome = MainForm()
    main_fome.ui.show()

    sys.exit(app.exec_())