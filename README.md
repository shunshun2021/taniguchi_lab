# taniguchi_lab
### 応用情報工学演習 (学部3年後期の授業のプロジェクト課題)

#### 居眠り防止アプリ
- 3秒以上目が閉じているのを検出するとアラートを出し、データベースに寝落ちした時間を記録。
- 居眠りログから、ユーザーの居眠りが多発している時間帯を抽出できる(教員の授業改善などに役立つ)。


##### 使用言語
- Python

##### フレームワーク等
- PyQt, OpenCV, FastAPI, SQLAlchemy


---------------------------------------------------------------------------------------------------------

#### Doze Prevention App
- If it detects eyes closed for more than 3 seconds, it alerts you and records the time you fell asleep in the database.
- Extract the times when users frequently doze off from the dozing logs (useful for teachers to improve their classes, etc.).
