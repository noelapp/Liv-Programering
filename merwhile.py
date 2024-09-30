
age= int(input("how old are you? "))
print("your age is ", age)
if(age >= 18 and age <= 65):
    print("you aren't an adult")
elif(age < 18):
    print("you are not of age")
else:
    print("you are to old")