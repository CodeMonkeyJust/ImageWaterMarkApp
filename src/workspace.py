# encoding= utf-8
# ------------------------------------------------------------------
# Author:zhulijun
# Created:2021-09-09
# Description:初始化用户空间
# ------------------------------------------------------------------
import os
import time
import path_unit
from config_unit import get_config


def init_file():
    # 配置
    path_unit.path_create(get_workspace_path())
    path_unit.path_create(get_config_path())
    try:
        f = open(get_config_filename(), 'r')
        f.close()
    except IOError:
        f = open(get_config_filename(), 'w')
        f.close()
    # 日志
    path_unit.path_create(get_log_path())


def get_workspace_path():
    return os.path.join(os.path.expanduser('~'), 'watermark')


def get_config_path():
    return os.path.join(get_workspace_path(), 'conf')


def get_config_filename():
    return os.path.join(get_config_path(), 'watermark.ini')


def get_log_path():
    return os.path.join(get_workspace_path(), 'log')


def get_log_filename():
    return os.path.join(get_log_path(), time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log')
