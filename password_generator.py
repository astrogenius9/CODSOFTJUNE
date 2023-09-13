import random
import string

f = "y"
a = 0
while f.lower() == "y":
    y = ""
    a = int(input("Enter the number of characters/digits you want to randomly generate: "))
    b = int(input("Enter any one of the choices from above: \n1. Generate characters and digits\n2. Generate characters, digits and punctuations.\n3. Generate only digits.\nPlease type your option here: "))
    if (b == 1):
        for i in range(a):
            randompasswd = random.choice(string.ascii_letters+string.digits)
            y+=randompasswd
    elif (b == 2):
        for i in range(a):
            randompasswd = random.choice(string.ascii_letters+string.digits+string.punctuation)
            y+=randompasswd
    elif (b == 3):
        for i in range(a):
            randompasswd = random.choice(string.digits)
            y+=randompasswd
    else:
        print("The input is invalid. ")
    print(y," is your randomly generated password. ")

    f = input("Do you want to generate another random password: y/n: ")
    if f.lower() == "n":
        print("Your final generated password is: ", y)
        print("Thank you for using the random generator program!")

