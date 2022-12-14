import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import tkinter as tk
from tkinter import ttk
from tkinter import font
import datetime
import camera
import main
import requests
import json

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent) # 初期化
        
        QWidget.__init__(self)
        self.layout = QGridLayout()
        
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('#FFFFE0')) # 背景色
        self.setPalette(p)
        
        self.initUI() # UIの初期化

    def initUI(self): # UIの初期化をするメソッド
        
        self.resize(800, 500) # ウィンドウの大きさの設定(横幅, 縦幅)
        self.move(-10, 0) # ウィンドウを表示する場所の設定(横, 縦)
        self.setWindowTitle('居眠り防止アプリケーション') # ウィンドウのタイトルの設定
        #self.setWindowIcon(QIcon('xxxx.jpg')) # ウィンドウ右上のアイコンの設定

        # ラベル名の設定
        lbl1 = QLabel('<p><font size="40" color="#00ff00">居眠り防止アプリ</font></p>', self)
        lbl1.move(250, 10)
        
        btn1 = QPushButton('スタート！', self) # ボタンウィジェット作成
        btn1.move(150, 200) # ボタンの位置設定
        btn1.resize(200,100)
        btn1.setStyleSheet('QPushButton {background-color: lightseagreen}')
    
        btn2 = QPushButton('設定', self) # ボタンウィジェット作成
        btn2.resize(btn2.sizeHint()) # ボタンのサイズの自動設定
        btn2.move(550, 200) # ボタンの位置設定
        btn2.setStyleSheet('QPushButton {background-color: lightseagreen}')
        
        btn3 = QPushButton('ログ', self) # ボタンウィジェット作成
        btn3.resize(btn3.sizeHint()) # ボタンのサイズの自動設定
        btn3.move(550, 280) # ボタンの位置設定
        btn3.setStyleSheet('QPushButton {background-color: lightseagreen}')
            
        self.sub=log_window()
        
        btn1.clicked.connect(camera.camera)
        btn3.clicked.connect(self.sub.show)
        btn3.clicked.connect(self.close)
       
class log_window(QWidget):
    def __init__(self,parent=None):
        super(log_window, self).__init__(parent) # 初期化
        
        QWidget.__init__(self)
        self.layout = QGridLayout()
        
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('#FFFFE0')) # 背景色
        self.setPalette(p)
        
        #self.initUI() # UIの初期化
        
    #def initUI(self):
        self.resize(800, 400) # ウィンドウの大きさの設定(横幅, 縦幅)
        self.move(-10, 0) # ウィンドウを表示する場所の設定(横, 縦)
        self.setWindowTitle('ログ') # ウィンドウのタイトルの設定
        #self.setWindowIcon(QIcon('xxxx.jpg')) # ウィンドウ右上のアイコンの設定

        # ラベル名の設定
        lbl1 = QLabel('<p><font size="40" color="#00ff00">ログ</font></p>', self)
        lbl1.move(350, 10)
        
        btn1 = QPushButton('寝落ち集中時間帯', self) # ボタンウィジェット作成
        btn1.move(250, 100) # ボタンの位置設定
        btn1.resize(300,50)
        btn1.setStyleSheet('QPushButton {background-color: lightseagreen}')
    
        btn2 = QPushButton('全て取得', self) # ボタンウィジェット作成
        btn2.move(250, 200) # ボタンの位置設定
        btn2.resize(300, 50) # ボタンのサイズの自動設定
        btn2.setStyleSheet('QPushButton {background-color: lightseagreen}')
        
        btn3 = QPushButton('戻る', self) # ボタンウィジェット作成
        btn3.resize(btn3.sizeHint()) # ボタンのサイズの自動設定
        btn3.move(0, 20) # ボタンの位置設定
        btn3.setStyleSheet('QPushButton {background-color: lightseagreen}')
        
        btn1.clicked.connect(self.log_intensive_screen)
        btn2.clicked.connect(self.log_screen)
        btn3.clicked.connect(self.window_close)
        
        
    def log_intensive_screen(self):
        url = "http://127.0.0.1:8000/intensive"
        r = requests.get(url)
        data = r.json()
        
        # 列の識別名を指定
        column = ('ID', 'Time')
        # メインウィンドウの生成
        root = tk.Tk()
        root.title('寝落ち集中時間帯')
        root.geometry('1200x800')
        
        font1 = font.Font(family='Helvetica', size=20, weight='bold')
        label1 = tk.Label(root, text="以下の時間帯に居眠りが集中しています!!", fg="red", font=font1)
        label1.pack(side="top")
        label2 = tk.Label(root, text="当該時間に演習を行うなどの授業内容の変更をお勧めします。", fg="black", font=font1)
        label2.place(x=50, y=550)
        # Treeviewの生成
        tree = ttk.Treeview(root, columns=column)
        # 文字サイズ
        style = ttk.Style()
        style.configure("Treeview", font=(None, 15), rowheight=40)
        style.configure("Treeview.Heading", font=(None, 20, 'bold'))
        # 列の設定
        tree.column('#0',width=0, stretch='no')
        tree.column('ID', anchor='center', width=100)
        tree.column('Time', anchor='center', width=400)
        # 列の見出し設定
        tree.heading('#0',text='')
        tree.heading('ID',text='ID', anchor='center')
        tree.heading('Time',text='Time', anchor='center')
        # レコードの追加
        
        judge = 0
        for v in data.values():
            for i in range(len(v)):
                # v[i] : i番目のタプル
                #if v[i]['start']:
                num1 = v[i]['start_hour']
                num2 = v[i]['start_minutes']
                num3 = v[i]['end_hour']
                num4 = v[i]['end_minutes']
                s1 = f'{num1:02}'
                s2 = f'{num2:02}'
                s3 = f'{num3:02}'
                s4 = f'{num4:02}'
                tree.insert(parent='', index='end', iid=i ,values=(i+1,str(s1) + ":" + str(s2) + "～" + str(s3) + ":" + str(s4)))        
                
                if i==9:
                    judge = 1
                    break
            if judge == 1:
                break
        # ウィジェットの配置
        tree.pack(pady=10)
        root.mainloop()
        
         
    def log_screen(self):
        
        url = "http://127.0.0.1:8000/all"
        r = requests.get(url)
        data = r.json()
        
        # 列の識別名を指定
        column = ('ID', 'Student_Number', 'Sleep_Time')
        # メインウィンドウの生成
        root = tk.Tk()
        root.title('全て取得')
        root.geometry('1300x800')
        
        font1 = font.Font(family='Helvetica', size=20, weight='bold')
        label2 = tk.Label(root, text="学籍番号及び居眠り時間帯", fg="black", font=font1)
        label2.pack(side="top")
        
        # Treeviewの生成
        tree = ttk.Treeview(root, columns=column)
        # 文字サイズ
        style = ttk.Style()
        style.configure("Treeview", font=(None, 15), rowheight=40)
        style.configure("Treeview.Heading", font=(None, 20, 'bold'))
        # 列の設定
        tree.column('#0',width=0, stretch='no')
        tree.column('ID', anchor='center', width=200)
        tree.column('Student_Number',anchor='center', width=400)
        tree.column('Sleep_Time', anchor='center', width=450)
        # 列の見出し設定
        tree.heading('#0',text='')
        tree.heading('ID', text='ID',anchor='center')
        tree.heading('Student_Number', text='student_number', anchor='center')
        tree.heading('Sleep_Time',text='sleep_time', anchor='center')
        # レコードの追加
        
        judge = 0
        for v in data.values():
            for i in range(len(v)):
              # v[i] : i番目のタプル
                dte = datetime.datetime.strptime(v[i]['sleep_time'], '%Y-%m-%dT%H:%M:%S')
                num1 = dte.month
                num2 = dte.day
                num3 = dte.hour
                num4 = dte.minute
                num5 = dte.second
                s1 = f'{num1:02}'
                s2 = f'{num2:02}'
                s3 = f'{num3:02}'
                s4 = f'{num4:02}'
                s5 = f'{num5:02}'
                tree.insert(parent='', index='end', iid=i ,values=(i+1, v[i]['student_number'], str(dte.year)+'年'+str(s1)+'月'+str(s2)+'日 '+str(s3)+'時'+str(s4)+'分'+str(s5)+'秒'))        
                if i==9:
                    judge = 1
                    break
            if judge == 1:
                break
             
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