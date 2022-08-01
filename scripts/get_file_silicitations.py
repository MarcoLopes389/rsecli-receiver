from database.index import get_file_collection

files = get_file_collection()

def get_file_solicitations():
    solicitations = files.find()
    for solicitation in solicitations:
        try:
            if solicitation['edit'] == True:
                read_file(solicitation, binary=False)
                while True:
                    solicitation = files.find_one({'_id': solicitation['_id']})
                    if solicitation['ready'] == True:
                        open(solicitation['path'], 'w').write(solicitation['file'])
                        files.update_one({'_id': solicitation['_id']}, {'$set': {'done': True}})
                        print('File updated')
                        break
            else: 
                read_file(solicitation)
        except Exception as e:
            print(e)
            pass

def read_file(solicitation, binary=True):
    binary_file = open(solicitation['path'], 'rb' if binary else 'r')
    data = binary_file.read()
    get_file_collection().update_one({'_id': solicitation['_id']}, {'$set': {'file': data, 'status': 'done' }})
    binary_file.close()
    print('File sent')

