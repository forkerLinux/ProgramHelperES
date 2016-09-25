#!/usr/bin/env python3

import datetime


def timestamp2datetime(timestamp, convert_to_local=True):
    if isinstance(timestamp, (int, float)):
        dt = datetime.datetime.utcfromtimestamp(timestamp)
    if convert_to_local: # 是否转化为本地时间
        dt = dt + datetime.timedelta(hours=8) # 中国默认时区
        return dt
    return timestamp

if __name__ == '__main__':
    ret = timestamp2datetime(1474806335)
    print(ret)
