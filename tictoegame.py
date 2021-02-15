import random

## Introduction to the game ##
print("****************  Welcome to the TIC TOE GAME  *****************************")

enter = input("do you want to the game?   (yes or no): ")

if(enter == "yes" or enter == "YES"):

## Taking information of the players ##
  
    player1 = input("enter the name Player1: ")    ## player one informattion
    print("Welcome To The Game \"{}\"  Play Well".format(player1))

    print("\n")
    
    player2 = input("enter the name Player2: ")     ## player two infromation
    print("Welcome To The Game \"{}\"  Play Well".format(player2))

    print("\n")

## Toss ##
    

    nm1 = [player1,player2]
    ## op1 = NULL                      ## token one
    ## op2 = NULL                      ## token two
    ## ch2 = NULL

    ch1 = random.choice(nm1)               ## the player is chosen randomly
    if(ch1 == player1):
        ch2 = player2
    else:
        ch2 = player1
    
    print('\"{}\"  WON the toss you start the game'.format(ch1))
    print("\n")
    
    op1 = input("choose X or O: ")      ## choose X or O
    
    if(op1 == "X"):
        op2 = "O"
    else:
        op2 = "X"

    print('\"{}\"  is going to play with  \"{}\" '.format(ch1,op1))     ## printing the player name and the one token to play with
    print("\n")
    print('\"{}\"  is going to play with \"{}\" '.format(ch2,op2))      ## printing the player name and the one token to play with
    print("\n")
    
    print("\n")


    
## the format of the tic toe pad
    
    print("### Display of the Game Pad on which we play the tic toe: ")          ## the display of the table

    print("\n")
    
    li = [[0,0,1,0,0,1,0,0],[2,2,1,2,2,1,2,2],[0,0,1,0,0,1,0,0],[2,2,1,2,2,1,2,2],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0]]
    for i in range(len(li)):
        p=0
        while(p<7):
            if(li[i][p]==0):
                print("  ",end="")
                p+=1
            elif(li[i][p]==1):
                print("|" , end="")
                p+=1
            elif(li[i][p]==2):
                print("__",end="")
                p+=1
        
        if(p==7):
            if(li[i][p]==0):
                print(" ")
            elif(li[i][p]==1):
                print("|")
            elif(li[i][p]==2):
                print("__")
    
    print("\n")
    
## displaying the format to choose from the  table
    mi = [[0,10,1,0,11,1,0,12],[2,2,1,2,2,1,2,2],[0,20,1,0,21,1,0,22],[2,2,1,2,2,1,2,2],[0,30,1,0,31,1,0,32],[0,0,1,0,0,1,0,0]]  
    for i in range(len(li)):
        p=0
        while(p<7):
            if(mi[i][p]==0):
                print("  ",end="")
                p+=1
            elif(mi[i][p]==1):
                print("|" , end="")
                p+=1
            elif(mi[i][p]==2):
                print("__",end="")
                p+=1
            elif(mi[i][p]==10):
                print("UL",end="")                                ## assigning the codes to the table
                p+=1
            elif(mi[i][p]==11):
                print("UM",end="")
                p+=1
            elif(mi[i][p]==12):
                print("UR",end="")
                p+=1
            elif(mi[i][p]==20):
                print("ML",end="")
                p+=1
            elif(mi[i][p]==21):
                print("MM",end="")
                p+=1
            elif(mi[i][p]==22):
                print("MR",end="")
                p+=1
            elif(mi[i][p]==30):
                print("LL",end="")
                p+=1
            elif(mi[i][p]==31):
                print("LM",end="")
                p+=1
            elif(mi[i][p]==32):
                print("LR",end="")
                p+=1
        
        if(p==7):
            if(mi[i][p]==0):
                print("  ")
    
            elif(mi[i][p]==1):
                print("|")
                
            elif(mi[i][p]==2):
                print("__")
                
            elif(mi[i][p]==10):
                print("UL")
                
            elif(mi[i][p]==11):
                print("UM")
                
            elif(mi[i][p]==12):
                print("UR")
                
            elif(mi[i][p]==20):
                print("ML")
                
            elif(mi[i][p]==21):
                print("MM")
                
            elif(mi[i][p]==22):
                print("MR")
                
            elif(mi[i][p]==30):
                print("LL")
                
            elif(mi[i][p]==31):
                print("LM")
                
            elif(mi[i][p]==32):
                print("LR")

    print("\n")


## start the atcual game 
    count_moves1 = 0                  ### number of moves for the first player
    count_moves2 = 0                  ### number of moves for the second player
    
    ## moves taken by the first player

    while(count_moves1 < 5):
        ## this is the base counting for the game
    
        print("choose upper row:- [UL: 10,UM: 11,UR: 12]")
        print("      middle row:- [ML: 20,MM: 21,MR: 22]")
        print("       lower row:- [LL: 30,LM: 31,LR: 32]")
        
    ## w1 ="NULL"
    ## w2 ="NULL"
    
        w1 = int(input('enter the block \"{}\"  to put the \"{}\" :  '.format(ch1,op1)))   ## player who won the toss plays the first move
        print("\n")
    ## placing the token in the table
     
        for i in range(1):
            if(w1 == 10):
                li[0][1] = op1
        
            elif(w1 == 11):
                li[0][4] = op1
        
            elif(w1 ==12):
                li[0][7] = op1
        
            elif(w1 == 20):
                li[2][1] = op1
        
            elif(w1 == 21):
                li[2][4] = op1
        
            elif(w1 == 22):
                li[2][7] = op1
        
            elif(w1 == 30):
                li[4][1] = op1
        
            elif(w1 == 31):
                li[4][4] = op1
        
            elif(w1 == 32):
                li[4][7] = op1

    ## displaying the table after placing the token in the table

        for i in range(len(li)):
            p=0
            while(p<7):
                if(li[i][p]==0):
                    print("  ",end="")
                    p+=1
                elif(li[i][p]==1):
                    print("|" , end="")
                    p+=1
                elif(li[i][p]==2):
                    print("__",end="")
                    p+=1
                elif(li[i][p] == op1):
                    print(op1 + " ",end="")
                    p+=1
                else:
                    print(op2 + " ",end="")
                    p+=1
        
        
            if(p==7):
                if(li[i][p]==0):
                    print(" ")
                elif(li[i][p]==1):
                    print("|")
                elif(li[i][p]==2):
                    print("__")
                elif(li[i][p]==op1):
                    print(op1 + " ")
                else:
                    print(op2 + " ")    
        
        print("\n")

        if( (li[0][1]==li[0][4]==li[0][7]==op1) or (li[0][1]==li[2][4]==li[4][7]==op1) or (li[0][7]==li[2][4]==li[4][1]==op1) or (li[2][1]==li[2][4]==li[2][7]==op1) or (li[4][1]==li[4][4]==li[4][7]==op1) or (li[0][1]== li[2][1]==li[4][1]==op1) or (li[0][4]==li[2][4]==li[4][4]==op1) or (li[0][7]==li[2][7]==li[4][7]==op1) ):
            print('\"{}\" YOU HAVE WON THE GAME !!!!! ☻☻☻☻'.format(ch1))
            break
        
        #### moves taken by the second player

        if(count_moves2 < 4):
            
            w2 = int(input('enter the block \"{}\"  to put the \"{}\" :  '.format(ch2,op2)))   ## the other player makes the first move
            
            for i in range(1):

                if(w2 == 10):
                    li[0][1] = op2
                
                elif(w2 == 11):
                    li[0][4] = op2
        
                elif(w2 ==12):
                    li[0][7] = op2
        
                elif(w2 == 20):
                    li[2][1] = op2
        
                elif(w2 == 21):
                    li[2][4] = op2
        
                elif(w2 == 22):
                    li[2][7] = op2
        
                elif(w2 == 30):
                    li[4][1] = op2
        
                elif(w2 == 31):
                    li[4][4] = op2
        
                elif(w2 == 32):
                    li[4][7] = op2


            for i in range(len(li)):
                p=0
                while(p<7):
                    if(li[i][p]==0):
                        print("  ",end="")
                        p+=1
                    elif(li[i][p]==1):
                        print("|" , end="")
                        p+=1
                    elif(li[i][p]==2):
                        print("__",end="")
                        p+=1
                    elif(li[i][p] == op1):
                        print(op1 + " ",end="")
                        p+=1
                    else:
                        print(op2 + " ",end="")
                        p+=1
        
                if(p==7):
                    if(li[i][p]==0):
                        print(" ")
                    elif(li[i][p]==1):
                        print("|")
                    elif(li[i][p]==2):
                        print("__")
                    elif(li[i][p] == op1):
                        print(op1 + " ")
                    else:
                        print(op2 + " ")
    
            print("\n")
        
        count_moves1+=1
        count_moves2+=1

        
        if( (li[0][1]==li[0][4]==li[0][7]==op2) or (li[0][1]==li[2][4]==li[4][7]==op2) or (li[0][7]==li[2][4]==li[4][1]==op2) or (li[2][1]==li[2][4]==li[2][7]==op2) or (li[4][1]==li[4][4]==li[4][7]==op2) or (li[0][1]== li[2][1]==li[4][1]==op2) or (li[0][4]==li[2][4]==li[4][4]==op2) or (li[0][7]==li[2][7]==li[4][7]==op2) ):
            print('\"{}\" YOU HAVE WON THE GAME !!!!! ☻☻☻☻'.format(ch2))
            break

    
    



       
    

    


    
    
                       
    






    



