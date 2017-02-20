class Figure(): 
	board = None
	position = -1 # -1 if not placed
	attacked_cells = set()
	
	def __init__(self, _board):
		self.board = _board;
		
	def put_on_board(self, _position):
		self.position = _position
		self.get_attacked_cells()
		
	def get_attacked_cells(self):
		pass