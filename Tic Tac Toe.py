# This code prints the current state of the board
def display_board(board):
    boardlist = list(board)
    table = f'\t|\t|\n   {boardlist[6]}\t|   {boardlist[7]}\t|    {boardlist[8]}\n________|_______|________\n\t|\t|\n   {boardlist[3]}\t|   {boardlist[4]}\t|    {boardlist[5]}\n________|_______|________\n\t|\t|\n   {boardlist[0]}\t|   {boardlist[1]}\t|    {boardlist[2]}\n\t|\t|'
    print(table)
    
def player_input():
    # Set up Player1 and Player2 variables

    Player1 = 0
    Player2 = 0

    while Player1 != 'X' or Player1 != 'O':
    # Assign Player1 and Player2 to X or O. Give choice, force valid input
        Player1 = input('Oy, shorty, you wanna be X or O? ')

        if Player1 == 'X':
            Player2 = 'O'
            break
        if Player1 == 'O':
            Player2 = 'X'
            break
        else:
            print('I said X or O numbnuts')
            continue
def place_marker(board, marker, position):
    # This code places either an X or O onto a position on the board
    if marker == 'X':
        board[position] = 'X'
    if marker == 'O':
        board[position] = 'O'

def win_check(board, mark):
       # This code checks for the winner
    while True:
        if (board[0] == mark) and (board[1] == mark) and (board[2] == mark):
            return True
            break
        if (board[3] == mark) and (board[4] == mark) and (board[5] == mark):
            return True
            break
        if (board[6] == mark) and (board[7] == mark) and (board[8] == mark):
            return True
            break
        if (board[0] == mark) and (board[3] == mark) and (board[6] == mark):
            return True
            break
        if (board[1] == mark) and (board[4] == mark) and (board[7] == mark):
            return True
            break
        if (board[2] == mark) and (board[5] == mark) and (board[8] == mark):
            return True
            break
        if (board[0] == mark) and (board[4] == mark) and (board[8] == mark):
            return True
            break
        if (board[2] == mark) and (board[4] == mark) and (board[6] == mark):
            return True
            break
        break

import random

def choose_first():
    # This code assigns a player to go first, the assignment of X or O could
    # come after this to prevent confusion
    first = random.randint(0,1)
    if first == 0:
        print('X goes first')
    if first == 1:
        print('O goes first')
    return first

def space_check(board, position):
    # Checks to see if there is actually space to enter a value
    if board[position] == 'X':
        return False
    if board[position] == 'O':
        return False
    else:
        return True

def full_board_check(board):
    # Checks if the board is full
    if '' in board:
        return False
    else:
        return True

def player_choice(board):
    # This is how a player inputs their desired position
    
    while True:
        
        print('Choose a number between 1 and 9!')
        markposition = int(input()) - 1
        if 0 <= (markposition) <= 8:
            if space_check(theboard, markposition) is True:
                return markposition
                break
            else:
                print('That space is full')
                continue
        else:
            print('Hah, I thought of that. Enter 1-9!')
            continue
            
def replay():
    # Depending on answer this will start the loop again, or finish it
    print('Would you like to play again? y/n')
    answer = input('')
    if answer == 'y':
        return True
    if answer == 'n':
        return False    

print('Welcome to Tic Tac Toe!')
print('The winner is the person to get three of their symbol in a row!')
print('To enter your symbol into a space, look at the diagram below')
print('\t|\t|\n   7\t|   8\t|    9\n________|_______|________\n\t|\t|\n   4\t|   5\t|    6\n________|_______|________\n\t|\t|\n   1\t|   2\t|    3\n\t|\t|')
while True:
    
    player_input()
    first = choose_first() 
    theboard = ['','','','','','','','','']
    display_board(theboard)
    game_on = True
    
    if first == 0:
    
        while True:
        
            place_marker(theboard, 'X', player_choice(theboard)) 
            print('\n'*100)
            display_board(theboard)
            if win_check(theboard, 'X') == True:
                print('X is the winner! You suck O.')
                break
            if full_board_check(theboard) == True:
                print("It's a tie!")
                break
        
            place_marker(theboard, 'O', player_choice(theboard)) 
            print('\n'*100)
            display_board(theboard)
            if win_check(theboard, 'O') == True:
                print('O is the winner! You suck X.')
                break
            if full_board_check(theboard) == True:
                print("It's a tie!")
                break
    else:
        
        while True:
            
            place_marker(theboard, 'O', player_choice(theboard)) 
            print('\n'*100)
            display_board(theboard)
            if win_check(theboard, 'O') == True:
                print('O is the winner! You suck X.')
                break
            if full_board_check(theboard) == True:
                print("It's a tie!")
                break
                
            place_marker(theboard, 'X', player_choice(theboard)) 
            print('\n'*100)
            display_board(theboard)
            if win_check(theboard, 'X') == True:
                print('X is the winner! You suck O.')
                break
            if full_board_check(theboard) == True:
                print("It's a tie!")
                break
        
        
    
    if replay() == True:
        continue
    else:
        break