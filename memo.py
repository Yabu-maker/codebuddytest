#!/usr/bin/env python3
"""简单命令行备忘录"""

import json
import os

FILE = "memos.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save(memos):
    with open(FILE, "w") as f:
        json.dump(memos, f, ensure_ascii=False, indent=2)

def add(text):
    memos = load()
    memos.append({"id": len(memos) + 1, "text": text})
    save(memos)
    print(f"已添加: {text}")

def list_all():
    memos = load()
    if not memos:
        print("暂无备忘录")
        return
    for m in memos:
        print(f"{m['id']}. {m['text']}")

def delete(mid):
    memos = load()
    memos = [m for m in memos if m["id"] != mid]
    save(memos)
    print(f"已删除 #{mid}")