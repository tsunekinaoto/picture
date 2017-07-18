# -*- coding: utf-8 -*-
import sys
import PySide.QtGui
# import PySide.QtCore
import PySide.QtUiTools
import os.path
import re
from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageOps



class MainForm(PySide.QtGui.QMainWindow,PySide.QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = PySide.QtUiTools.QUiLoader().load('./MainDialog02.ui')
        self.establish()
        self.open_file_bottun = PySide.QtGui.QPushButton('file_open')
        self.open_file_bottun = PySide.QtGui.QPushButton('gray_img')
        self.open_file_bottun = PySide.QtGui.QPushButton('mozaiku')
        self.open_file_bottun = PySide.QtGui.QPushButton('emboss_img')
        self.open_file_bottun = PySide.QtGui.QPushButton('noise_img')
        self.open_file_bottun = PySide.QtGui.QPushButton('reset_img')
        self.open_file_bottun = PySide.QtGui.QPushButton('opening_img')
        self.open_file_bottun = PySide.QtGui.QPushButton('closing_img')
        self.open_file_bottun = PySide.QtGui.QPushButton('pen_img')
        self.open_file_bottun = PySide.QtGui.QPushButton('edges_img')
        self.open_file_bottun = PySide.QtGui.QPushButton('save_button')
        self.list1 = []



    def pushButton(self):
        filename = PySide.QtGui.QFileDialog.getOpenFileName(self,'Open file',os.path.expanduser('~')+'/Desktop')
        self.original_pic = filename[0]
        img = Image.open(self.original_pic)
        self.list1.append(img)
        img.thumbnail((951,551),Image.ANTIALIAS)
        img.save('thumb.jpg')
        thumb_pass = os.path.abspath('thumb.jpg')
        self.original_pic = thumb_pass
        self.draw(self.original_pic)

    def saveButton(self):
        dir_path,_ = PySide.QtGui.QFileDialog.getSaveFileName(self, 'Open Directory',directory = '/home/kanglab/file/git/picture')

        img = Image.open(self.original_pic)
        img.save(dir_path)

    def reset_pic(self):
        img = Image.open(self.original_pic)
        reset_pass = os.path.abspath('thumb.jpg')
        self.original_pic = reset_pass
        self.draw(self.original_pic)

    def gray_pic(self):
        img = Image.open(self.original_pic)
        self.list1.append(img)
        gray_img = img.convert('L')
        gray_img.save('gray.jpg')
        gray_pass = os.path.abspath('gray.jpg')
        self.original_pic = gray_pass
        self.draw(self.original_pic)

    def moza_pic(self):
        img = Image.open(self.original_pic)
        self.list1.append(img)
        mozaimg = img.filter(ImageFilter.GaussianBlur(4))
        mozaimg.resize([x // 8 for x in img.size]).resize(img.size)
        mozaimg.save('moza.jpg')
        moza_pass = os.path.abspath('moza.jpg')
        self.original_pic = moza_pass
        self.draw(self.original_pic)

    def noise_pic(self):
        img = Image.open(self.original_pic)
        self.list1.append(img)
        noiseimg = img.filter(ImageFilter.MedianFilter())
        noiseimg.save('noise.jpg')
        noise_pass = os.path.abspath('noise.jpg')
        self.original_pic = noise_pass
        self.draw(self.original_pic)

    def emboss_pic(self):
        img = Image.open(self.original_pic)
        self.list1.append(img)
        embossimg = img.filter(ImageFilter.EMBOSS)
        embossimg.save('emboss.jpg')
        emboss_pass = os.path.abspath('emboss.jpg')
        self.original_pic = emboss_pass
        self.draw(self.original_pic)

    def opening_pic(self):
        img = Image.open(self.original_pic)
        self.list1.append(img)
        openingimg = img.filter(ImageFilter.MinFilter())
        openingimg.save('opening.jpg')
        opening_pass = os.path.abspath('opening.jpg')
        self.original_pic = opening_pass
        self.draw(self.original_pic)

    def closing_pic(self):
        img = Image.open(self.original_pic)
        self.list1.append(img)
        closingimg = img.filter(ImageFilter.MaxFilter())
        closingimg.save('closing.jpg')
        closing_pass = os.path.abspath('closing.jpg')
        self.original_pic = closing_pass
        self.draw(self.original_pic)

    def pen_pic(self):
        img = Image.open(self.original_pic)
        self.list1.append(img)
        gray = img.convert("L")
        gray2 = gray.filter(ImageFilter.MaxFilter(5))
        senga_inv = ImageChops.difference(gray, gray2)
        penimg = ImageOps.invert(senga_inv)
        penimg.save('pen.jpg')
        pen_pass = os.path.abspath('pen.jpg')
        self.original_pic = pen_pass
        self.draw(self.original_pic)

    def edges_pic(self):
        img = Image.open(self.original_pic)
        self.list1.append(img)
        edgesimg = img.filter(ImageFilter.FIND_EDGES)
        edgesimg.save('edges.jpg')
        edges_pass = os.path.abspath('edges.jpg')
        self.original_pic = edges_pass
        self.draw(self.original_pic)





    def establish(self):
        self.ui.file_open.clicked.connect(self.pushButton)
        self.ui.gray_img.clicked.connect(self.gray_pic)
        self.ui.mozaiku.clicked.connect(self.moza_pic)
        self.ui.emboss_img.clicked.connect(self.emboss_pic)
        self.ui.noise_img.clicked.connect(self.noise_pic)
        self.ui.reset_img.clicked.connect(self.reset_pic)
        self.ui.opening_img.clicked.connect(self.opening_pic)
        self.ui.closing_img.clicked.connect(self.closing_pic)
        self.ui.pen_img.clicked.connect(self.pen_pic)
        self.ui.edges_img.clicked.connect(self.edges_pic)
        self.ui.save_button.clicked.connect(self.saveButton)



    def draw(self,original_pic):
        pixmap = PySide.QtGui.QPixmap()
        pixmap.load(self.original_pic)
        self.scene = PySide.QtGui.QGraphicsScene(self)
        item = PySide.QtGui.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.graphicsView.setScene(self.scene)

if __name__ == '__main__':
    app = PySide.QtGui.QApplication(sys.argv)
    # app = PySide.QtGui.QApplication.instance()

    main_fome = MainForm()
    main_fome.ui.show()

    sys.exit(app.exec_())