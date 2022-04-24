import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = "@$%#&*^!@`~_++()|{}/?"
numbers = "123456789"

passwordContain = lower + upper + symbols + numbers

while True:
    print("Choose an Option : \n\t1)Create Password\n\t2)Exit")
    choice = input("Your Choice : ")
    if choice == "1":
        length = int(input("Enter length of password : "))
        passwordHasher = "".join(random.sample(passwordContain,length))
        print(passwordHasher)
    elif choice == "2":
        break
    else:
       print("Sorry just Choose 1 or 2 !!!")
