from pip.req import parse_requirements


with open(‘requirements.txt’) as f:
install_requires = f.read().strip().split(’\n’)
