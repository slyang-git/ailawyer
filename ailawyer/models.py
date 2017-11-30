# -*- coding: utf-8 -*-

"""
Created by yangshuanglong at 17/11/30
"""
from ailawyer import db


class Lawyer(db.Model):
    __tablename__ = 'lawyers'
    __table_args__ = {'autoload': True}