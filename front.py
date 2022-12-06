import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import PySimpleGUI as sg
import tkinter as tk
from tkinter import ttk
import camera
import main
import requests
import json

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
            
        self.sub=log_window()
        
        btn1.clicked.connect(camera.camera)
        btn3.clicked.connect(self.sub.show)
        btn3.clicked.connect(self.close)
       
class log_window(QWidget):
    def __init__(self,parent=None):
        super(log_window, self).__init__(parent) # 初期化
        #self.initUI() # UIの初期化
        
    #def initUI(self):
        self.resize(800, 400) # ウィンドウの大きさの設定(横幅, 縦幅)
        self.move(-10, 0) # ウィンドウを表示する場所の設定(横, 縦)
        self.setWindowTitle('ログ') # ウィンドウのタイトルの設定
        #self.setWindowIcon(QIcon('xxxx.jpg')) # ウィンドウ右上のアイコンの設定

        # ラベル名の設定
        lbl1 = QLabel('<p><font size="40" color="#00ff00">ログ</font></p>', self)
        lbl1.move(350, 10)
        
        btn1 = QPushButton('集中', self) # ボタンウィジェット作成
        btn1.move(250, 100) # ボタンの位置設定(ボタンの左上の座標)
        btn1.resize(300,50)
        btn1.setStyleSheet('QPushButton {background-color: lightseagreen}')
    
        btn2 = QPushButton('全て取得', self) # ボタンウィジェット作成
        btn2.move(250, 200) # ボタンの位置設定(ボタンの左上の座標)
        btn2.resize(300, 50) # ボタンのサイズの自動設定
        btn2.setStyleSheet('QPushButton {background-color: lightseagreen}')
        
        btn3 = QPushButton('戻る', self) # ボタンウィジェット作成
        btn3.resize(btn3.sizeHint()) # ボタンのサイズの自動設定
        btn3.move(0, 20) # ボタンの位置設定(ボタンの左上の座標)
        btn3.setStyleSheet('QPushButton {background-color: lightseagreen}')
        
        btn2.clicked.connect(self.log_screen)
        btn3.clicked.connect(self.window_close)
        
        
    def log_screen(self):
        all_data = main.Refister_item()
        
        url = "http://127.0.0.1:8000/all"
        r = requests.get(url)
        data = r.json()
        
        # 列の識別名を指定
        column = ('ID', 'Name', 'Score')
        # メインウィンドウの生成
        root = tk.Tk()
        root.title('ログ')
        root.geometry('1200x800')
        # Treeviewの生成
        tree = ttk.Treeview(root, columns=column)
        # 文字サイズ
        style = ttk.Style()
        style.configure("Treeview", font=(None, 15), rowheight=40)
        style.configure("Treeview.Heading", font=(None, 20, 'bold'))
        # 列の設定
        tree.column('#0',width=0, stretch='no')
        tree.column('ID', anchor='center', width=200)
        tree.column('Name',anchor='w', width=400)
        tree.column('Score', anchor='center', width=400)
        # 列の見出し設定
        tree.heading('#0',text='')
        tree.heading('ID', text='ID',anchor='center')
        tree.heading('Name', text='student_number', anchor='w')
        tree.heading('Score',text='sleep_time', anchor='center')
        # レコードの追加
        
        for v in data.values():
            for i in range(len(v)):
                # v[i] : i番目のタプル
                tree.insert(parent='', index='end', iid=0 ,values=(i+1, v[i]['student_number'], v[i]['sleep_time']))        
        
        # ウィジェットの配置
        tree.pack(pady=10)
        root.mainloop()
    
    def window_close(self):
        self.main = MainWindow()
        self.main.show()
        self.close()
 

if __name__ == '__main__':
    app = QApplication(sys.argv) #PyQtで必ず呼び出す必要のあるオブジェクト
    main_window = MainWindow() #ウィンドウクラスのオブジェクト生成
    main_window.show() #ウィンドウの表示
    
    sys.exit(app.exec_()) #プログラム終了