from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Model = declarative_base()
spider_engine = create_engine('mysql+pymysql://root:123456@localhost/resultdb?charset=utf8')
ph_engine = create_engine('mysql+pymysql://root:123456@localhost/programhelper?charset=utf8')

sp = sessionmaker(bind=spider_engine)
sp_session = sp()

ph = sessionmaker(bind=ph_engine)
ph_session = ph()

if __name__ == '__main__':
    from models import *
    Model.metadata.create_all(ph_engine)
    print('db init finish')
