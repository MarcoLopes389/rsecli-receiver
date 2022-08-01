from pymongo.errors import PyMongoError

from database.index import get_connection
from scripts.exec_commands import exec_commands
from scripts.get_file_silicitations import get_file_solicitations
from scripts.send_information import send_information

while True:
    try:
        send_information()
        exec_commands()
        get_file_solicitations()
    except KeyboardInterrupt:
        get_connection().close()
        break
    except PyMongoError:
        print('MongoDB error')
        break
