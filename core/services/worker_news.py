# -*- coding: utf-8 -*-
from datetime import datetime
from core.services.db_execution import DbExecutionService


class WorkerNewsService():
    
    def __init__(self):
        self.db = DbExecutionService()


    def list(self):
        news = self.db.find(collection='news', param={'isActive': True})
        return {
            'statusCode': 200,
            'output': {
                'data': news,
                'qtd_registro': len(news),
                'error': None,
                'isValid': True
            }
        }
    
    
    def read(self, id):
        if not id:
            return {
                'statusCode': 400,
                'output': {
                    'data': [],
                    'error': 'I was expecting a id, but apparently on is missing',
                    'isValid': False
                }
            }
            
        news = self.db.find_one(collection='news', id=id, param={'isActive': True})
        if not news:
            return {
                'statusCode': 404,
                'output': {
                    'data': [],
                    'error': 'Id does not exist',
                    'isValid': False
                }
            }
            
        return {
            'statusCode': 200,
            'output': {
                'data': {
                    "_id": news['_id'],
                    "title": news['title'],
                    "content": news['content'],
                    "dt_publish": news['dt_publish']
                },
                'error': None,
                'isValid': True
            }
        }


    def create(self, payload):
        if not payload:
            return {
                'statusCode': 400,
                'output': {
                    'data': [],
                    'error': 'I was expecting a payload, but apparently on is missing',
                    'isValid': False
                }
            }
        
        payload['dt_publish'] = datetime.utcnow()
        payload['isActive'] = True
        self.db.insert_one(collection='news', data=payload)
        return {
            'statusCode': 200,
            'output': {
                'data': [],
                'message': 'News saved successfully',
                'error': None,
                'isValid': True
            }
        }


    def update(self, id, payload):
        if not id or not payload:
            return {
                'statusCode': 400,
                'output': {
                    'data': [],
                    'error': 'I was expecting a id and a payload, but apparently on (or both) is missing',
                    'isValid': False
                }
            }
        
        news = self.db.find_one(collection='news', id=id, param={'isActive': True})
        if not news:
            return {
                'statusCode': 404,
                'output': {
                    'data': [],
                    'error': 'Id does not exist',
                    'isValid': False
                }
            }
        
        self.db.update_one(collection='news', id=id, data=payload)
        return {
            'statusCode': 200,
            'output': {
                'data': [],
                'message': 'News updated successfully',
                'error': None,
                'isValid': True
            }
        }
    
        
    def delete(self, id):
        if not id:
            return {
                'statusCode': 400,
                'output': {
                    'data': [],
                    'error': 'I was expecting a id, but apparently on is missing',
                    'isValid': False
                }
            }
            
        news = self.db.find_one(collection='news', id=id, param={'isActive': True})
        if not news:
            return {
                'statusCode': 404,
                'output': {
                    'data': [],
                    'error': 'Id does not exist',
                    'isValid': False
                }
            }
        
        self.db.update_one(collection='news', id=id, data={'isActive': False})
        return {
            'statusCode': 200,
            'output': {
                'data': [],
                'message': 'News successfully deleted',
                'error': None,
                'isValid': True
            }
        }
