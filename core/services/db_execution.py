from bson import ObjectId
from core.services.db_connection import DbConnectionService


class DbExecutionService:
    """ Serviço responsável por executar comandos no db. """
    
    def __init__(self):
        self.db = DbConnectionService()
    
    
    def __map(self, row):
        row['_id'] = str(row['_id'])
        return row
    
    
    def list(self, collection, search, sort=None, sequence=1):
        if not isinstance(search, dict):
            raise TypeError('search must be a object')
        
        session = self.db.create_connection(collection)
        if sort:
            return list(map(self.__map, session.find(search).sort(sort, sequence)))
        return list(map(self.__map, session.find(search)))
    
    
    def create(self, collection, data):
        if not isinstance(data, dict):
            raise TypeError('data must be a object.')
            
        session = self.db.create_connection(collection)
        return session.insert_one(data)
    
    
    def read(self, collection, id):
        if not isinstance(id, str):
            raise TypeError('id must be a string')
        
        session = self.db.create_connection(collection)
        return session.find_one({'_id': ObjectId(id)})
    
    
    def update(self, collection, id, data):
        if not isinstance(id, str):
            raise TypeError('id must be a string')
        
        if not isinstance(data, dict):
            raise TypeError('data must be a object')
        
        session = self.db.create_connection(collection)
        return session.update_one({'_id': ObjectId(id)}, { "$set": data })
    
    
    def delete(self, collection, id):
        if not isinstance(id, str):
            raise TypeError('id must be a string')
        
        session = self.db.create_connection(collection)
        return session.delete_one({'_id': ObjectId(id)})
