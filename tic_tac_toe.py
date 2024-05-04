from os import system
def board():
    d = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    return d


def display(tac_board):
    j =0
    d = tac_board
    f = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    if d !=f:
        system('cls')

    print("\nTIC TAC TOE")
    print("Current board:")
        
    print('columns ',['0','1','2'])
    for i in d:
       
        print(f'row: {j}  ', i)
        j +=1
    #system('cls')
def player(count):
    
    if count == 1:
        return 2
    else:
        return 1


def user_choice():
    row = 4
    col = 4
    while (row not in [0,1,2]) or (col not in [0,1,2]):

        if (row not in [0,1,2]):
            row = int(input("Select a row: 0,1,2: "))
            if (row not in [0,1,2]):
                continue
        
        if (col not in [0,1,2]):
            col = int(input("Select a column: 0,1,2: "))
            
    return (row,col)


 
def mark_board(tac_board,choice,player):
    row,col =choice
    b = tac_board
    while b[row][col] != ' ':
        choice = user_choice()
        row,col =choice

    if player == 1:
        b[row][col]= 'X'
        return b
    if player == 2:
        b[row][col]= 'O'
        return b

def winner(tac_board):
    b = tac_board
    sds = [
    b[0],b[1],b[2],
    [b[0][0],b[1][0],b[2][0]],
    [b[0][1],b[1][1],b[2][1]],
    [b[0][2],b[1][2],b[2][2]],
    [b[0][0],b[1][1],b[2][2]],
    [b[2][0],b[1][1],b[0][2]]
    ]
    
    if ['X','X','X'] in sds or ['O','O','O'] in sds:
        return True
    return False




def full_check(tac_board):
    full = True
    for i in tac_board:
        for j in i:
            if j == ' ':
                full = False
                return full
    return full        



play_on = True

while play_on:
    print("\nWelcome to Tic Tac Toe game!\nPlayer1: 'X'\nPlayer2: 'O'")
    tic_board = board()
    display(tic_board)
    count = 1
    full = full_check(tic_board)
    won_game = False
    while full == False:
        
        if count == 1 and won_game == False:
            print("\nPlayer 1 turn: 'X'")
            mark = user_choice()
            tic_board = mark_board(tic_board,mark,count)
            display(tic_board)
            won_game = winner(tic_board)
            if won_game == True:
                print("\nPlayer One won")
                full =True
                continue
            count = player(count)
        else:
            print("\nPlayer 2 turn: 'O'")
            mark = user_choice()
            tic_board = mark_board(tic_board,mark,count)
            display(tic_board)
            won_game = winner(tic_board)
            if won_game == True:
                print("\nPlayer Two won")
                full =True
                continue
            count = player(count)


        full = full_check(tic_board)


    ns = input("Do you want to play again? Y or N: ")
    ns = ns.upper()


    if ns == 'Y':
        play_on = True
    if ns == 'N':
        play_on = False
    


