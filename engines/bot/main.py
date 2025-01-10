import chess
import numpy as np
from .opening import play_opening
from .minmax import minmax
def get_move(board, depth):
    opening_move = play_opening(board)
    if opening_move:
        print("PLAYING OPENING MOVE: ", opening_move)
        return opening_move
    top_move = None;
    if board.turn == chess.WHITE:
      top_eval = -np.inf
    else:
      top_eval = np.inf
    for move in board.legal_moves:
        board.push(move)
        eval = minmax(board, depth - 1, -np.inf, np.inf, board.turn)
        board.pop()
        if board.turn == chess.WHITE:
            if eval > top_eval:
                top_move = move
                top_eval = eval
        else:
            if eval < top_eval:
                top_move = move
                top_eval = eval
    print("CHOSEN MOVE: ", top_move, "WITH EVAL: ", top_eval)
    return top_move
