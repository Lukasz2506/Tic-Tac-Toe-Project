# PROJECT FROM THE PYTHON BIBLE COURSE, Ziyad Yehia: Tic Tac Toe Game, 
# Student Lukasz

print("\n -----------Tick Tack Toe GaMe------------- \n")
#Board creating
board = [" " for i in range(9)]

def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()
    print(board)

print_board()

#Players define and marking choices on the board
print("enter your nickname!")
player_number_1 = input("Player number one...")
player_number_2 = input("Player number two...")

def player_move(icon):
    
    if icon == "X":
        player = player_number_1
    elif icon == "O":
        player = player_number_2

    print("Your turn player {}".format(player))
    
    choice = int(input("enter your move (1-9): ").strip())
    if board[choice - 1] == " ":
       board[choice -1] = icon
    else:
        print()
        print("That field is taken!") 

#All of the winning conditions
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2]) == icon or \
       (board[3] == icon and board[4] == icon and board[5]== icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or\
       (board[0] == icon and board[3] == icon and board[6]) == icon or \
       (board[1] == icon and board[4] == icon and board[7]== icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8]== icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

#Draw define (no wins) 
def is_draw():
    if " " not in board:
        return True
    else:
        return False

# Loop the game
while True:
    
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins! Congrats!!! :)")
        break
    elif is_draw():
        print("Its a draw")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins! Congrats!!! :)")
        break
    elif is_draw():
        print("Its a draw")
        break
    print_board()
