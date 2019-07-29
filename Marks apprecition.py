import operator
x = int(input("how many students are present in class?"))
name = []
marks = []
dic ={}
if x>=3:
        for i in range(0,x) :
            n = input("Name of student {} = ".format(i+1))
            name.append(n)
            m = int(input("Marks of student {} = ".format(i+1)))
            marks.append(m)
            dic.update({name[i]:marks[i]})
else:
    print("Number of student must be atleast 3")
            

dics = dict( sorted(dic.items(), key=operator.itemgetter(1),reverse=True))
tup = ("$500","$300","$100")


print("Congratulations! {}.You got first rank in class with {} marks And you rewarded with {}.".format(list(dics.keys())[0],list(dics.values())[0],tup[0]))
    
print("Congratulations! {}.You got second rank in class with {} marks And you rewarded with {}.".format(list(dics.keys())[1],list(dics.values())[1],tup[1]))
    
print("Congratulations! {}.You got third rank in class with {} marks And you rewarded with {}.".format(list(dics.keys())[2],list(dics.values())[2],tup[2]))


for i in range(0,x):
    if list(dics.values())[i] >= 950 :
         print("{} your work is appreciable.Keep it up.".format(list(dics.keys())[i]))

input("Press enter")
         



