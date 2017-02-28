from Board import Board

class BoardCombinator():
	pieces = []
	depth = 0
	board = None
	i = 0
	has_results = False
	
	def __init__(self, _board):
		self.board = _board
		
	def start(self, mode = "free_cells"):
		self.depth = len(self.pieces) - 1
		i = 0
		
		if(mode == "all_cells"):
			self.step_all_cells(i, self.board.cells, self.board.cells)
		else:
			self.step(i, self.board.cells)
	
	#######
	
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
		j = 0;
		piece = self.pieces[i]
		
		while not self.has_results and j < len(cells_free):
			first_cell = list(cells_free)[j];
			
			if (self.can_be_placed(i, cells_free, first_cell)):
	
				if(self.depth == i):
					self.has_results = True
					self.board = Board()
					
					for piece in self.pieces:
						self.board.place_figure(piece)
					
				else:
					self.step(i + 1, cells_free - piece.attacked_cells)

			j += 1;
		
	#######
	
	def can_be_placed_all_cells(self, i, cells_free, first_cell, cells_empty):
		can_be_placed = False
			
		for pos in cells_empty:
			if (pos < first_cell):
				continue
				
			self.pieces[i].calculate(pos) 
			
			can_be_placed = self.pieces[i].position in cells_empty
			
			if can_be_placed: 
				break
				
		if (not can_be_placed):
			self.pieces[i].calculate(-1)
			
		return can_be_placed
			
	def step_all_cells(self, i, cells_free, cells_empty):
		
		if(not self.is_founded and i <= self.depth):
			piece = self.pieces[i]
				
			for first_cell in cells_empty:
				if (self.can_be_placed_all_cells(i, cells_free, first_cell, cells_empty)):
					
					if(i == self.depth and cells_free == False):
						v_board = Board()
						for piece in self.pieces: 
							v_board.place_figure(piece)
						print('vboard', i, cells_free)
						v_board.render()

					if(self.depth == i and cells_free == False):
						self.is_founded = True 
						
					else:
						self.step_all_cells(i + 1, cells_free - piece.attacked_cells, cells_empty - set([piece.position]))