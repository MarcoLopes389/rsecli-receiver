from requests import get

def get_ip_util():
    return get('https://api.ipify.org').text