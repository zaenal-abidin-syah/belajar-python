import ipaddress

def generate_ip_addresses(network_address, subnet_mask, num_addresses):
  network = ipaddress.IPv4Network(f"{network_address}/{subnet_mask}", strict=False)
  ip_addresses = [str(ip) for ip in list(network.hosts())[:num_addresses]]
  return ip_addresses

def save_to_file(ip_addresses, filename):
  with open(filename, 'w') as file:
    for ip in ip_addresses:
      file.write(ip + '\n')
        

# Contoh penggunaan
network_address = "104.18.0.0"
subnet_mask = "255.255.0.0"
num_addresses = 65534
output_filename = "ip_addresses.txt"

result = generate_ip_addresses(network_address, subnet_mask, num_addresses)
save_to_file(result, output_filename)