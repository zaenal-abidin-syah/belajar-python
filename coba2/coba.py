from subprocess import run
from setting import *

# system('proxyman list')
# print(IP)
success = []
for ip in IP:
  # print(ip)
  ok = False
  try:
    run(f'v2ray tls ping {ip}', shell=True, timeout=2)
    ok = True
  except:
    print("handshake failed !!")
    
  if ok:
    success.append(ip)

print('ip handshake successfully')
for sc in success:
  print('ip = ', sc)
