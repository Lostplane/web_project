# coding:utf-8
from . import api
from flask import current_app


@api.route("/calcotwo")
def index():
    current_app.logger.info("index page")
    return "index"
