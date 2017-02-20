from Figures import Bishop, King, Knight, Queen, Rook 

class FigureManager():
	board = None
	
	def __init__(self, _board):
		self.board = _board;
	
	def make(self, code, position = -1):
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
			figure = Rook(self.board)
			
		if(position >= 0):
			figure.calculate(position)
		
		return figure