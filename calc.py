import sys


def calc(expr):
    try:
        result = eval(expr, {"__builtins__": {}}, {})
        return result
    except Exception as e:
        return f"错误: {e}"


def main():
    print("简易计算器 (输入 'q' 退出)")
    history = []
    while True:
        expr = input(">>> ").strip()
        if expr.lower() in ('q', 'quit', 'exit'):
            break
        if not expr:
            continue
        result = calc(expr)
        print(f"= {result}")
        history.append(f"{expr} = {result}")
    if history:
        print("\n--- 历史记录 ---")
        for h in history:
            print(h)
def start_step():
        mng_id = OpenApiMngGameFunctionUtils.query_mng_by_name(self, settings.TCMPP_MNG_NAME)

        self.start_step("获取小游戏团队的GlobalTeamId")
        mini_team_id = OpenApiTeamFunctionUtils.get_team_id(self, settings.TCMPP_MINI_TEAM)

        self.start_step("获取应用团队的GlobalTeamId")
        team_id = OpenApiTeamFunctionUtils.get_team_id(self, settings.TCMPP_APP_TEAM)

        self.start_step("获取应用id")
        application_id = OpenApiAppFunctionUtils.get_application_id(self)

if __name__ == "__main__":
    main()
