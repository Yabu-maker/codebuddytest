#!/usr/bin/env python3
"""猜数字游戏"""
import random
target = random.randint(1, 100)
print("猜数字游戏（1-100）")
print("猜数字游戏开始")
print("=" * 20)
while True:
    try:
        guess = int(input("请输入你猜的数字: "))
    except ValueError:
        print("请输入有效数字")
        continue
    if guess < target:
        print("猜小了")
    elif guess > target:
        print("猜大了")
    else:
        print(f"恭喜你！猜对了，数字是 {target}")
        break
print("游戏结束")