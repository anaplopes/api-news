# -*- coding: utf-8 -*-
from datetime import datetime
from bson.objectid import ObjectId
from core.services.db_connection import DbConnectionService


class DbExecutionService:
    """ Serviço responsável por executar comandos no db. """
    
    def __init__(self):
        self.db = DbConnectionService()
    
    
    def __convert_data(self, row):
        for i in row:
            if isinstance(row[i], ObjectId):
                row[i] = str(row[i])
                
            if isinstance(row[i], datetime):
                row[i] = row[i].strftime("%Y-%m-%dT%H:%M:%S.%f%z")
                
        return row
    
    
    def find(self, collection, param={}, sort=None, sequence=1):
        if not isinstance(param, dict):
            raise TypeError('param must be a object')
        
        session = self.db.create_connection(collection)
        if sort:
            return list(map(self.__convert_data, session.find(param).sort(sort, sequence)))
        # return list(map(lambda row: {i: str(row[i]) if isinstance(row[i], ObjectId) else row[i] for i in row}, session.find(param)))
        return list(map(self.__convert_data, session.find(param))) 
    
    
    def insert_one(self, collection, data):
        if not isinstance(data, dict):
            raise TypeError('data must be a object.')
            
        session = self.db.create_connection(collection)
        return session.insert_one(data)
    
    
    def find_one(self, collection, id, param=None):
        session = self.db.create_connection(collection)
        search = {'_id': ObjectId(id)}
        if param:
            search.update(param)
        
        result = session.find_one(search)
        if not result:
            return result
        return self.__convert_data(result)
    
    
    def update_one(self, collection, id, data):
        if not isinstance(data, dict):
            raise TypeError('data must be a object')
        
        session = self.db.create_connection(collection)
        return session.update_one({'_id': ObjectId(id)}, { "$set": data })
    
    
    def delete(self, collection, id):
        session = self.db.create_connection(collection)
        return session.delete_one({'_id': ObjectId(id)})
