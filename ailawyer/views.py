# -*- coding: utf-8 -*-

"""
Created by yangshuanglong at 17/11/30
"""

from flask import jsonify, request, render_template
import json
import logging

from ailawyer import app, services

logger = logging.getLogger(__name__)


@app.route('/v1/realname', methods=['POST'])
def realname():
    """实名认证"""
    data = request.get_json(force=True)
    logger.info('实名认证请求数据: %s', json.dumps(data))
    name = data.get('name')
    idcard = data.get('idcard')
    result = services.realname(name, idcard)

    rv = {
        'name': name,
        'idcard': idcard,
        'result': result
    }
    logger.info('实名认证接口返回数据：%s', json.dumps(rv))
    return jsonify(rv)


@app.route('/test')
def test():
    return render_template('test.html',
                           seq=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                           username='<dfdsfdsf&')
