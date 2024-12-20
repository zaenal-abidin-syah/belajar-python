# import socket
import requests
class Ip_generator:
    def __init__(self, baseip) -> None:
        self.base = baseip
    def run(self):
        # for a in range(1, 255):
        for b in range(1, 60):
            # print(f'{baseip}.1.{b}')
            self.check(f'{baseip}.225.{b}')
        # try:
        #     for b in range(1, 60):
        #         # print(f'{baseip}.1.{b}')
        #         self.check(f'{baseip}.225.{b}')
        # except:
        #     pass
    def check(self, ip):
        response = requests.get("http://"+ip, proxies=None)
        print(response.headers)
        # print(response.ok)
        # if response.content:
        #     print('true : ',ip)
        # return response.headers.items()
        # return response.headers.get('Server', '').lower() == 'cloudflare'

baseip = "104.18"

ip_gen = Ip_generator(baseip)
ip_gen.run()

# ip = '104.18.4.6'
# response = requests.get("http://"+ip)
# print(response.headers.items())