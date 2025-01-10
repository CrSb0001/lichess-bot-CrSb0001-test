import pandas as pd
import chess
import chess.pgn
import random
import os
def play_opening(board):
    next_opening_moves = [];
    if board.turn == chess.WHITE and board.fullmove_number == 1:
        next_opening_moves.append("e2e4")
    new_board = chess.Board()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'openings.csv')
    chess_openings = pd.read_csv(file_path)
    chess_openings = chess_openings["moves"].tolist()
    for opening in chess_openings:
        moves_in_openings = opening.split();
        for index, move in enumerate(moves_in_openings):
            try:
                new_board.push_san(move)
                if board == new_board:
                    next_move = board.parse_san(moves_in_openings[index + 1]).uci()
                    next_opening_moves.append(next_move)
            except:
                break;
        new_board.reset()
    if not next_opening_moves:
        return None
    random_opening_from_array = random.choice(next_opening_moves)
    return random_opening_from_array
