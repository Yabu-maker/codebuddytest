# 简单计算器
print("简简单单的计算器")

a = float(input("请输入第一个数: "))
print(f"已输入: {a}")
op = input("请输入运算符 (+, -, *, /): ")
print(f"运算符: {op}")
b = float(input("请输入第二个数: "))

if op == "+":
    print(f"结果: {a + b}")
elif op == "-":
    print(f"结果: {a - b}")
elif op == "*":
    print(f"结果: {a * b}")
elif op == "/":
    print(f"结果: {a / b}" if b != 0 else "除数不能为0")
elif op == "%":
    print(f'我的结果是{a // b}')
else:
    print("不支持的运算符")
