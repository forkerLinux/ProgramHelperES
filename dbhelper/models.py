#!/usr/bin/env python3
# coding:utf-8

from datetime import datetime
from sqlalchemy import Column, BIGINT, INT, DateTime, TEXT, \
    Integer, Boolean, Index, String, BLOB, TIMESTAMP
from sqlalchemy.dialects.mysql import LONGTEXT
from configs import Model
import json


class CsdnModel(Model):

    __tablename__ = 'csdn6'

    taskid = Column(String(64), primary_key=True)
    url = Column(String(1024))
    result = Column(BLOB)
    updatetime = Column(TIMESTAMP)

    def get_blog(self):
        blog = self.result.decode('utf-8')
        return json.loads(blog)


class BlogModel(Model):

    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    url = Column(String(255), unique=True)
    title = Column(String(255))
    category = Column(String(255))
    subcategory = Column(String(255))
    fetch_time = Column(DateTime)
    create_time = Column(DateTime)

    def to_json(self):
        ret_dict = {}
        for k in self.__table__.columns:
            ret_dict[k.name] = getattr(self, k.name)
        return ret_dict
