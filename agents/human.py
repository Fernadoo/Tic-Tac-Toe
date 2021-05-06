class HumanPlayer():
	def __init__(self, name, play_type):
		super().__init__()
		self.name = name
		self.type = play_type

	def play(self, board):
		x = int(input("Choose the row: "))
		y = int(input("Choose the col: "))
		return x, y