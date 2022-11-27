import random

object_list = ["rock", "paper", "scissor"]
ai = random.choice(object_list)
print("You can select between rock, paper and scissor!")
user = str(input("Your choose: "))

if user!= "rock" or user!= "paper" or user!= "scissor":
    print("Please insert a valid value! Error Message: 0000001")

if user == ai:
    print("You got the same!")

elif user == "rock" and ai == "scissor":
    print("You won")
    print("The AI selected", ai)

elif user == "paper" and ai == "rock":
    print("You won")
    print("The AI selected", ai)

elif user == "scissor" and ai == "paper":
    print("You won")
    print("The AI selected", ai)

elif user == "rock" and ai == "paper":
    print("The AI won")

elif user == "scissor" and ai == "rock":
    print("The AI won")

elif user == "paper" and ai == "scissor":
    print("The AI won")

else:
    print("An error occurred! Error Message: 0000002")
