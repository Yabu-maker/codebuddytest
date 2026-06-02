"""演示模块：导入 a 模块展示功能"""

from src.a import add, reverse, is_palindrome


def demo() -> None:
    """运行演示示例"""
    print(f"3 + 5 = {add(3, 5)}")
    print(f"reverse('hello') = {reverse('hello')}")
    print(f"is_palindrome('racecar') = {is_palindrome('racecar')}")
    print(f"is_palindrome('hello') = {is_palindrome('hello')}")


if __name__ == "__main__":
    demo()
