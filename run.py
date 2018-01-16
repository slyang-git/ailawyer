# -*- coding: utf-8 -*-

"""
Created by yangshuanglong at 17/11/30
"""
from flask import jsonify

from ailawyer import app


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'404': 'Not Found'}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'405': 'Method Not Allowed'}), 405


@app.errorhandler(500)
def server_error(e):
    return jsonify({'500': 'Server Error'}), 500


if __name__ == '__main__':
    app.run('0.0.0.0', port=5050, debug=True)