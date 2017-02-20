from Figure import Figure

class Knight(Figure):
	code = "N"
	
	def get_attacked_cells(self):
		self.attacked_cells = set()
		
		if(self.position >= 0):
			(y, x) = self.board.decode_position(self.position)
	
			if(y - 2 >= 0):
				if(x - 1 >= 0):
					self.attacked_cells.add(self.board.encode_position(y - 2, x - 1)) 
				if(x + 1 < self.board.n):
					self.attacked_cells.add(self.board.encode_position(y - 2, x + 1)) 
			if(y - 1 >= 0):
				if(x - 2 >= 0):
					self.attacked_cells.add(self.board.encode_position(y - 1, x - 2)) 
				if(x + 2 < self.board.n):
					self.attacked_cells.add(self.board.encode_position(y - 1, x + 2)) 
			if(y + 2 >= 0):
				if(x - 1 >= 0):
					self.attacked_cells.add(self.board.encode_position(y + 2, x - 1)) 
				if(x + 1 < self.board.n):
					self.attacked_cells.add(self.board.encode_position(y + 2, x + 1)) 
			if(y + 1 >= 0):
				if(x - 2 >= 0):
					self.attacked_cells.add(self.board.encode_position(y + 1, x - 2)) 
				if(x + 2 < self.board.n):
					self.attacked_cells.add(self.board.encode_position(y + 1, x + 2)) 
					
			self.attacked_cells.add(self.board.encode_position(y, x)) # position cell