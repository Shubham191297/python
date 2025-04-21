import random

gameResult = [
    [0,1,-1],
    [-1,0,1],
    [1,-1,0]
]

choice = ["snake 🐍", "water 💦", "gun 🔫"]

print("=====Welcome to the game=====\n0. Snake\n1. Water\n2. Gun")
answer = int(input("Enter your choice: "))

computerAnswer = random.randint(0,2)

compSelect = choice[computerAnswer]
userSelect = choice[answer]

outcome = gameResult[answer][computerAnswer]

if(outcome==1):
    print(f"Computer chose {compSelect} and you chose {userSelect}. You win 🏆")
elif(outcome==-1):
    print(f"Computer chose {compSelect} and you chose {userSelect}. You loose 🔻")
else:
    print(f"Computer chose {compSelect} and you chose {userSelect}. Its a draw 😉")