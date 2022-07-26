from threading import Thread
from database.index import get_file_collection

data = None

def get_file_solicitations():
    solicitations = get_file_collection().find()
    for solicitation in solicitations:
        try:
            Thread(target=read_file, args=(solicitation['path'],)).start()
            while data is None:
                pass
            get_file_collection().update_one({'_id': solicitation['_id']}, {'$set': {'file': data, 'status': 'done' }})
        except:
            pass

def read_file(path):
    global data
    binary_file = open(path, 'rb')
    data = binary_file.read()
    binary_file.close()
