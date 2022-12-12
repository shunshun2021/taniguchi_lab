# データベースの定義, 初期化
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime
import pandas as pd
import os
import datetime

database_file = os.path.join(os.path.abspath(os.getcwd()), 'data.bd')

engine = create_engine('sqlite:///' + database_file, convert_unicode=True, echo=True)

db_session = scoped_session(
    sessionmaker(
      autocommit = False,
      autoflush = False,
      bind = engine
    )
)

Base = declarative_base()
Base.query = db_session.query_property()

class Sleep(Base):
  #テーブルの名前
  __tablename__ = 'sleep_table'
  #columnの作成
  id = Column(Integer, primary_key=True)
  student_number = Column(Integer, unique = False)
  sleep_time = Column(DateTime, unique = False)


  def __init__(self, student_number=None, sleep_time=None, ):
    self.student_number = student_number
    self.sleep_time = sleep_time


Base.metadata.create_all(bind=engine)

#テンプレートの作成
item = Sleep(student_number=4620000,sleep_time=datetime.datetime(2022,12,13,11,10))
db_session.add(item)
item = Sleep(student_number=4620999,sleep_time=datetime.datetime(2022,12,13,11,15))
db_session.add(item)
item = Sleep(student_number=4620999,sleep_time=datetime.datetime(2022,12,13,11,18))
db_session.add(item)
db_session.commit()
