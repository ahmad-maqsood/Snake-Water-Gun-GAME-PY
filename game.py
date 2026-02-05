import random

playerName = input("Enter the player's name : ")

opponentNames = ["Subtain", "Hussain", "Zainab", "Anas", "Moiz", "Ahmed", "Ayesha", "Sana", "Zubair", "Khadija"]
computerName = random.choice(opponentNames)

print(f'=========="{playerName}" vs "{computerName}"==========')

options = ["s","w","g"]
playerScore = 0
computerScore = 0
roundNum = 1

while(True):
    print(f"==========Round # {roundNum}==========")
    print("Snake, Water, Gun : 's', 'w', 'g'")
    playerChoice = input("Make your move : ").lower()

    computerChoice = random.choice(options)

    if(playerChoice != "s" and playerChoice != "w" and playerChoice != "g"):
        print("Wrong Choice. Try Again.")
        continue

    print(f"{playerName} Chose : {playerChoice} || {computerName} Chose : {computerChoice}")

    print("======================")
    if(playerChoice == computerChoice):
        print("It's a draw!")

    elif(playerChoice=="s"):
        if(computerChoice=="w"):
            print(f"{playerName} won this round😋😎")
            print(f"{computerName} lost this round😥")
            playerScore+=1
        elif(computerChoice=="g"):
            print(f"{computerName} won this round😋😎")
            print(f"{playerName} lost this round😥")
            computerScore+=1

    elif(playerChoice=="w"):
        if(computerChoice=="g"):
            print(f"{playerName} won this round😋😎")
            print(f"{computerName} lost this round😥")
            playerScore+=1
        elif(computerChoice=="s"):
            print(f"{computerName} won this round😋😎")
            print(f"{playerName} lost this round😥")
            computerScore+=1

    elif(playerChoice=="g"):
        if(computerChoice=="s"):
            print(f"{playerName} won this round😋😎")
            print(f"{computerName} lost this round😥")
            playerScore+=1
        elif(computerChoice=="w"):
            print(f"{computerName} won this round😋😎")
            print(f"{playerName} lost this round😥")
            computerScore+=1
    

    continueGame = input("Another Round? Press Y to continue : ")
    if(continueGame=="y" or continueGame=="Y"):
        print("==========Oh yeah!😈==========")
        print(f"Score :-")
        print(f"{playerName} : {playerScore} || {computerName} : {computerScore}")

    else:
        print("==========Scared already?😏==========")
        print(f"Score :-")
        print(f"{playerName} : {playerScore} || {computerName} : {computerScore}")

        if(playerScore==computerScore):
            print("The match was a tie.")
        elif(playerScore>computerScore):
            print(f"{playerName} won this match!")
        else:
            print(f"{computerName} won this game!")
        break
    roundNum+=1