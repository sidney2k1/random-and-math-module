import random
options=["rock","paper","scissors"]
userchoice=input("choose rock paper or scissors:")
computerchoice=random.choice(options)
print("you chose",userchoice)
print("computer chose",computerchoice)
if userchoice==computerchoice:
    print("its a tie!!")
elif userchoice=="scissors" and computerchoice=="paper":
    print("Scissors cut paper so u win")
elif userchoice=="rock" and computerchoice=="scissors":
    print("rock smashes scissors so u win")
elif userchoice=="paper" and computerchoice=="rock":
    print("Paper covers rock so u win")
else:
    print("U lost")