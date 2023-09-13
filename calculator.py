f = 'y'
while f == 'y':
    x = float(input("Enter first number: "))
    y = float(input("Enter the second number: "))
    choice = int(input("Enter any one of the choices: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nPlease enter your choice now: "))
    if(choice == 1):
        a = x+y
        print(x," + ",y," = ",a)
    elif(choice == 2):
        b = x - y
        print(x, " - ", y, " = ", b)
    elif (choice == 3):
        c = x*y
        print(x, " * ", y, " = ", c)
    elif (choice == 4):
        d = x/y
        print(x, " / ", y, " = ", d)
    else:
        print("The input doesn't match with any of the above options. ")
    f = input("Do you wanna continue: y/n: ")
    if f == 'n':
        print("Thank you for using the calculator! ")



