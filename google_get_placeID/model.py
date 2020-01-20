from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://jerry:Ksd53890045@@localhost/travel?charset=utf8", pool_size=20, max_overflow=0)
Base = declarative_base()
# 創建單表
class googleApi(Base):
    __tablename__ = 'google_api'
    id = Column(Integer, primary_key=True,autoincrement=True)
    googlekey = Column(String(250))
    used = Column(Integer,comment='使用次數')
    limited=Column(Integer,comment='使用限制')
    status=Column(Boolean,comment='是否使用中',default=False)
    create_at=Column(DateTime,default=func.now(),comment='創建時間')
    modify_at=Column(DateTime,default=func.now(),onupdate=func.utc_timestamp(),comment='更新時間')

class googleData(Base):
    __tablename__ = 'google_data'
    id = Column(Integer, primary_key=True,autoincrement=True)
    lat=Column(Float)
    lon=Column(Float)
    icon=Column(String(250))
    google_id =Column(String(250),unique=True)
    name =Column(String(250))
    placeid =Column(String(250),unique=True)
    vicinity =Column(String(250))
    type =Column(String(250))
    price =Column(String(250))
    rating=Column(Float,comment='星星數')
    user_ratings_total =Column(Integer,comment='評論數')
    create_at=Column(DateTime,default=func.now(),comment='創建時間')
    modify_at=Column(DateTime,default=func.now(),onupdate=func.utc_timestamp(),comment='更新時間')



class shapeFileData(Base):
    __tablename__ = 'shape_file_data'
    id = Column(Integer, primary_key=True,autoincrement=True)
    area=Column(String(250))
    r  = Column(Float,comment='搜尋半徑要X10^5 m')
    sum_count_meth0=Column(Integer,comment='總爬巡次數方法0')
    sum_count_meth1=Column(Integer,comment='總爬巡次數方法1')
    now_count_meth0=Column(Integer,comment='目前爬巡次數方法0')
    now_count_meth1=Column(Integer,comment='目前爬巡次數方法1')
    google_count_meth0=Column(Integer,comment='使用GOOGLE爬巡次數方法0')
    google_count_meth1=Column(Integer,comment='使用GOOGLE爬巡次數方法1')
    create_at=Column(DateTime,default=func.now(),comment='創建時間')
    modify_at=Column(DateTime,default=func.now(),onupdate=func.utc_timestamp(),comment='更新時間')





def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)




