from Figure import Figure

class Queen(Figure):
	def get_attacked_cells(self):
		(y, x) = self.board.decode_position(self.position)
		
		for i in range(0, self.board.n):
			left = x - abs(i - y)
			right = x + abs(i - y)
			
			self.attacked_cells.add(self.board.encode_position(i, x))
			self.attacked_cells.add(self.board.encode_position(y, i))
			
			if (left >= 0):
				self.attacked_cells.add(self.board.encode_position(i, left))
			if (right < self.board.n):
				self.attacked_cells.add(self.board.encode_position(i, right))