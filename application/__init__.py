# coding:utf-8
from flask_session import Session
from flask_wtf import CSRFProtect
from flask import Flask
from config import config_map, Config
from application import api_v1_0
from logging.handlers import RotatingFileHandler

import redis
import logging

# connect redis
redis_store = None

# 配置日志文件的位置
logging.basicConfig(level=logging.DEBUG)
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=0)
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
file_log_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_log_handler)


# 在生产app时候建议使用工厂模式
def create_app(model):
    """
    根据开发模式 创建app
    :param model: （str) 开发模式“develop”  生产模式”product“
    :return: flask的应用对象
    """
    app = Flask(__name__)
    app.config.from_object(config_map.get(model))
    Session(app)
    # 为flask 添加csrf的攻击保护
    global redis_store
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
    CSRFProtect(app)
    # 注册蓝图
    app.register_blueprint(api_v1_0.api, url_prefix="/api")
    return app
