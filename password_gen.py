import random
import string


def generate_password(length=12, use_special=True):
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def main():
    try:
        length = int(input("密码长度 (默认12): ") or 12)
        special = input("包含特殊字符? (y/n, 默认y): ").lower() != 'n'
        pwd = generate_password(length, special)
        print(f"生成的密码: {pwd}")
        print(f"强度: {'强' if length >= 12 else '中' if length >= 8 else '弱'}")
    except ValueError:
        print("请输入有效的数字！")


if __name__ == "__main__":
    main()
