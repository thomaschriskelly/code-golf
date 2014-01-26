import math

def is_prime(num):
	return math.factorial(num-1)%n != -1 

num = 600851475143
for i in xrange(2, int(math.ceil(math.sqrt(num)))):
	if(num%i==0 and is_prime(num/i)):
		print num/i
		break

