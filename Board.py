class Board:
	n = 0
	cells_count = 0
	cells = None
	cells_free = None
	cells_booked = None
	cells_placed = None
	figures_placed = None
	
	def __init__(self, _n = 8):
		self.n = _n
		self.cells_count = self.n**2;
		self.cells = set(range(0, self.cells_count))
		self.cells_free = self.cells
		self.cells_booked = set()
		self.cells_placed = set()
		self.figures_placed = set()
		 
	def place_figure(self, figure):
		self.figures_placed.add(figure)
		
		self.cells_booked = self.cells_booked | figure.attacked_cells
		self.cells_free = self.cells_free - figure.attacked_cells
		self.cells_placed.add(figure.position)
	
	def encode_position(self, y, x):
		return y * self.n + x;
	
	def decode_position(self, position):
		y = int(position / self.n);
		x = position - self.n * y;
		return y, x;
		
	def render_figure(self, figure):
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
			
	def render(self):
		flist = {}
		
		for figure in self.figures_placed:
			flist[figure.position] = figure.code
			
		for y in range(0, self.n):
			line = ""
			
			for x in range(0, self.n):
				pos = self.encode_position(y, x)
				if(flist.has_key(pos)):
					line += flist[pos] + " "
				else:
					line += "_ "
			
			print(line)
			