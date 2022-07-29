from threading import Thread
from database.index import get_file_collection

def get_file_solicitations():
    solicitations = get_file_collection().find()
    for solicitation in solicitations:
        try:
            read_file(solicitation)  
        except Exception as e:
            print(e)
            pass

def read_file(solicitation):
    binary_file = open(solicitation['path'], 'rb')
    data = binary_file.read()
    get_file_collection().update_one({'_id': solicitation['_id']}, {'$set': {'file': data, 'status': 'done' }})
    binary_file.close()
