# import requests
# from setting import *
from os import listdir
# import socket
from cloudflare import Cloudflare
# domain = 


class Main:
    def __init__(self, domains=None) -> None:
        self.domains = domains
        self.cloudflare = Cloudflare()
        self.res = []
    def check_domain(self):
        if self.domains:
            with open('./domain/'+self.domains) as f:
                data = f.read()
            sub = data.strip().split('\n')
            for host in sub:
                self.cloudflare.set_hostname(host)
                if self.cloudflare.run():
                    self.res.append(host)
            f.close()
        else:
            self.domains = [domain for domain in listdir('./domain')]
            for domain in self.domains:
                with open('./domain/'+domain) as f:
                    data = f.read()
                sub = data.strip().split('\n')
                f.close()
                for host in sub:
                    self.cloudflare.set_hostname(host)
                    if self.cloudflare.run():
                        self.res.append(host)
    def write(self):
        res = '\n'.join(self.res)
        # print(res)
        with open('./result/result.txt', 'w') as f:
            f.write(res)
            
    def run(self):
        self.check_domain()
        self.write()
        

if __name__ == "__main__":
    main = Main()
    main.run()