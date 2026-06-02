"""工具模块：数学与字符串工具函数"""


def add(a: int | float, b: int | float) -> int | float:
    """返回两数之和"""
    return a + b


def reverse(s: str) -> str:
    """反转字符串"""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """判断字符串是否为回文"""
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
