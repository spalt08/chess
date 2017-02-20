from Figure import Figure

class Rook(Figure):
	code = "R"
	
	def get_attacked_cells(self):
		self.attacked_cells = set()
		
		if(self.position >= 0):
			(y, x) = self.board.decode_position(self.position)
			
			for i in range(0, self.board.n):
				self.attacked_cells.add(self.board.encode_position(i, x))
				self.attacked_cells.add(self.board.encode_position(y, i))