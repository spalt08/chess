import argparse
from Board import Board
from Figures import FigureManager
from BoardCombinator import BoardCombinator

# CMD input
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--knights", type=int, default=0, help="Knights count")
parser.add_argument("-k", "--kings", type=int, default=0, help="Kings count")
parser.add_argument("-q", "--queens", type=int, default=0, help="Queens count")
parser.add_argument("-b", "--bishops", type=int, default=0, help="Bishops count")
parser.add_argument("-r", "--rooks", type=int, default=0, help="Rookes count")
args = parser.parse_args()

# Main
board = Board();
pieces_catalog = FigureManager(board)

pieces_input = []
for i in range(0, 8):
	pieces_input.append(pieces_catalog.make("Q"));
	
# make
handle = BoardCombinator(board)
handle.pieces = pieces_input
handle.start()

# debug stuff 

# fig = pieces.make("N", 35);
# board.draw_figure(fig) 

# tests = [0, 1, 5, 8, 9, 15, 16, 18]
# for pos in tests:
# 	(x, y) = board.decode_position(pos);
# 	print(x, y, board.encode_position(x,y))