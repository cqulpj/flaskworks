#coding=utf-8

from watchlist import db, app
from flask import Flask, render_template

@app.errorhandler(404)          # ����Ҫ����Ĵ������
def page_not_found(e):          # �����쳣������Ϊ����
    return render_template('404.html'), 404

