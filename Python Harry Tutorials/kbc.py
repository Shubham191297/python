kbcQuiz = [
    {"query": "Which coding language is the most efficient for machine learning?","options":["C++","Javascript","Python","Golang"], "answer": 2, 1: "Shubham"},
    {"query": "Which loop is exit control loop from following?","options":["do-while","for of","while","for"],"answer":0},
    {"query": "Which of the following datatypes are immutable?","options":["string","tuple","list","map"],"answer":1}    
]

print("================================")
print("        Welcome to KBC          ")
print("================================")
amount = 2500000
optionSerial=["A","B","C","D"]

for i in range(len(kbcQuiz)):
    prizeAmount = amount*(i+1)
    print("\n\n")
    print("Your",i+1,"question for the amount of Rs",prizeAmount,"is as below")
    print(kbcQuiz[i]["query"])
    
    optionsForAnswer = kbcQuiz[i]["options"]
    correctAnswer = kbcQuiz[i]["answer"]
    
    for p in range(len(optionsForAnswer)):
        print(optionSerial[p],kbcQuiz[i]["options"][p])
        
    answer=input("Enter your answer option:")
    answerIndex = optionSerial.index(answer)
    
    if(answerIndex==correctAnswer):
        print("Congratulations!!! You have won Rs", prizeAmount,".")
        choice = input("Do you want to go to next level OR quit with the prize money?\n y to next level & n to quit:")
        if(choice=="y"):
            print("Welcome to next level!!")
        elif(choice=="n"):
            print("Great to have you. Lets see you next time")
            break
    else:
        print("Sorry your answer is wrong. Right answer is option",optionSerial[answerIndex],optionsForAnswer[correctAnswer],"Great to have you. Lets see you next time")
        break
    