# -*- coding: utf-8 -*-
import sys
import json
import traceback
from flask.views import MethodView
from flask import Blueprint, jsonify, request
from core.services.db_execution import DbExecutionService


bp_news = Blueprint('news', __name__, url_prefix='/api')
class News(MethodView):
    
    def __init__(self):
        self.db = DbExecutionService()


    def get(self, id=None):
        response = {
            'content': None,
            'message': None,
            'isValid': True,
            'error': None
        }
        
        try:
            if id is None:
                response['content'] = self.db.list(collection='news', search={})
            
            else:
                content = self.db.read(collection='news', id=id)
                if not content:
                    response['message'] = 'Não foi localizado nenhum registro com esse id.'
                    return jsonify(response), 404
                
                response['content'] = content
            
            return jsonify(response), 200
            
        except Exception:
            response['error'] = traceback.format_exc()
            response['isValid'] = False
            print(response, file=sys.stderr)
            return jsonify(response), 500


    def post(self):
        response = {
            'message': None,
            'isValid': True,
            'error': None
        }
        
        try:
            payload = request.get_json()
            if payload:
                payload['isActive'] = True
                self.db.create(collection='news', data=payload)
                response['message'] = 'Notícia salva com sucesso.'
                return jsonify(response), 200
            
        except Exception:
            response['error'] = traceback.format_exc()
            response['isValid'] = False
            print(response, file=sys.stderr)
            return jsonify(response), 500


    def put(self, id):
        response = {
            'message': None,
            'isValid': True,
            'error': None
        }
        
        try:
            if not id:
                response['message'] = 'id não localizado'
                return jsonify(response), 400
            
            content = self.db.read(collection='news', id=id)
            if not content:
                response['message'] = 'Não foi localizado nenhum registro com esse id.'
                return jsonify(response), 404
            
            payload = request.get_json()
            if payload:
                self.db.update(collection='news', id=id, data=payload)
                response['message'] = 'Notícia atualizada com sucesso.'
                return jsonify(response), 200
            
        except Exception:
            response['error'] = traceback.format_exc()
            response['isValid'] = False
            print(response, file=sys.stderr)
            return jsonify(response), 500
        
        
    def delete(self, id):
        response = {
            'message': None,
            'isValid': True,
            'error': None
        }
        
        try:
            if not id:
                response['message'] = 'id não localizado'
                return jsonify(response), 400
            
            content = self.db.read(collection='news', id=id)
            if not content:
                response['message'] = 'Não foi localizado nenhum registro com esse id.'
                return jsonify(response), 404
            
            self.db.update(collection='news', id=id, data={'isActive': True})
            response['message'] = 'Notícia excluída com sucesso.'
            return jsonify(response), 200
            
        except Exception:
            response['error'] = traceback.format_exc()
            response['isValid'] = False
            print(response, file=sys.stderr)
            return jsonify(response), 500


view = News.as_view('news')
bp_news.add_url_rule('/news', view_func=view, methods=['GET'])
bp_news.add_url_rule('/news/<id>', view_func=view, methods=['GET', 'PUT', 'DELETE'])
bp_news.add_url_rule('/news/create', view_func=view, methods=['POST'])
