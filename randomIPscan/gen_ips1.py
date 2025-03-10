import random 
def gen_ip():
	octet1 = random.randint(80,130)
	octet2 = random.randint(0,10)
	octet3 = random.randint(0,10)
	octet4 = random.randint(0,10)
	
	ip_add = f"{octet1}.{octet2}.{octet3}.{octet4}"
	return ip_add

def save(filename,num_ip):
	with open(filename, 'w') as file:
		for i in range(num_ip):
			ip=gen_ip()
			file.write(ip + '\n')

num_ip = 1000

output = 'random_ips.txt'

save(output,num_ip)

print(f"{num_ip} random IP addresses have been saved to {output}.")
