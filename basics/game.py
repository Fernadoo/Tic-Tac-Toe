class Game(object):
	def __init__(self, board, players):
		super().__init__()
		self.board = board
		self.players = players

	def starts(self, visual=False):
		rounds = 0
		# if visual:
		# 	self.board.print_board()
		while not self.game_ends():
			if rounds % 2 == 0:
				player = self.players[0]
			else:
				player = self.players[1]
			x, y = player.play(self.board)
			self.board.move(player, x, y, visual=visual)
			rounds += 1
		
		if visual:
			if self.winner == 'TIE':
				print("Game ties!")
			else:
				print(f"Game ends! {self.players[self.winner].name} wins the game!")

	def game_ends(self):
		ret, winner = self.board.check_winner()
		self.winner = winner
		return ret
