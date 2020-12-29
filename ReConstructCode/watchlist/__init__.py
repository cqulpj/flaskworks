#coding=utf-8

import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

WIN = sys.platform.startswith('win')
if WIN:  # ����� Windows ϵͳ��ʹ������б��
    prefix = 'sqlite:///'
else:  # ����ʹ���ĸ�б��
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # �رն�ģ���޸ĵļ��
app.config['SECRET_KEY'] = 'dev'
# ����չ��ʵ����ǰ��������
db = SQLAlchemy(app)
# ʵ������չ��
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
# �����û����ػص������������û�ID��Ϊ����
def load_user(user_id):
    from watchlist.models import User
    user = User.query.get(int(user_id))
    return user

@app.context_processor          # ע��ģ�������Ĵ�����
def inject_user():              # ��������������
    from watchlist.models import User
    users = User.query.all()
    return dict(user=users[-1]) # ��Ҫ�����ֵ䣬��ͬ��{'user': user}

from watchlist import views, errors, commands

