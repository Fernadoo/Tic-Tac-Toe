import numpy as np

"""
 x|x|x    [[ 1 , 1 , 1 ],
 - - -    
 o|x|o  => [-1 , 1 ,-1 ],
 - - -    
  |o|o     [ 0 ,-1 ,-1 ]]
"""
PLAYERx = 0
PLAYERo = 1
TYPEx = 1
TYPEo = -1

class Board(object):
	"""docstring for Board"""
	def __init__(self):
		super().__init__()
		self.board = np.zeros(shape=(3,3))
		self.empty = 9

	def print_board(self):
		for i in range(3):
			# print('|', end='')
			for j in range(3):
				if self.board[i,j] == 0:
					print(' ', end='')
				elif self.board[i,j] == 1:
					print('x', end='')
				elif self.board[i,j] == -1:
					print('o', end='')
				if j < 2:
					print('|', end='')
				else:
					print()
			if i < 2:
				print('- - -')

	def state_hash(self):
		return str(self.board)

	def move(self, player, x, y, visual=False):
		self.board[x,y] = player.type
		self.empty -= 1
		if visual:
			self.print_board()
			print(f"{player.name} move [{x},{y}]!")
			print()

	def is_legal(self, x, y):
		if self.board[x,y] == 0:
			return True
		else:
			return False

	def check_winner(self):
		# Row cases
		if self.board[0,0] + self.board[0,1] + self.board[0,2] == 3:
			return True, PLAYERx
		elif self.board[0,0] + self.board[0,1] + self.board[0,2] == -3:
			return True, PLAYERo

		if self.board[1,0] + self.board[1,1] + self.board[1,2] == 3:
			return True, PLAYERx
		elif self.board[1,0] + self.board[1,1] + self.board[1,2] == -3:
			return True, PLAYERo

		if self.board[2,0] + self.board[2,1] + self.board[2,2] == 3:
			return True, PLAYERx
		elif self.board[2,0] + self.board[2,1] + self.board[2,2] == -3:
			return True, PLAYERo

		# Col cases
		if self.board[0,0] + self.board[1,0] + self.board[2,0] == 3:
			return True, PLAYERx
		elif self.board[0,0] + self.board[1,0] + self.board[2,0] == -3:
			return True, PLAYERo 

		if self.board[0,1] + self.board[1,1] + self.board[2,1] == 3:
			return True, PLAYERx
		elif self.board[0,1] + self.board[1,1] + self.board[2,1] == -3:
			return True, PLAYERo

		if self.board[0,2] + self.board[1,2] + self.board[2,2] == 3:
			return True, PLAYERx
		elif self.board[0,2] + self.board[1,2] + self.board[2,2] == -3:
			return True, PLAYERo

		# Diag cases
		if self.board[0,0] + self.board[1,1] + self.board[2,2] == 3:
			return True, PLAYERx
		elif self.board[0,0] + self.board[1,1] + self.board[2,2] == -3:
			return True, PLAYERo

		if self.board[0,2] + self.board[1,1] + self.board[2,0] == 3:
			return True, PLAYERx
		elif self.board[0,2] + self.board[1,1] + self.board[2,0] == -3:
			return True, PLAYERo

		# Tie
		if self.empty == 0:
			return True, 'TIE'

		# Going on
		return False, 'Go_on'
		



		
		