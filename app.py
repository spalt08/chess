import argparse
from Board import Board
from Figures import FigureManager
from BoardCombinator import BoardCombinator

# CMD options
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, default=None, help="Input Filename")
parser.add_argument("-o", "--output", help="Output filename", type=str, default=None)
args = parser.parse_args()
args_input = []

# File Input
file = open((args.input if args.input else 'input.txt'), 'r')
mode = file.readline()

for line in file:
	litera = line.split(" ")[0]
	count = int(line.split(" ")[1])
	args_input += [litera] * count	

# Main
board = Board();
pieces_catalog = FigureManager(board)
pieces_input = []

for letter in args_input:
	pieces_input.append(pieces_catalog.make(letter));
	
# Start Calculation
handle = BoardCombinator(board)
handle.pieces = pieces_input
handle.start()

# Get Results
if(handle.has_results):
	str_figures = handle.board.encode_figures() 
	str_placement = handle.board.render(True) 
	
	with open((args.output if args.output else 'output.txt'), "w") as context:
		context.write(str_figures)
		context.write("\n")
		context.write("\n")
		context.write(str_placement)
else:
	with open((args.output if args.output else 'output.txt'), "w") as context:
		context.write("No any corrent placement")
        