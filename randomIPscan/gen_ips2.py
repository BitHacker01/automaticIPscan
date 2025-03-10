import random

def gen_ran_ipv4():
	return ".".join(str(random.randint(0,255)) for i in range(4))
	
output='domain2.txt'	
num_ip=10
with open(output,'w') as file:
	for i in range(num_ip):
		ip=gen_ran_ipv4()
		file.write(ip + '\n')
