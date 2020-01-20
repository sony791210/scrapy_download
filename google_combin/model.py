from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://jerry:Ksd53890045@@localhost/travel?charset=utf8", pool_size=20, max_overflow=0)i
Base = declarative_base()



class google(Base):
    __tablename__='google'
    id=Column(Integer, primary_key=True,autoincrement=True)
    icon=Column(String(200),nullable=True,comment='圖標')
    lon=Column(Float,nullable=True,comment='經度')
    lat=Column(Float,nullable=True,comment='緯度')
    name=Column(String(100),comment='店名')
    placeid=Column(String(100),nullable=False,unique=True,comment='goole查詢用')
    rating=Column(Float,nullable=True,comment='評分')
    review=Column(Float,nullable=True,comment='回復數量')
    price=Column(String(100),nullable=True,comment='價位')
    url=Column(String(1024),nullable=True,comment='網址')
    types=Column(String(1024),comment='屬性英文')
    phone=Column(String(100),nullable=True,comment='電話')
    vicinity=Column(String(1024),nullable=True,comment='地址')
    googletype=Column(String(100),nullable=True,comment='屬性中文')
    imageUrl=Column(String(1024),nullable=True,comment='圖片網址')
    webUrl=Column(String(1024),nullable=True,comment='相關網址')
    area=Column(String(100),nullable=True,comment='地區')
    city=Column(String(100),nullable=True,comment='城市')
    opentime=Column(String(1024),nullable=True,comment='營業時間')
    fbcount=Column(Integer,nullable=True,comment='FB的外鍵')
    tripcount=Column(Integer,nullable=True,comment='trip的外鍵')
    create_at=Column(DateTime,default=func.now(),comment='創建時間')
    modify_at=Column(DateTime,default=func.now(),onupdate=func.utc_timestamp(),comment='更新時間')

class fb(Base):
    __tablename__='fb'
    id=Column(Integer, primary_key=True,autoincrement=True)
    name=Column(String(100),comment='店名')
    rating=Column(Float,nullable=True,nullable=True,comment='評分')
    review=Column(Float,nullable=True,nullable=True,comment='回復數量')
    price=Column(String(100),nullable=True,comment='價位')
    types=Column(String(1024),comment='屬性英文')
    checkin=Column(Float,nullable=True)
    follow=Column(Float,nullable=True)
    likes=Column(Float,nullable=True)
    recommend=Column(Float,nullable=True)
    phone=Column(String(100),nullable=True,comment='電話')
    vicinity=Column(String(1024),nullable=True,comment='地址')
    placeid=Column(String(100),nullable=False,unique=True,comment='goole查詢用')
    googlepk=Column(Integer,nullable=True)
    area=Column(String(100),nullable=True,comment='地區')
    city=Column(String(100),nullable=True,comment='城市')
    create_at=Column(DateTime,default=func.now(),comment='創建時間')
    modify_at=Column(DateTime,default=func.now(),onupdate=func.utc_timestamp(),comment='更新時間')


class trip(Base):
    __tablename__='trip'
    id=Column(Integer, primary_key=True,autoincrement=True)
    name=Column(String(100),comment='店名')
    img=Column(String(200),nullable=True,comment='圖片網址')
    lon=Column(Float,comment='經度')
    lat=Column(Float,comment='緯度')
    rating=Column(Float,nullable=True,comment='評分')
    review=Column(Float,nullable=True,comment='回復數量')
    price=Column(String(100),nullable=True,comment='價位')
    url=Column(String(1024),nullable=False,unique=True,comment='價位')
    types=Column(String(1024),comment='屬性英文')
    vicinity=Column(String(1024),nullable=True,comment='地址')
    web=Column(String(1024),nullable=True,comment='網址')
    orderdetail=Column(String(1024),nullable=True,comment='點餐')
    other=Column(String(1024),nullable=True,comment='其他')
    servies=Column(String(1024),nullable=True,comment='服務')
    phone=Column(String(100),nullable=True,comment='電話')
    googlepk=Column(Integer,nullable=True)
    area=Column(String(100),nullable=True,comment='地區')
    city=Column(String(100),nullable=True,comment='城市')
    create_at=Column(DateTime,default=func.now(),comment='創建時間')
    modify_at=Column(DateTime,default=func.now(),onupdate=func.utc_timestamp(),comment='更新時間')













def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)




