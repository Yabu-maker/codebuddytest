import secrets
import string

_rng = secrets.SystemRandom()


def generate_password(length: int = 12, use_special: bool = True) -> str:
    pools = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    if use_special:
        pools.append(string.punctuation)
    # 保证每种字符至少出现一次，再随机填充至目标长度
    chars: list[str] = [secrets.choice(p) for p in pools]
    chars += [secrets.choice(''.join(pools)) for _ in range(length - len(pools))]
    _rng.shuffle(chars)
    return ''.join(chars)


def strength(password: str) -> str:
    score = sum([
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password),
        len(password) >= 8,
        len(password) >= 12,
    ])
    return ['极弱', '弱', '中', '中', '良', '强', '极强'][score]


def main():
    try:
        length = int(input("密码长度 (默认12): ") or 12)
        special = input("包含特殊字符? (y/n, 默认y): ").lower() != 'n'
        pwd = generate_password(length, special)
        print(f"生成的密码: {pwd}")
        print(f"强度: {strength(pwd)}")
    except ValueError:
        print("请输入有效的数字！")


if __name__ == "__main__":
    main()
