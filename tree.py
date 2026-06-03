import os
import sys


def tree(dir_path, prefix=''):
    items = os.listdir(dir_path)
    for i, name in enumerate(items):
        path = os.path.join(dir_path, name)
        is_last = i == len(items) - 1
        connector = '└── ' if is_last else '├── '
        print(f'{prefix}{connector}{name}')
        if os.path.isdir(path):
            extension = '    ' if is_last else '│   '
            tree(path, prefix + extension)

def start_step():
        mng_id = OpenApiMngGameFunctionUtils.query_mng_by_name(self, settings.TCMPP_MNG_NAME)

        self.start_step("获取小游戏团队的GlobalTeamId")
        mini_team_id = OpenApiTeamFunctionUtils.get_team_id(self, settings.TCMPP_MINI_TEAM)

        self.start_step("获取应用团队的GlobalTeamId")
        team_id = OpenApiTeamFunctionUtils.get_team_id(self, settings.TCMPP_APP_TEAM)

        self.start_step("获取应用id")
        application_id = OpenApiAppFunctionUtils.get_application_id(self)
if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(target)
    tree(target)
