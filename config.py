# coding:utf-8
import redis


class Config(object):
    DEBUG = True
    SECRET_KEY = "dsh121dha##lqwke**"
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # flask-session 配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 3600


class DevelopmentConfig(Config):
    """开发模式配置信息"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置信息"""
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}
