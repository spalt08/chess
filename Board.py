class Board:
	n = 0;
	cells_count = 0;
	
	def __init__(self, _n = 8):
		self.n = _n;
		self.cellsCount = _n**2;
		
	def encode_position(self, y, x):
		return y * self.n + x;
	
	def decode_position(self, position):
		y = int(position / self.n);
		x = position - self.n * y;
		return y, x;
		
	def draw_figure(self, figure):
		for x in range(0, self.n):
			line = ""
			
			for y in range(0, self.n):
				position = self.encode_position(y, x)
				
				if(position == figure.position):
					line += "X ";
				
				elif(position in figure.attacked_cells):
					line += "1 ";
					
				else: 
					line += "0 ";
			
			print(line)
			
		print(figure.attacked_cells) 