from Figures import Figure

class Bishop(Figure):
	code = "B"
	
	def get_attacked_cells(self):
		self.attacked_cells = set()
		
		if(self.position >= 0):
			(y, x) = self.board.decode_position(self.position)
			
			for i in range(0, self.board.n):
				left = x - abs(i - y)
				right = x + abs(i - y)
				
				if (left >= 0):
					self.attacked_cells.add(self.board.encode_position(i, left))
				if (right < self.board.n):
					self.attacked_cells.add(self.board.encode_position(i, right))