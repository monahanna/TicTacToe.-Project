import os    
import time    
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
   
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    

Game = Running    
Mark = 'X'    
def DrawBoard():    
    print(" %s | %s | %s " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %s | %s | %s " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %s | %s | %s " % (board[7],board[8],board[9]))    
    print("   |   |   ")    

def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False        
def CheckWin():    
    global Game  
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win  
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win   
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win   
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running  
#Added a welcome message, these print statements are placed at the beginning of the code, just before the game starts. They will be executed when the program runs, displaying the welcome message to the players.
print("Welcome to Tic-Tac-Toe!")
print("Get ready to enjoy some exciting rounds of Tic-Tac-Toe!")
print("May the best player win! Have fun!")
# added ASCII art representing a Tic-Tac-Toe board at the beginning of the code. This enhances the visual presentation of the game and gives players a clear understanding of the game board layout. I also added a comment to explain the purpose of the ASCII art.
print("\n" + 
    " 1 | 2 | 3 \n" +
    "___|___|___\n" +
    " 4 | 5 | 6 \n" +
    "___|___|___\n" +
    " 7 | 8 | 9 \n" +
    "   |   |   \n") 
# added line 51 describing the rules of the game for players who haven't played the game before.
print("\nRules:\nThis is a two player game where each player will take turns marking\n an empty square and who evers gets 3 of their mark in a row in\n any direction wins the game!")
print("\n\n\nTic-Tac-Toe Game\n")  
# instead of having "player 1 and player 2", users are able to name themselves
player_1 = input('Player 1, please enter your name: ')  
print('Hi',player_1 + ", you are player 1.\n")
player_2 = input('Player 2, please enter your name: ')
print('Hi',player_2 + ", you are player 2.\n")
# allowed players to customize their marks instead of the traditional "X" and "O"
player1_mark = input(player_1 + " please input your mark character if you wish to customize. To use the default mark please enter 'X': ")
player2_mark = input(player_2 + " please input your mark character if you wish to customize. To use the default mark please enter 'O': ")

print("Player 1 [" + player1_mark + "] --- Player 2 [" + player2_mark + "]\n")    
print()    
print()    
print("Please Wait...")    
time.sleep(3)    
while(Game == Running):    
    os.system('cls')    
    DrawBoard()    

    if(player % 2 != 0):    
        print(player_1 + "-Player 1's chance")    
        Mark = player1_mark    
    else:    
        print(player_2 + "-Player 2's chance")    
        Mark = player2_mark    
    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
    if(CheckPosition(choice)):    
        board[choice] = Mark    
        player+=1    
        CheckWin() 
     
os.system('cls')    
DrawBoard()    
if(Game==Draw):    
    print("Game Draw")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print(player_1,"Won!")    
    else:    
        print(player_2,"Won!")
