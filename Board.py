class Board:
	n = 0;
	cells_count = 0;
	
	def __init__(self, _n = 8):
		self.n = _n;
		self.cellsCount = _n**2;
		
	def encode_position(self, x, y):
		return x * self.n + y;
	
	def decode_position(self, position):
		x = int(position / self.n);
		y = position - self.n * x;
		return x, y;
		
	def draw_figure(self, figure):
		for x in range(0, self.n):
			line = ""
			
			for y in range(0, self.n):
				position = self.encode_position(x, y)
				
				if(position == figure.position):
					line += "X ";
				
				else: 
					line += "0 ";
			
			print(line)
			
		print(figure.attacked_cells)