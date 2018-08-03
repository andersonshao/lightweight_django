import os


def check_dependencies(package_name):
    with os.popen('pip show %s' % package_name) as p:
        lines = p.readlines()
        if not len(lines):
            return None
        dependencies = lines[-2].split(':')[-1].strip()
        if dependencies:
            dependencies = dependencies.split(',')
        else:
            dependencies = None
        return dependencies


def remove_package(package_name):
    dependencies = check_dependencies(package_name)
    if dependencies:
        for dependency in dependencies:
            remove_package(dependency)
    os.system('pip uninstall -y %s' % package_name)


if __name__ == '__main__':
    package_name = input('请输入需要删除的包：')
    remove_package(package_name)
