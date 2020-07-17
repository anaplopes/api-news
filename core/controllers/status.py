# -*- coding: utf-8 -*-
import json
from core.app import started_date
from datetime import datetime
from flask import Blueprint, jsonify
from flask.views import MethodView


bp_status = Blueprint('status', __name__, url_prefix='/')
class Live(MethodView):

    def get(self):
        with open('news/package.json', 'r') as json_file:
            file = json.load(json_file)
        
            payload = {
                'name': file['name'],
                'version': file['version'],
                'started': started_date,
                'uptime': str(datetime.now() - started_date)
            }
            return jsonify(payload), 200


view = Live.as_view('status')
bp_status.add_url_rule('/', view_func=view, methods=['GET'])
