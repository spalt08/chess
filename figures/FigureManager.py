from figures import Bishop, King, Knight, Queen, Rook 

class FigureManager():
	board = None
	
	def __init__(self, _board):
		self.board = _board;
	
	def make(self, code, position = 0):
		figure = None
		
		if(code == "B"):
			figure = Bishop(self.board)
		elif(code == "K"):
			figure = King(self.board)
		elif(code == "N"):
			figure = Knight(self.board)
		elif(code == "Q"):
			figure = Queen(self.board)
		else: 
			return Rook(self.board)
			
		figure.put_on_board(position)
		
		return figure