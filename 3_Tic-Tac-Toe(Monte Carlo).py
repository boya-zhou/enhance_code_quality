"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 5         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

#board = provided.TTTBoard(3)
#player = provided.PLAYERX
#scores = [[0 for _ in range(board.get_dim())] for _ in range(board.get_dim())]

# Add your functions here.
def mc_update_scores(scores, board, player):
    '''
    If the current player (the player for which your code 
    is currently selecting a move) won the game, each square 
    that matches the current player should get a positive score
    '''
    ## check if player is the winner
    winner = board.check_win()
    if winner == provided.DRAW:
        pass
    elif winner == player:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == player:
                    scores[row][col] += SCORE_CURRENT
                elif board.square(row, col) == provided.switch_player(player):
                    scores[row][col] -= SCORE_OTHER
    else:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == player:
                    scores[row][col] -= SCORE_CURRENT
                elif board.square(row, col) == provided.switch_player(player):
                    scores[row][col] += SCORE_OTHER                 
    return scores

def get_best_move(board, scores):
    # find empty location
    empty_locations = board.get_empty_squares()
    empty_location_scores = []
    if len(empty_locations) != 0:
        for location in empty_locations:
            empty_location_scores.append(scores[location[0]][location[1]])
            max_score = max(set(empty_location_scores))
            index = empty_location_scores.index(max_score)
        return empty_locations[index]
    else:
        return None

def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    It then plays a game starting with the given player by making
    random moves, alternating between players. The function returns when
    the game is over. The modified board contains the state of the game,
    so the function does not return anything.
    """    
    while board.check_win() == None:
        empty_squares = board.get_empty_squares()
        random_square = random.choice(empty_squares)
        board.move(random_square[0], random_square[1], player)
        player = provided.switch_player(player)

def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is,
    and the number of trials to run. It then use the mc_trial() Monte Carlo
    simulation above to return a move for the machine player in the form of
    a (row, column) tuple.
    """   
    # initial empty scores list
    dim = board.get_dim()    
    scores = [[0 for dummycol in range(dim)] 
              for dummyrow in range(dim)]
    
    # simulate n number of trials
    for _ in range(trials):
        trial = board.clone()
        mc_trial(trial, player)
        #update the scores list after every trial
        mc_update_scores(scores, trial, player)
        
    return get_best_move(board, scores)        
        
'''
def mc_trial(board, player):
    player_current = player
    for order in range(board.get_dim()**2):
        if board.check_win() is None:             
            if order% 2 == 0:
                location = get_best_move(board, scores)
                player_current = provided.PLAYERX
                board.move(location[0], location[1], provided.PLAYERX)
            else:
                location = random.choice(board.get_empty_squares())
                player_current = provided.PLAYERO
                board.move(location[0], location[1], provided.PLAYERO)
            print str(board)
        else:
            break
    mc_update_scores(scores, board, player_current)
    print scores       
        
def mc_move(board, player, trial):
    for single_trial in range(trial):
        mc_trial(board, player)
        board = provided.TTTBoard(3)
        player = provided.switch_player(player)

mc_move(board, player, NTRIALS)

'''        
# Test game with the console or the GU I. Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
