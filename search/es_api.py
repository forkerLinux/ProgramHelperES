#!/usr/bin/env python3
# coding:utf-

import json
from elasticsearch import Elasticsearch

es = Elasticsearch('127.0.0.1:9200')

def query_blog(title=None, offset=0, limit=20):
    match_list = []
    match_list.append({'match': {'title': {'query': title, 'operator': 'and'}}})

    query_dict = {
        'query': {
            'bool': {
                'must': match_list,
            }
        },
        'sort': [
            {'fetch_time': 'desc'},
        ],
        'from': offset,
        'size': limit
    }

    ret_query = es.search(index='programhelper', doc_type='blog', body=query_dict)
    ret = {
        'id_list': [item['_source']['id'] for item in ret_query['hits']['hits']],
        'blog_list': [item['_source'] for item in ret_query['hits']['hits']],
        'total': ret_query['hits']['total'],
    }
    return ret
