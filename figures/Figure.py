class Figure(): 
	board = None
	position = -1 # -1 if not placed
	attacked_cells = set()
	code = "X"
	
	def __init__(self, _board):
		self.board = _board;
		
	def calculate(self, _position):
		self.position = _position
		self.get_attacked_cells()
	
	def is_hit_by(self, figure):
		return (self.position in figure.attacked_cells)
	
	def get_attacked_cells(self):
		pass