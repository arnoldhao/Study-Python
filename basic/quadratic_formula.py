#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
#    if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
#       raise TypeError('Pleae type right int or float')
    if a == 0:
        return ('相同，非二元一次方程式')
    else:
        r = b*b - 4*a*c
        if r < 0:
            return ('复数')
        else:
            x1 = (-b + math.sqrt(r))/(2*a)
            x2 = (-b - math.sqrt(r))/(2*a)
            return x1,x2
a = float(input('请输入系数a:'))
b = float(input('请输入系数b:'))
c = float(input('请输入系数c:'))
print('%dx^2+%dx+%d=0的解为%s'%(a,b,c,quadratic(a,b,c)))