import base64
import json

def json_to_vmess(vmess_data):
    

    vmess_string = json.dumps(vmess_data)
    encoded_vmess = base64.b64encode(vmess_string.encode()).decode()
    
    return f"vmess://{encoded_vmess}"

def vmess_to_json(vmess_url):
    decoded_vmess = base64.b64decode(vmess_url.replace("vmess://", "")).decode()
    vmess_data = json.loads(decoded_vmess)

    return vmess_data

def edit(vmess):
    
  vmess_data = vmess_to_json(vmess_url)

  
  new_vmess = {}
  for part in  vmess_data:
    # print(part, ' type = ', type(part))
    if part == "id" or part == "aid" or part == 'path' or part == 'host':
      new_vmess[part] = vmess_data[part]
    else:
      change = input('perlukah mengganti '+ part + ' y/n')
      if change == 'y':
        new_vmess[part] = input(part + ' ==> ')
      else:
        new_vmess[part] = vmess_data[part]
  print(json_to_vmess(new_vmess))



if __name__ == "__main__":
    vmess_url = input("Masukan Vmess ==>  ")
    edit(vmess_url)
# Contoh penggunaan
# uuid = "your-uuid"
# address = "your-server-address"
# port = 12345
# security = "auto"

# encoded_vmess_url = encode_vmess(uuid, address, port, security)
# print("Encoded VMess URL:", encoded_vmess_url)

# decoded_vmess_data = decode_vmess(encoded_vmess_url)
# print("Decoded VMess Data:", decoded_vmess_data)