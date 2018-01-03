#!/usr/bin/python
# -*- coding: utf-8 -*-
def my_abs(x):
    if not isinstance(x,(float,int)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x
        