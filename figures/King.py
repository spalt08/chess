from Figure import Figure

class King(Figure):
	def get_attacked_cells(self):
		(y, x) = self.board.decode_position(self.position)
		
		if(y >= 0):
			self.attacked_cells.add(self.board.encode_position(y - 1, x))
		if(y < self.board.n):
			self.attacked_cells.add(self.board.encode_position(y + 1, x))
		if(x >= 0):
			self.attacked_cells.add(self.board.encode_position(y, x - 1))				
		if(x < self.board.n):
			self.attacked_cells.add(self.board.encode_position(y, x + 1))
			
		self.attacked_cells.add(self.board.encode_position(y, x)) # position cell