from Board import Board

class BoardCombinator():
	pieces = []
	depth = 0
	board = None
	i = 0
	is_founded = False
	
	def __init__(self, _board):
		self.board = _board
		
	def start(self):
		self.depth = len(self.pieces) - 1
		i = 0

		# for each cell try to place a first figure
		self.step(i, self.board.cells)
	
	def can_be_placed(self, i, cells_free, first_cell):
		can_be_placed = False
			
		for pos in cells_free:
			if (pos < first_cell):
				continue
				
			self.pieces[i].calculate(pos) 
			
			can_be_placed = not any(self.pieces[previous].is_hit_by(self.pieces[i]) for previous in range(0, i))
			
			if can_be_placed: 
				break
				
		if (not can_be_placed):
			self.pieces[i].calculate(-1)
			
		return can_be_placed
				
	def step(self, i, cells_free):	
		if(not self.is_founded):
			piece = self.pieces[i]
				
			for first_cell in cells_free:
				if (self.can_be_placed(i, cells_free, first_cell)):
					
					if(i == self.depth):
						v_board = Board()
						for piece in self.pieces:
							v_board.place_figure(piece)
						print('vboard')
						v_board.render()

					if(self.depth == i):
						self.is_founded = True
						
					else:
						self.step(i + 1, cells_free - piece.attacked_cells)
		