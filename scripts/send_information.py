from database.index import get_infos_collection
from utils.get_ip import get_ip_util
from utils.get_machine_info import get_machine_info
from utils.get_username import get_username

collection = get_infos_collection()

def send_information():
    register = collection.find_one({'ip': get_ip_util(), 'name': get_username()})

    if register is None:
        new_register = collection.insert_one(get_machine_info())
        return new_register
    
    return register