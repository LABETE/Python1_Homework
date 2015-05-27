#!/usr/local/bin/python3
"""Porgram for practice functions"""

def my_func(a, b='b was not entered', c='c was not entered'):
    print('Value in a: {0}, value in b: {1} and value in c: {2}'.format(a, b, c))
    
my_func('test')
my_func('test','test')
my_func('test','test','test')
print(my_func)