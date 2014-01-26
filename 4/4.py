def is_palin(num):
	stringed = str(num)
	return stringed == stringed[::-1]

def main():
	highest = 0
	for i in reversed(range(100,999)):
		for j in reversed(range(100,999)):
			product = i*j
			if(is_palin(product)):
				highest = max(highest, product)
	print highest
				
main()
