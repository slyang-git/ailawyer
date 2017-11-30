# -*- coding: utf-8 -*-

"""
Created by yangshuanglong at 17/11/30
"""
import logging
from logging import handlers
from os.path import dirname, abspath, exists

import os

from flask import Flask
from flask_restful import Api
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

ROOT_DIR = dirname(dirname(abspath(__file__)))
LOGFILE_DIR = ROOT_DIR + '/logs'
PROJECT_NAME = os.path.split(ROOT_DIR)[1]

if not exists(LOGFILE_DIR):
    os.mkdir(LOGFILE_DIR)


def init_log():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s-%(name)s-line %(lineno)d- [%(levelname)s]-%(message)s')
    console.setFormatter(formatter)

    logger.addHandler(console)

    handler = logging.handlers.TimedRotatingFileHandler('{0}/{1}-{2}'.format(LOGFILE_DIR, PROJECT_NAME, os.getpid()),
                                                        when='D', interval=1, backupCount=30, encoding='utf8')
    handler.suffix = "%Y%m%d.log"
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)


init_log()
app = Flask(__name__)
restful_api = Api(app)
app.secret_key = '34384n43229k3'
app.config.from_object('config')


engine = create_engine(SQLALCHEMY_DATABASE_URI, encoding='utf8', pool_size=15, pool_recycle=500) # echo_pool=True, echo=True)
# itopia_engine = create_engine(ITOPIA_SQLALCHEMY_DATABASE_URI, encoding='utf8', pool_size=15, pool_recycle=500) # echo_pool=True, echo=True)

# Session 工厂类
Session = scoped_session(sessionmaker(bind=engine))
# ItopiaSession = scoped_session(sessionmaker(bind=itopia_engine))

