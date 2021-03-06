#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : 陈坤泽
# @Email  : 877362867@qq.com
# @Data   : 2020/05/30 11:34

# 如何把自己的开源项目发布到Pypi服务器：https://mp.weixin.qq.com/s/O4rKq8XJK-MHHy3EDJ3NLg
# 上传项目： python setup.py register sdist bdist_egg upload

from setuptools import setup, find_packages
import io

VERSION = '0.0.4'

with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

install_requires = open("requirements.txt").readlines()

setup(
    name="pyxllib",  # pip 安装时用的名字
    version=VERSION,  # 当前版本，每次更新上传到pypi都需要修改
    author="code4101",
    author_email="877362867@qq.com",
    url="https://github.com/XLPRUtils/pyxllib",
    keyworads="pyxllib",
    description="厦门理工模式识别团队通用python代码工具库",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=('tests', 'tests.*', '*account.pkl')),
    include_package_data=True,
    license='Apache License',
    classifiers=[],
    install_requires=install_requires,
)
