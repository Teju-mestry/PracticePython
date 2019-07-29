
def greatest(r,e):
	if(r>e):
		return("{} is greater than {}".format(r,e))
	elif(e>r):
		return("{} is greater then {}".format(e,r))
	else:
		return("Both numbers are equal")

print("enter two number")
x = int(input('first number ='))
y = int(input('second number ='))

x = greatest(x,y)
print(x)

input("Press enter")
