from database.index import get_file_collection

def get_file_solicitations():
    solicitations = get_file_collection().find()
    for solicitation in solicitations:
        try:
            if solicitation['edit'] == True:
                read_file(solicitation, binary=False)
                while True:
                    solicitation = get_file_collection().find_one({'_id': solicitation['_id']})
                    if solicitation['ready'] == True:
                        open(solicitation['path'], 'w').write(solicitation['file'])
                        get_file_collection().delete_one({'_id': solicitation['_id']})
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

