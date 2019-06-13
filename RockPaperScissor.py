# rock paper scissors game

print("Lets play ROCK PAPER SCISSORS :)\n RULES:Rock beats scissors\n Scissors beats paper \n Paper beats rock\n")
print(" *****REMEMBER*****")
print("ENTER R for ROCK\nS for SCISSORS\nP for PAPER")

while True:
    print("Enter your choice from 'R' 'P' and 'S'\n")
    p1=input("PLAYER 1 : ")
    p2=input("PLAYER 2 : ")
    if(p1=="R" and p2=="S")or(p1=="S" and p2=="P")or(p1=="P" and p2=="R"):
        print("\nHURRAH !\nPlayer 1 is the winner")
    elif(p1=="S" and p2=="R" )or(p1=="P" and p2=="S")or(p1=="R" and p2=="P"):
        print("\nyayy !\nyou rocked Player 2")
    elif(p1==p2):
        print("\nIts a tie. you can try agian")
    else:
        print("\nEnter the appropriate choice")
    i=input("\nContinue (Y/N) ")
    if(i=="N"):
            break
