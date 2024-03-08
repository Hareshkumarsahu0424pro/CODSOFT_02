def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
def exponent(x,y):
   return x**y
print("enter number to select a operation:")
print("click 1 for addition")
print("click 2 for subtraction")
print("click 3 for multiplication")
print("click 4 for division")
print("click 5 for exponent")
while True:
    choice=input("enter your choice here(1/2/3/4/5):")
    if choice in ('1','2','3','4','5'):
     num1=float(input("enter first number:"))
     num2=float(input("enter second number:"))
     if choice=='1':
        print("result of addition is:",addition(num1,num2))
     elif choice=='2':
        print("result of subtraction is:",subtraction(num1,num2))
     elif choice=='3':
        print("result of multiplication is:",multiplication(num1,num2))
     elif choice=='4':
        print("result of division is:",division(num1,num2))
     elif choice=='5':
        print("result of exponent is:",exponent(num1,num2))
    else:
      print("choice not match try another choice")
    next=input("do you want to do more calculation?:(y/n)")
    if next!='y':
       break