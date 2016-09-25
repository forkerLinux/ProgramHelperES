#!/usr/bin/env python3
# coding:utf-8

from configs import sp_session, ph_session
from models import CsdnModel, BlogModel
from helper import timestamp2datetime


def handle_csdn():
    blog_list = sp_session.query(CsdnModel).all()
    for item in blog_list:
        blog = item.get_blog()
        fetch_time = timestamp2datetime(blog['fetch_time'])
        create_time = timestamp2datetime(blog['create_time'])

        blog_info = {
            'url': blog['url'],
            'title': blog['title'],
            'tags': ','.join(blog['tags']),
            'category': blog['category'],
            'subcategory': blog['subcategory'],
            'content': blog['content'],
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

if __name__ == '__main__':
    handle_csdn()
