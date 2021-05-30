# 
# Tic-tac-toe (or noughts and crosses) is a simple strategy game in which two players take turns placing a mark on a 3x3 board, attempting to make a row, column, or diagonal of three with their mark. In this homework, we will use the tools we've covered in the past two weeks to create a tic-tac-toe simulator and evaluate basic winning strategies.
# 
# In the following exercises, we will learn to create a tic-tac-toe board, place markers on the board, evaluate if either player has won, and use this to simulate two basic strategies.
# 
# #### Instructions 
# 
# - For our tic-tac-toe board, we will use a numpy array with dimension 3 by 3. 
# - Make a function `create_board()` that creates such a board with the value of each cell set to the integer `0`.
# - Call `create_board()` and store it.
import numpy as np
import collections
import random 
random.seed(1)
def create_board():
    return np.zeros((3,3))

# 
# - Create a function `place(board, player, position)`, where:
#     - `player` is the current player (an integer 1 or 2).
#     - `position` is a tuple of length 2 specifying a desired location to place their marker.
#     -  function should only allow the current player to place a marker on the board (change the board position to their number) if that position is empty (zero).

def place(board, player, position):     
    if (board[position] == 0.0):
        board[position] = player

# - Create a function `possibilities(board)` that returns a list of all positions (tuples) on the board that are not occupied (0).

def possibilities(board):
    return np.where(board == 0)

# The next step is for the current player to place a marker among the available positions. we will select an available board position at random and place a marker there.
# 
# function `random_place(board, player)` that places a marker for the current player at random among all the available positions (those currently set to 0).
#     - Find possible placements with `possibilities(board)`.
#     - Select one possible placement at random using `random.choice(selection)`.

def random_place(board, player):
    possible_places = possibilities(board)
    possible_places_list = [(possible_places[0][i],possible_places[1][i]) for i in range(len(possible_places[0]))]
    if (len(possible_places_list) > 0):
        place(board, player, random.choice(possible_places_list))

# 
# In the next few exercises, we will make functions that check whether either player has won the game.
# 
# #### Instructions 
# - function `row_win(board, player)` that takes the player (integer) and determines if any row consists of only their marker. 
#     - Have it return `True` if this condition is met and `False` otherwise.

def row_win(board, player):
    for row in board:
        if (np.all(row == player)):
            return True
    return False

# #### Instructions 
# - function `col_win(board, player)` that takes the player (integer) and determines if any column consists of only their marker. 
#     - Have it return `True` if this condition is met and `False` otherwise.

def col_win(board, player):
    for col in board.T:
        if (np.all(col == player)):
            return True
    return False

# 
# function `diag_win(board, player)` that tests if either diagonal of the board consists of only their marker. Have it return `True` if this condition is met, and `False` otherwise.

def diag_win(board, player):

    if (np.all(np.diag(np.fliplr(board)) == player)):
        return True
    elif (np.all(np.diag(board) == player)):
        return True
    else:
        return False

# - function `evaluate(board)` that uses `row_win`, `col_win`, and `diag_win` functions for both players. If one of them has won, return that player's number. If the board is full but no one has won, return -1. Otherwise, return 0.

def evaluate(board):
    winner = 0
    for player in [2, 1]:
        # add your code here!
        if (row_win(board, player) or col_win(board, player) or diag_win(board, player)):
            return player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
# 
# - `create_board()`, `random_place(board, player)`, and `evaluate(board)` have been created in previous exercises. Create a function `play_game()` that:
#     - Creates a board.
#     - Alternates taking turns between two players (beginning with Player 1), placing a marker during each turn.
#     - Evaluates the board for a winner after each placement.
#     - Continues the game until one player wins (returning 1 or 2 to reflect the winning player), or the game is a draw (returning -1).
# - Call play_game 1000 times, and store the results of the game in a list called `results`.

def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                return winner
    return winner


# #### Instructions 
# - Create a function `play_strategic_game()`, where Player 1 always starts with the middle square, and otherwise both players place their markers randomly.
# - Call `play_strategic_game` 1000 times.

def play_strategic_game():
    board = create_board()
    winner = 0
    board[(1,1)] = 1
    while winner == 0:
        for player in [2, 1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                return winner
    return winner


def main():
	results = list()
	for i in range(1000):
		results.append(play_game())
		#results.append(play_strategic_game()) 

	print (collections.Counter(results))

if __name__ == "__main__":
    main()
	





