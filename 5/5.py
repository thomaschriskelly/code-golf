def evenly_divisible(num):
	return all(num%i==0 for i in range(1, 20))

def main():
	i = 20
	while True:
		if(evenly_divisible(i)):
			print(i)
			return
		i = i+1

main()	
