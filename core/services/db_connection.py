# -*- coding: utf-8 -*-
import os
from pymongo import MongoClient


class DbConnectionService:
    """ Serviço responsável por cria e fechar conexão com o database. """

    def __init__(self):
        self.__mongo_db = os.getenv('MONGO_DB', '')
        self.client = MongoClient(os.getenv('MONGO_URI', ''))
    
    def create_connection(self, collection):
        dbs = self.client.list_database_names()
        if not self.__mongo_db in dbs:
            raise Exception('Database does not exist.')
        
        db = self.client[self.__mongo_db]
        session = db[collection]
        return session
