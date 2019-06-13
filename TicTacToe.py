import time
#Input for X or O form the players
def players():
    while True:
        p1=input("Enter your choice Player 1").upper()
        if(p1 in "XO")and (p1!=""):
            break
    if(p1=="X"):
        p2="O"
    else:
        p2="X"
    return p1,p2

# draw game
def draw():

    print(x,board[0],x,board[1],x,board[2],x)
    print("-------------")
    print(x,board[3],x,board[4],x,board[5],x)
    print("-------------")
    print(x,board[6],x,board[7],x,board[8],x)
    print("-------------")

# for waiting
def wait():
    print("Please wait...\n")
    time.sleep(1)

# Taking users choice about where they want to put there signs
def choice():
    count=1
    c=""
    while(count<=9):
        if(count%2!=0):
            try:c=int(input("Enter your choice Player 1 from (1-9)"))
            except:
                print("Not a valid input, Enter from (1-9) ")
                continue
            if(board[c-1]==" "):
                board[c-1]=p1
                draw()
                count+=1
            elif(board[c-1]!=" "):
                print("Already taken")

        else:
            try:c=int(input("Enter your choice Player 2 from (1-9)"))
            except:
                print("Not a valid input, Enter from (1-9) ")
                continue
            if(board[c-1]==" "):
                board[c-1]=p2
                draw()
                count+=1
            elif(board[c-1]!=" "):
                print("Space already taken")


# For checking the winner
def winner():
    p1_c=0
    p2_c=0
    if(board[0]==p1 and board[1]==p1 and board[2]==p1) or (board[3]==p1 and board[4]==p1 and board[5]==p1)or(board[6]==p1 and board[7]==p1 and board[8]==p1):
        print(f"{p1} wins the row ")
        p1_c+=1
    if(board[0]==p2 and board[1]==p2 and board[2] ==p2)or(board[3]==p2 and board[4]==p2 and board[5]==p2)or(board[6]==p2 and board[7]==p2 and board[8]==p2):
        print(f"{p2} wins the row")
        p2_c+=1
    if(board[0]==p1 and board[3]==p1 and board[6]==p1)or(board[2]==p1 and board[4]==p1 and board[7]==p1)or(board[3]==p1 and board[5]==p1 and board[8]==p1):
        print(f"{p1} wins the column")
        p1_c+=1
    if(board[0]==p2 and board[3]==p2 and board[6]==p2)or(board[2]==p2 and board[4]==p2 and board[7]==p2)or(board[3]==p2 and board[5]==p2 and board[8]==p2):
        print(f"{p2} wins the column")
        p2_c+=1
    if(board[0]==p1 and board[4]==p1 and board[8]==p1)or(board[2]==p1 and board[4]==p1 and board[6]==p1):
        print(f"{p1} wins the diagonal")
        p1_c+=1
    if(board[0]==p2 and board[4]==p2 and board[8]==p2)or(board[2]==p2 and board[4]==p2 and board[6]==p2):
        print(f"{p2} wins the diagonal")
        p2_c+=1

    time.sleep(1)
    # announcing the winner
    if(p1_c==p2_c):
        print("Its a draw")
    elif(p1_c>p2_c):
        print(f"{p1} is the winner")
    else:
        print(f"{p2} is the winner")



print("WELCOME")
p1,p2=players()
print(f"Player 1 :{p1}")
print(f"Player 2 :{p2}")
wait()
print("Here is the board")
# board for TIC TAC TOE
x='|'
board=[" "," "," ",
       " "," "," ",
       " "," "," "]
draw()
choice()
winner()
