import sys
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import tkinter as tk
from tkinter import ttk
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
        btn2.setStyleSheet('QPushButton {background-color: lightseagreen}')
        
        btn3 = QPushButton('ログ', self) # ボタンウィジェット作成
        btn3.resize(btn3.sizeHint()) # ボタンのサイズの自動設定
        btn3.move(600, 280) # ボタンの位置設定(ボタンの左上の座標)
        btn3.setStyleSheet('QPushButton {background-color: lightseagreen}')
            
        btn1.clicked.connect(camera.camera)
        btn3.clicked.connect(self.log_screen)
        
    def log_screen(self):
        # 列の識別名を指定
        column = ('ID', 'Name', 'Score')
        # メインウィンドウの生成
        root = tk.Tk()
        root.title('ログ')
        root.geometry('1000x600')
        # Treeviewの生成
        tree = ttk.Treeview(root, columns=column)
        # 文字サイズ
        style = ttk.Style()
        style.configure("Treeview", font=(None, 15), rowheight=40)
        style.configure("Treeview.Heading", font=(None, 20, 'bold'))
        # 列の設定
        tree.column('#0',width=0, stretch='no')
        tree.column('ID', anchor='center', width=200)
        tree.column('Name',anchor='w', width=300)
        tree.column('Score', anchor='center', width=200)
        # 列の見出し設定
        tree.heading('#0',text='')
        tree.heading('ID', text='ID',anchor='center')
        tree.heading('Name', text='Name', anchor='w')
        tree.heading('Score',text='Score', anchor='center')
        # レコードの追加
        tree.insert(parent='', index='end', iid=0 ,values=(1, 'KAWASAKI',80))
        tree.insert(parent='', index='end', iid=1 ,values=(2,'SHIMIZU', 90))
        tree.insert(parent='', index='end', iid=2, values=(3,'TANAKA', 45))
        tree.insert(parent='', index='end', iid=3, values=(4,'OKABE', 60))
        tree.insert(parent='', index='end', iid=4, values=(5,'MIYAZAKI', 99))
        # ウィジェットの配置
        tree.pack(pady=10)

        root.mainloop()    

if __name__ == '__main__':
    app = QApplication(sys.argv) #PyQtで必ず呼び出す必要のあるオブジェクト
    main_window = MainWindow() #ウィンドウクラスのオブジェクト生成
    main_window.show() #ウィンドウの表示
    
    sys.exit(app.exec_()) #プログラム終了