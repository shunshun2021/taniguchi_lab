import os,sys
import cv2
import json
import requests
import main
import time

def camera(self):

    url = "http://127.0.0.1:8000/Register_sleep" #データベースに送る用
    

    cap = cv2.VideoCapture(0) #カメラ起動
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

    #始まりの時間を指定
    start_time = time.time()

    while True:
        ret, rgb = cap.read()

        gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY) #グレースケールに変換
        faces = cascade.detectMultiScale(
            gray, scaleFactor=1.11, minNeighbors=3, minSize=(100, 100))
        
        #顔認証する場合
        if len(faces) == 1: 
            x, y, w, h = faces[0, :]
            cv2.rectangle(rgb, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # 処理高速化のために顔の上半分を検出対象範囲とする
            eyes_gray = gray[y : y + int(h/2), x : x + w]

            #目の認識を実行
            eyes = eye_cascade.detectMultiScale(
                eyes_gray, scaleFactor=1.11, minNeighbors=3, minSize=(8, 8))

            for ex, ey, ew, eh in eyes:
                cv2.rectangle(rgb, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (255, 255, 0), 1)
            
            #目が検知できない場合
            if len(eyes) == 0:

                end_time = time.time()

                #3秒以上目を閉じていた場合
                if end_time - start_time >= 3:

                    #「寝るな」と表示
                    cv2.putText(rgb,"Sleepy eyes. Wake up!",
                        (10,100), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 2, cv2.LINE_AA)

                    r = requests.post(url) #データベースに送る

            #目が検知できた場合
            elif len(eyes) > 0:

                #時間をもとに戻す
                start_time = end_time


        #結果を出力
        cv2.imshow('frame', rgb)

        #エンターが押されたら終了
        if cv2.waitKey(1) == 27:
            break  # esc to quit

    cap.release()
    cv2.destroyAllWindows()