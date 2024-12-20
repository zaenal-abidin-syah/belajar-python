import requests
from setting import *
from os import listdir
import socket


class Cloudflare:
    def __init__(self):
        self.ip = ''
        self.hostname = ''
    def host_to_ip(self):
        self.ip = socket.gethostbyname(self.hostname)
    def set_hostname(self, hostname):
        self.hostname = hostname
    def check(self):
        response = requests.get("http://"+self.ip)
        # print(response.headers.get('Server', ''))
        return response.headers.get('Server', '').lower() == 'cloudflare'
    def run(self):
        try:
            self.host_to_ip()
            return self.check()
        except:
            return False