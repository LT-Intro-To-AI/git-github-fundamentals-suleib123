from random import randint

f_name = input("What is your first name? ") 
l_name = input("What is your last name? ")

print("Hello", f_name, l_name+"!")

guess = input("Guess a number 1-10: ")

if guess != randint(1, 10):
    print("Wrong")
else:
    print("Correct")