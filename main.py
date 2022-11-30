from typing import Optional
from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime
import pandas as pd
import os
import math
import datetime

database_file = os.path.join(os.path.abspath(os.getcwd()), 'data.bd')

engine = create_engine('sqlite:///' + database_file, convert_unicode=True, echo=True)
#engine = create_engine('sqlite:///' + database_file, echo=True)

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

  def __init__(self, student_number=None, sleep_time=None):
    self.student_number = student_number
    self.sleep_time = sleep_time


def make_docs(db):
    all_data = {"data":[]}

    for row in db:
        data = {
            "id": 0,
            "student_number": None,
            "sleep_time": None,
        }
        data['id'] = row.id
        data['student_number'] = row.student_number
        data['sleep_time'] = row.sleep_time

        all_data['data'].append(data)
    
    return all_data


app = FastAPI()

# データベースのテーブルアイテムの全てのデータを確認する
@app.get("/all")
async def Refister_item():

    db = db_session.query(Sleep).all()

    all_data = make_docs(db)
    
    return  all_data


# 睡眠リストに追加
@app.post("/Register_sleep/")
async def Register_item():
#async def Register_item(student_number: int, shop_name: datetime):
    # 日時を取得.
    dt_now = datetime.datetime.now()
    student_number = 4620000
    sleep = Sleep(student_number=student_number,sleep_time=dt_now )
    db_session.add(sleep)
    db_session.commit()
    
    db = db_session.query(Sleep).all()
    all_data = make_docs(db)
    
    return all_data


# 居眠りリストの取得
@app.get("/sleep_list/")
async def item_by_store():
    db = db_session.query(Sleep).all()

    all_data = {"data":[]}

    for row in db:
        data = {
            "student_number": None,
            "sleep_time":None,
        }
        data['student_number'] = row.student_number
        data['sleep_time'] = row.sleep_time

        all_data['data'].append(data)

    return all_data
