# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()
app = Flask(__name__)
CORS(app)
started_date = datetime.now()

# config secret keys
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '')
app.secret_key = app.config['SECRET_KEY']

# import controllers
from core.controllers.status import bp_status
app.register_blueprint(bp_status)

from core.controllers.news import bp_news
app.register_blueprint(bp_news)
