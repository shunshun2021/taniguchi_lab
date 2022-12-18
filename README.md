# taniguchi_lab
### 応用情報工学演習 (学部3年後期の授業のプロジェクト課題)

#### 居眠り防止アプリ
- 3秒以上目が閉じているのを検出するとアラートを出し、データベースに寝落ちした時間を記録。
- 居眠りログから、ユーザーの居眠りが多発している時間帯を抽出できる(教員の授業改善などに役立つ)。

#### 使い方
1. pip install fastapi uvicorn    &emsp; &emsp; &nbsp; # FastAPIのインストール(必要な人のみ)
2. python create_database.py      &emsp; &emsp;  # データベースの作成
3. uvicorn main:app --reload      &emsp; &emsp; # サーバーの起動 
4. python front.py                &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; # アプリの起動


##### 使用言語
- Python

##### フレームワーク等
- PyQt, OpenCV, FastAPI, SQLAlchemy


---------------------------------------------------------------------------------------------------------

#### Doze Prevention App
- If it detects eyes closed for more than 3 seconds, it alerts you and records the time you fell asleep in the database.
- Extract the times when users frequently doze off from the dozing logs (useful for teachers to improve their classes, etc.).
