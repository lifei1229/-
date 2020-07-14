# -*- coding=utf-8 -*-
import time

def calculate_time(f):
    def inner(*args,**kwargs):
        startTime = time.time()
        result = f(*args,**kwargs)
        endTime = time.time()
        print(endTime - startTime)
        return result
    return inner

@calculate_time
def index():
    time.sleep(2)
    return 'index'

@calculate_time
def add(x,y):
    time.sleep(2)
    return x + y

res = index()
addRes = add(1,2)
print(res,addRes)