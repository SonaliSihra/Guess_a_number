import random

x = random.randrange(1, 10)
print(x)
print("Let the game begin!! \n guess the number:")


try:
    input1 = int(input("Hint=[it is between 0 to 10]: "))

except ValueError:
    print("Please enter integer only!!")
    exit(0)

if input1 == x:
    print("Congratulations!!! this is a correct answer.")
elif input1 > (x/2):
    print("You need to lower down the number to reach your goal!")
elif input1 < (x/2):
    print("you need to rise above your guess!!")
else:
    print("Wrong answer!!! Try again with a new number!")