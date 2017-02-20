from Figure import Figure

class King(Figure):
	code = "K"
	
	def get_attacked_cells(self):
		self.attacked_cells = set()
		
		if(self.position >= 0):
			(y, x) = self.board.decode_position(self.position)
			
			from_y = max(0, y - 1)
			from_x = max(0, x - 1)
			to_y = min(self.board.n - 1, y + 1)
			to_x = min(self.board.n - 1, x + 1)

			for y in range(from_y, to_y + 1):
				for x in range(from_x, to_x + 1):
					self.attacked_cells.add(self.board.encode_position(y, x))