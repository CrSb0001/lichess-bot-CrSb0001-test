import chess
def get_material(board):
  pw = 90
  kw = 290
  bw = 350
  rw = 512
  qw = 1024
  kingw = 16384
  wp = len(board.pieces(chess.PAWN,chess.WHITE))
  wr = len(board.pieces(chess.ROOK,chess.WHITE))
  wk = len(board.pieces(chess.KNIGHT,chess.WHITE))
  wb = len(board.pieces(chess.BISHOP,chess.WHITE))
  wq = len(board.pieces(chess.QUEEN,chess.WHITE))
  wking = len(board.pieces(chess.KING,chess.WHITE))
  bp = len(board.pieces(chess.PAWN,chess.BLACK))
  br = len(board.pieces(chess.ROOK,chess.BLACK))
  bk = len(board.pieces(chess.KNIGHT,chess.BLACK))
  bb = len(board.pieces(chess.BISHOP,chess.BLACK))
  bq = len(board.pieces(chess.QUEEN,chess.BLACK))
  bking = len(board.pieces(chess.KING,chess.BLACK))
  wpw = wp * pw
  wrw = wr * rw
  wkw = wk * kw
  wbw = wb * bw
  wqw = wq * qw
  wkingw = wking * kingw
  bpw = bp * pw
  brw = br * rw
  bkw = bk * kw
  bbw = bb * bw
  bqw = bq * qw
  bkingw = bking * kingw
  white_material = wpw + wrw + wkw + wbw + wqw + wkingw
  black_material = bpw + brw + bkw + bbw + bqw + bkingw
  total_material = white_material + black_material
  return total_material
