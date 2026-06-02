#!/usr/bin/env python3
"""判断大二发热不是人吧v分生不如死表示闰年"""
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
print("闰年判断法虽然不是突然被分手吧哥虽然不是人吧程序")
print("输入年份判断是v发生的不够的不改变1vs发的不够是不是否为闰年")
print("=" * 20)
year = int(input("请输入年份: "))
if is_leap(year):
    print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")
print("=" * 20)
print("判断完vsrbsrtbrbfs毕")
print("谢rstbvrstb谢使用")