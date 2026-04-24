'''
      SIMPLE CALCULATOR IN PYTHON
# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVISE
'''
print("select an operation to perfore:")
print("1 add")
print("2 subtrect")
print("3 multiply")
print("4 division")

operation = input()

if operation == "1":
    num1 = input("enter the first number: ")
    num2 = input("enter the second number: ")
    #validadion
    if(num1.isnumeric() and num2.isnumeric()):
        sum = int(num1) + int(num2)
        print("the sum of 2 numbers is :"+str(sum))
    else:
        print("type a valid number!")
elif operation == "2":
    num1 = input("enter the first number: ")
    num2 = input("enter the second number: ")
    if(num1.isnumeric() and num2.isnumeric()):
        sub = int(num1) - int(num2)
        print("the difference between 2 numbers is: "+str(sub))
    else:
        print("type a valid number!")
elif operation == "3":
    num1 = input("enter the first number:  ")
    num2 = input("enyer the second number: ")
    if(num1.isnumeric() and num2.isnumeric()):
        mul = int(num1) * int(num2)
        print("the multiplication of 2 values: "+str(mul))
    else:
        print("type a valid number!")    
elif operation == "4":
    num1 = input("enter the first number: ")
    num2 = input("enter the second number: ")
    if(num1.isnumeric () and num2.isnumeric()):
        div = int(num1) / int(num2)
        print("the division of 2 numbers is:  "+ str(div))
else:
    print("please enter the valid operation")

