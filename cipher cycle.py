exa = input("Enter string")
y = int(input("How many characters you want to shift? "))
        
r =""
for i in range(len(exa)):
    char = exa[i]
    r += chr(ord(char)+ y)
    print(r)


input("press enter")
