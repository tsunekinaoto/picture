# -*- coding: utf-8 -*-
import sys
import PySide.QtGui
# import PySide.QtCore
import PySide.QtUiTools
import os.path
import re
from PIL import Image

class MainForm(PySide.QtGui.QMainWindow,PySide.QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = PySide.QtUiTools.QUiLoader().load('./MainDialog02.ui')
        self.establish()
        self.open_file_bottun = PySide.QtGui.QPushButton('file_open')
        self.open_file_bottun = PySide.QtGui.QPushButton('gray_img')

    def pushButton(self):
        filename = PySide.QtGui.QFileDialog.getOpenFileName(self,'Open file',os.path.expanduser('~')+'/Desktop')
        self.original_pic = filename[0]
        self.draw(self.original_pic)

        
    def gray_pic(self):
        img = Image.open(str(self.original_pic))
        gray_img = img.convert('L')
        gray_img.save('gray.jpg')
        # gray_pass = PySide.QtGui.QFileDialog.getOpenFileName('gray.jpg')
        gray_pass = os.path.abspath('gray.jpg')
        print gray_pass
        self.original_pic = gray_pass
        self.draw(self.original_pic)


    def establish(self):
        self.ui.file_open.clicked.connect(self.pushButton)
        self.ui.gray_img.clicked.connect(self.gray_pic)

    def draw(self,original_pic):
        pixmap = PySide.QtGui.QPixmap()
        pixmap.load(self.original_pic)
        self.scene = PySide.QtGui.QGraphicsScene(self)
        item = PySide.QtGui.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.graphicsView.setScene(self.scene)

        # __width = item.boundingRect().width()
        # __height = item.boundingRect().height()
        
        # """画像配置用ウィジットのデフォルトサイズ値を採取"""
        # __x = 441
        # __y = 341
        # """画像に合わせてウィジットのサイズを変更"""
        # self.graphicsView.setGeometry(QtCore.QRect(__x, __y, __width, __height))
        
        # __main_x = int(__x + __width + 20)
        # __main_y = int(__y + __height + 50)
        
        # """画像に合わせてメインウィンドウのサイズ変更"""
        # self.resize(__main_x,__main_y)
        # """ウィジットに画像を配置"""
        # scene.addItem(item)
        # """前回作成したフォームとの関連付け"""
        # self.graphicsView.setScene(scene)


if __name__ == '__main__':
    app = PySide.QtGui.QApplication(sys.argv)
    # app = PySide.QtGui.QApplication.instance()

    main_fome = MainForm()
    main_fome.ui.show()

    sys.exit(app.exec_())