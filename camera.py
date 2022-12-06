import os,sys
import cv2
import json
import requests
import main
import time

def camera(self):
    
    url = "http://127.0.0.1:8000/Register_sleep" #データベースに送る用

    cap = cv2.VideoCapture(0)

    start_time = time.time()

    while True:
        
        #----------------------------------------------------------------------------------------------------
        
        #カスケードファイルを用意（眼鏡をかけていても検出される）
        cascade_file = "haarcascade_eye_tree_eyeglasses.xml"
        
        cascade = cv2.CascadeClassifier(cascade_file)
        
        #----------------------------------------------------------------------------------------------------
    
        #1フレームずつ取得する
        ret, frame = cap.read()
        
        #左右を反転する
        frame = cv2.flip(frame, 1)
        
        if not ret:
            break
        
        #画像を縮小
        frame = cv2.resize(frame, (500, 300))
        
        #グレイスケールに変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #目の認識を実行
        eyes_list = cascade.detectMultiScale(gray, minNeighbors=15)
        
        #----------------------------------------------------------------------------------------------------
        
        #目の部分を四角で囲む
        for (x,y,w,h) in eyes_list:
            
            red = (0,0,255)
            
            cv2.rectangle(frame, (x,y), (x+w,y+h),red, 1)
            
        #----------------------------------------------------------------------------------------------------
        
        #目を検出できなかった場合
        if len(eyes_list) == 0:
                
            end_time = time.time()
            
            print(end_time-start_time)
            
            #もし，3秒経過したら，
            if end_time - start_time >= 3:
            
                #「寝るな!」と表示
                cv2.putText(frame,"Don't Sleep!",(10,70),cv2.FONT_HERSHEY_PLAIN,1.5,(0,0,255),2,cv2.LINE_AA)
          
        #目を検出した場合
        elif len(eyes_list) > 0:

            end_time = time.time()
            
            #時間をもとに戻す
            start_time = end_time
            
        #----------------------------------------------------------------------------------------------------

        #結果を出力
        cv2.imshow("human_body_detect", frame)

        #もし，エンターが押されたら終了
        key = cv2.waitKey(1)
        if key == 13:
            break
        
    cap.release()
    
    cv2.destroyAllWindows()
