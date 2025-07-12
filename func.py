def calculation(a,b):

    addition = a+b
    subtraction = a-b
    return addition,subtraction
x = int(input("Enter your first number:"))
y = int(input("Enter your second number:"))

res,res2 = calculation(x,y)
print("Addition:"+str(res))
print("Subtraction:"+str(res2))
print("Addition",res)


