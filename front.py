import sys
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import camera

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent) # 初期化
        self.initUI() # UIの初期化

    def initUI(self): # UIの初期化をするメソッド
        self.resize(1000, 600) # ウィンドウの大きさの設定(横幅, 縦幅)
        self.move(-10, 0) # ウィンドウを表示する場所の設定(横, 縦)
        self.setWindowTitle('居眠り防止アプリケーション') # ウィンドウのタイトルの設定
        #self.setWindowIcon(QIcon('xxxx.jpg')) # ウィンドウ右上のアイコンの設定

    # ラベル名の設定
        lbl1 = QLabel('<p><font size="40" color="#00ff00">居眠り防止アプリ</font></p>', self)
        # ラベルをx=15,y=10へ移動
        lbl1.move(300, 10)
        
        btn1 = QPushButton('スタート！', self) # ボタンウィジェット作成
        btn1.move(200, 200) # ボタンの位置設定(ボタンの左上の座標)
        btn1.resize(200,100)
        btn1.setStyleSheet('QPushButton {background-color: lightseagreen}')
    
        btn2 = QPushButton('設定', self) # ボタンウィジェット作成
        btn2.resize(btn2.sizeHint()) # ボタンのサイズの自動設定
        btn2.move(600, 200) # ボタンの位置設定(ボタンの左上の座標)
        
        btn3 = QPushButton('ログ', self) # ボタンウィジェット作成
        btn3.resize(btn3.sizeHint()) # ボタンのサイズの自動設定
        btn3.move(600, 280) # ボタンの位置設定(ボタンの左上の座標)
    
        btn1.clicked.connect(camera.camera)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv) #PyQtで必ず呼び出す必要のあるオブジェクト
    main_window = MainWindow() #ウィンドウクラスのオブジェクト生成
    main_window.show() #ウィンドウの表示
    sys.exit(app.exec_()) #プログラム終了