import os
def print_board(board):
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if j < (len(board[0])-1):
                print(board[i][j], "| ",end="")
            else:
                print(board[i][j])
        if i < len(board)-1:
            print("----------")
            
def user_choice():
    print("welcome to Tic-Tac-Toe game!")
    print("Please enter choice of player1")
    while True:
        choice = input("Pick a player: 'X' or 'O': ")
        choice = choice.upper()
        
        if choice != 'X' and choice != 'O':
            print("Invalid choice of player. Try again!")
        else:
            return choice

def start_game():
    player1 = user_choice()
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    while True:
        _=os.system('cls')
        print_board(board)
        result = play_game(player1)
        if result == player1:
            print(f'Player1 {result} wins')
            break
        elif result == "D":
            print("Game is a draw")
            break
        
        _=os.system('cls')
        print_board(board)
        result = play_game(player2)
        if result == player2:
            print(f'Player2 {result} wins')
            break  
        elif result == "D":
            print("Game is a draw")
            break
        

    

def play_game(player):
    while True:
        print(f"Turn for '{player}' ")
        position1 = input("Please enter the position ")
        
        try: 
            position1 = int(position1)
        except:
            print("\nInvalid position. Try again!!!")
        else:
            print("position: ",position1)
            if position1 not in range(1,10):
                print("Invalid")
            
            else:
                position1 -= 1
                if not update_board(board,player,position1):
                    pass
                else:
                    response = check_status(board)
                    if response == 'success':
                        return player
                    else:
                        if response == 'D':
                            return 'D'
                        else:
                            return False
        

def update_board(board,player,position):
    
    if position < 3:
        i = 0
    elif position >= 3 and position < 6:
        i = 1
    else:
        i = 2
    
    j = (3+(position))%3
    
    if board[i][j] == 'X' or board[i][j] == 'O':
        print("The position is not empty. Try again")
        return False
    else:
        board[i][j] = player
        return True

    
def check_status(board):
    result=''
            
    for i in range(0,len(board)-1):
        j = 0
        if ((board[i][j] == board[i][j+1]) and (board[i][j+1] == board[i][j+2])) or ((board[j][i] == board[j+1][i]) and (board[j+1][i]== board[j+2][i])):
            result = 'success'
            break
    
    i,j = 0,0
    
    if (board[j][i] == board[j+1][i+1]) and (board[j+1][i+1] == board[j+2][i+2]):
        result = 'success'
    
    if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
        result = 'success'

    remaining = ''
    if result != 'success':
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    remaining = 'Y'
                    break

        if remaining != 'Y':
            result = "D"
        
    if result == 'success':
        return result
    elif result == "D":
        return result
    else:
        return False
    
        
board = [['1','2','3']
        ,['4','5','6']
        ,['7','8','9']]
start_game()