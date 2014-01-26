t1=1
t2=2
mySum=0
while(t2<4000000):
	if(t2%2 == 0):
		mySum+=t2
	t1, t2 = t2, t1
	t2 = t1 + t2
print mySum
