#game board 

game_board = ["-","-","-",
"-","-","-",
"-","-","-",]



#display board
def display_board():
    print(f'{game_board[0]} | {game_board[1]} | {game_board[2]}')
    print(f'{game_board[3]} | {game_board[4]} | {game_board[5]}')
    print(f'{game_board[6]} | {game_board[7]} | {game_board[8]}')

current_player = 'x'
game_mode = True
winner = None

#play game 
def play_game():
    global game_mode
    print(f"WELCOME \U0001F60A")
    display_board()
    while game_mode:
        
        player_movement(current_player)
        toggle_player()
        game_still_on()
    if winner == 'x' or winner == 'o':
        print(f'{winner} won \U0001F60D')
    elif winner == None:
        print('TIE \U0001F614')
    


        
        

#check user input/player movement
def player_movement(player):
    print(f'it\'s {player}\'s turn')
    user_first_input = input('PLEASE CHOOSE A  NUMBER FROM 1-9 TO FILL SPECIFIC POSITION: ')
    #check for valid input from the user
    while user_first_input not in ['1','2','3','4','5','6','7','8','9']:
        user_first_input = input('ALPHABET OR NUMBER GREATER THAN 9 ARE NOT ALLOWED: ')
    
    #check current position 
    position = int(user_first_input) - 1
    while game_board[position] != "-":
        position = int(input(f'POSITION {position + 1} HAS PLAYER {game_board[position]} PLEASE SELECT AN EMPTY POSITION: ')) - 1
    game_board[position] = player
    display_board()


def game_still_on():
    check_winner()
    game_tie()

#check winner
def check_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_column()
    diagonal_winner = check_diagonal()
    #check_Tie()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    


def check_rows():
    global game_mode
    row_1 = game_board[0] == game_board[1] == game_board[2] != "-"
    row_2 = game_board[3] == game_board[4] == game_board[5] != "-"
    row_3 = game_board[6] == game_board[7] == game_board[8] != "-"

    if row_1 or row_2 or row_3:
        game_mode = False
        if row_1:
            return game_board[0]
        elif row_2:
            return game_board[1]
        elif row_3:
            return game_board[2]

def check_column():
    global game_mode
    column_1 = game_board[0] == game_board[3] == game_board[6] != "-"
    column_2 = game_board[1] == game_board[4] == game_board[7] != "-"
    column_3 = game_board[2] == game_board[5] == game_board[8] != "-"

    if column_1 or column_2 or column_3:
        game_mode = False
        if column_1:
            return game_board[0]
        elif column_2:
            return game_board[1]
        elif column_3:
            return game_board[2]
        

def check_diagonal():
    global game_mode
    diagonal_1 = game_board[0] == game_board[4] == game_board[8] != "-"
    diagonal_2 = game_board[6] == game_board[4] == game_board[2] != "-"

    if diagonal_1 or diagonal_2:
        game_mode = False
        if diagonal_1:
            return game_board[0]
        elif diagonal_2:
            return game_board[6]

def game_tie():
    global game_mode
    if "-" not in game_board:
        game_mode = False


# toggle player
def toggle_player():
    global current_player
    if current_player == 'x':
        current_player = 'o'
    elif current_player == 'o':
        current_player = 'x'






while  True:
    play_game()
    option_to_play_agin = input('will you like to play again[y/n]: ')
    if option_to_play_agin == 'y':
        game_mode = True
        game_board = ["-","-","-",
                    "-","-","-",
                    "-","-","-",]

        play_game()
        
    else:
        break




