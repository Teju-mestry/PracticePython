i = int(input("Enter number ="))
a =2
while a>1 and a<i:
	if (i%a ==0):
		print("{} is not a prime number".format(i))
		break
	a=a+1
else:
	print("{} is prime number".format(i))
	
input("press enter")
