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


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(target)
    tree(target)
