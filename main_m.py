import sys
from PySide import QtCore,QtGui

"""生成されたフォームのファイルからフォームをインポート"""
from pyqt_Opencv import Ui_Qt_CV_MainWindow

"""おまじない その1"""
class DesignerMainWindow(QtGui.QMainWindow,Ui_Qt_CV_MainWindow):
 def __init__(self, parent = None):
    super(DesignerMainWindow, self).__init__(parent)
    self.ui = Ui_Qt_CV_MainWindow()
    self.setupUi(self)
    """おまじない その1終わり"""
    
    """シグナル&スロット：file_buttonをクリックすると、open_file関数を実行"""
    QtCore.QObject.connect(self.file_button, QtCore.SIGNAL("clicked()"), self.open_file)
 """open_file関数"""
 def open_file(self):
    """「ファイルを開く」ダイアログにて画像読み込み"""
    file = QtGui.QFileDialog.getOpenFileName()
        if file:
        	"""file_edit(Line editオブジェクト）にファイルアドレスをセット"""
        	self.file_edit.setText(file[0])
		"""画像配置用ウィジット生成"""
		scene = QtGui.QGraphicsScene()
        	"""PixmapItem形式で画像を取り込み"""
		pic_Item = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(file[0]))
            	"""画像の幅と高さ情報を採取"""
        	__width = pic_Item.boundingRect().width()
        	__height = pic_Item.boundingRect().height()
        	"""画像配置用ウィジットのデフォルトサイズ値を採取"""
        	__x = self.pic_View.x()
        	__y = self.pic_View.y()
        	"""画像に合わせてウィジットのサイズを変更"""
        	self.pic_View.setGeometry(QtCore.QRect(__x, __y, __width, __height))
        	
        	__main_x = int(__x + __width + 20)
        	__main_y = int(__y + __height + 50)
        	
        	"""画像に合わせてメインウィンドウのサイズ変更"""
        	self.resize(__main_x,__main_y)
        	"""ウィジットに画像を配置"""
        	scene.addItem(pic_Item)
        	"""前回作成したフォームとの関連付け"""
        	self.pic_View.setScene(scene)

if __name__ == '__main__':
	"""おまじない その２"""
	app = QtGui.QApplication(sys.argv)
	dmw = DesignerMainWindow()
	dmw.show()
	sys.exit(app.exec_())
	"""おまじない その2終わり"""