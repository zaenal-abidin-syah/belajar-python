import requests
from setting import *
from os import listdir
import socket


class Playground:
    def __init__(self, hostname):
        self.ip = ''
        self.hostname = hostname
    def host_to_ip(self):
        self.ip = socket.gethostbyname(self.hostname)
    def check(self):
        response = requests.get("http://"+self.ip)
        print(response.headers.get('Server', ''))
    def run(self):
        self.host_to_ip()
        self.check()

if __name__ == "__main__":
    play = Playground('app.ruangguru.com')
    play.run()