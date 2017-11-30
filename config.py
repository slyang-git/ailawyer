# -*- coding: utf-8 -*-

"""
Created by yangshuanglong at 17/11/30
"""


# DEBUG = False
DEBUG = True

RUN_IN_NON_PRODUCTION = DEBUG


if DEBUG:  # 测试环境
    DB_HOST = ''
    DB_USERNAME = ''
    DB_PASSWORD = ''
    DB_NAME = ''

else:  # 生产环境
    DB_HOST = ''
    DB_USERNAME = ''
    DB_PASSWORD = ''
    DB_NAME = ''


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8mb4&use_unicode=1'.format(DB_USERNAME,
                                                                                              DB_PASSWORD,
                                                                                              DB_HOST,
                                                                                              DB_NAME)
