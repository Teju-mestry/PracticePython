import math

print("Enter two numbers")

x = int(input("x= "))
y = int(input("y = "))

gcd = math.gcd(x,y)
lcm = str((x*y)/gcd)

print("LCM = "+lcm)
input("press enter")
