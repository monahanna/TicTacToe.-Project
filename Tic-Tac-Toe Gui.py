import os    
import time    

# Define initial game variables
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
Game = Running    
Mark = 'X'   

# Define different themes with color codes
themes = {
    1: {'border': '\033[95m', 'empty': '\033[0m', 'player1': '\033[91m', 'player2': '\033[94m'},
    2: {'border': '\033[92m', 'empty': '\033[0m', 'player1': '\033[91m', 'player2': '\033[94m'},
    # Add more themes as desired
}

# Function to check if a position on the board is available
def CheckPosition(x):    
    if board[x] == ' ':    
        return True    
    else:    
        return False     
        
# Function to draw the game board using the selected theme
    # Apply colors from the selected theme
    border_color = theme['border']
    empty_color = theme['empty']
    player1_color = theme['player1']
    player2_color = theme['player2']
    
# Function to draw the game board using the selected theme
def DrawBoard(theme):  
    # Apply colors from the selected theme
    border_color = theme['border']
    empty_color = theme['empty']
    player1_color = theme['player1']
    player2_color = theme['player2']
    
    #added a border to the board game and changed "%c" to "%s" to accept string


# Function to check if a player has won the game
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
   



# Added describing the rules of the game for players who haven't played the game before.
print("\nRules:\nThis is a two-player game where each player will take turns marking\n an empty square and who evers gets 3 of their mark in a row in\n any direction wins the game!")

    
# Instead of having "player 1 and player 2", users are able to name themselves
player_1 = input('Player 1, please enter your name: ')  
print('Hi', player_1 + ", you are player 1.\n")
player_2 = input('Player 2, please enter your name: ')
print('Hi', player_2 + ", you are player 2.\n")

# Allowed players to customize their marks instead of the traditional "X" and "O"
player1_mark = input(player_1 + " please input your mark character if you wish to customize. To use the default mark please enter 'X': ")
player2_mark = input(player_2 + " please input your mark character if you wish to customize. To use the default mark please enter 'O': ")
print("Player 1 [" + player1_mark + "] --- Player 2 [" + player2_mark + "]\n")    
print()    
print()    
print("Please Wait...")    
time.sleep(3)
           


os.system('cls')    
DrawBoard(selected_theme)    
if(Game == Draw):    
    # Added ASCII art "Draw" when it is a tie  
    print("It's a draw!")
    print(" _____ ")                    
    print("|  __ | ")                   
    print("| |  | |_ __ __ ___      __")
    print("| |  | | '__| _` | | || | |")
    print("| |__| | | | |_| || V  V | ")
    print("|_____||_|  |__,_| |_||_| ")    
elif(Game == Win):    
    player -= 1    
    if(player % 2 != 0): 
        
         # Added ASCII "congrats" art to player that wins   
        print(player_1, "Has won!")
        print('                                 _ ')      
        print('                                | | ')     
        print('  ___ ___  _ __   __ _ _ __ __ _| |_ ___ ')
        print(" | __| _ || '_ | | _  | '__| _' | __| __|")
        print("| |_[ |_| ] | | | |_| | | | |_| | |_|__ |")
        print(' |___|___||_| |_||__, |_|  |__,_||__|___|')
        print('                  __| |                  ')
        print('                 |___|                   ')    
    else:    
        print(player_2,"Has won!")
        print('                                 _ ')      
        print('                                | | ')     
        print('  ___ ___  _ __   __ _ _ __ __ _| |_ ___ ')
        print(" | __| _ || '_ | | _  | '__| _' | __| __|")
        print("| |_[ |_| ] | | | |_| | | | |_| | |_|__ |")
        print(' |___|___||_| |_||__, |_|  |__,_||__|___|')
        print('                  __| |                  ')
        print('                 |___|                   ')
