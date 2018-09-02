#!/usr/bin/env python3

num = 150

if num >= 200:
    print('num >= 200')
elif num <= 100:
    print('num <= 100')
else:
    print('100 < num < 200')


non_zero_num = 4

if non_zero_num:
    print('non_zero_num =', non_zero_num)
if 0:
    print('zero')


non_empty_str = 'abc'

if non_empty_str:
    print('non_empty_str =', non_empty_str)
if '':
    print('empty str')


non_empty_list = ['a', 'b']

if non_empty_list:
    print('non_empty_list =', non_empty_list)
if []:
    print('empty list')


non_empty_tuple = ('a', 'b')

if non_empty_tuple:
    print('non_empty_tuple =', non_empty_tuple)
if ():
    print('empty tuple')


non_empty_set = {'a', 'b'}

if non_empty_set:
    print('non_empty_set =', non_empty_set)
if ():
    print('empty set')


def get_or_default(x, v):
    return x if x else v

print("get_or_default('abc', 'a') =", get_or_default('abc', 'a'))
print("get_or_default('', 'a') =", get_or_default('', 'a'))

