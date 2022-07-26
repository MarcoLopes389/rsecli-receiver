from platform import *

from utils.get_ip import get_ip_util
from utils.get_username import get_username

def get_machine_info():
    m_version = version()
    m_platform = platform()
    m_machine = machine()
    m_processor = processor()
    m_release = release()
    m_system = system()

    return {
        'ip': get_ip_util(),
        'name': get_username(),
        'version': m_version,
        'platform': m_platform,
        'machine': m_machine,
        'processor': m_processor,
        'release': m_release,
        'system': m_system
    }
