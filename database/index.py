import os
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()

connection = MongoClient(os.environ.get('MONGODB_URI'))

def get_commands_collection():
    collection = connection.cadastro.get_collection('commands')
    return collection

def get_infos_collection():
    collection = connection.cadastro.get_collection('computer_infos')
    return collection

def get_results_collection():
    collection = connection.cadastro.get_collection('results')
    return collection

def get_file_collection():
    collection = connection.cadastro.get_collection('files')
    return collection

def get_db():
    return connection.cadastro

def get_connection():
    return connection