import random
playing=True
number=str(random.randint(10,20))
print("I will generate a number between 10 and 20. If u guess the number correctly, u win")
print("you have to guess one number at a time")
while playing:
    guess=input("Enter the number:\n")
    if number==guess:
        print("You have won the game")
        print("The number was",number)
        break
    else:
        print("Try again next time")