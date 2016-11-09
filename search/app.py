#!/usr/bin/env python3
# coding:utf-8

import json
from flask import Flask, request

from es_api import query_blog

app = Flask(__name__)


@app.route('/', methods=['GET', ])
def index():
    return 'hello world'


@app.route('/blog', methods=['POST', ])
def get_blog():
    post_data = request.get_json()
    query_keys = set(post_data.keys())
    allow_keys = set({'title', 'limit', 'offset'})
    if query_keys != allow_keys:
        ret = {
            'errcode': 1,
            'errmsg': 'params invalid',
            'data': '',
        }
        return json.dumps(ret)
    ret_query = query_blog_helper(**post_data)
    return json.dumps(ret_query)


def query_blog_helper(*args, **kwargs):
    return query_blog(*args, **kwargs)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
