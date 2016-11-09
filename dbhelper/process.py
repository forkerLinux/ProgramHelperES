#!/usr/bin/env python3
# coding:utf-8

from configs import sp_session, ph_session
from models import CsdnModel, BlogModel
from helper import timestamp2datetime
from elasticsearch import Elasticsearch

es = Elasticsearch('127.0.0.1:9200')

# 转化爬虫数据
def handle_csdn():
    blog_list = sp_session.query(CsdnModel).all()
    for item in blog_list:
        blog = item.get_blog()
        fetch_time = timestamp2datetime(blog['fetch_time'])
        create_time = timestamp2datetime(blog['create_time'])

        blog_info = {
            'url': blog['url'],
            'title': blog['title'],
            'category': blog['category'],
            'subcategory': blog['subcategory'],
            'fetch_time': fetch_time,
            'create_time': create_time,
        }

        try:
            blog = BlogModel(**blog_info)
            ph_session.add(blog)
            ph_session.flush()
        except Exception as e:
            ph_session.rollback()
            print(e)
    ph_session.commit()

# 导入ES
def import_data():
    blog_list = ph_session.query(BlogModel).all()

    for item in blog_list:
        es.create(index='programhelper', doc_type='blog', id=item.id, body=item.to_json(), refresh=True)

if __name__ == '__main__':
    handle_csdn()
