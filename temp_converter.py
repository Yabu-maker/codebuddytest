#!/usr/bin/env python3
"""温度转换器"""
def c_to_f(c):
    return c * 9 / 5 + 32
def f_to_c(f):
    return (f - 32) * 5 / 9
print("温度转换器")
print("=" * 20)
print("1. 摄氏转华氏")
print("2. 华氏转摄氏")
