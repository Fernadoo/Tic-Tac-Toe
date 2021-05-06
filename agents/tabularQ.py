import pickle
import numpy as np
from copy import deepcopy

PLAYERx = 0
PLAYERo = 1
TYPEx = 1
TYPEo = -1

"""
Rewards:
	Win: 1, Lose:-1, Tie:2, Else:0 
"""

class TabularQPlayer():
	def __init__(self, name, play_type, alpha=0.9, gamma=0.9, epsilon=0.2, from_last_Q=None, load_Q=False):
		super().__init__()
		self.name = name
		self.type = play_type

		self.alpha = alpha
		self.gamma = gamma
		self.epsilon = epsilon
		self.Q = dict()
		if from_last_Q:
			self.Q = deepcopy(from_last_Q)

		self.load_Q = load_Q
		if load_Q:
			with open(load_Q, 'rb') as f:
				self.Q = pickle.load(f)
			print(f"Q value loaded from {load_Q}")

	def play(self, board):
		# Eval phase
		if self.load_Q:
			x, y = self.get_move_from_Q(board)
			return x, y
		
		# Training phase
		else:
			x, y = self.get_move_from_Q(board)
			self.update_Q_after_move(x, y, board)
			# print(self.Q)
			return x, y

	def get_move_from_Q(self, board):
		state = board.state_hash()
		if state not in self.Q:
			self.Q[state] = np.zeros(9)
		Q = deepcopy(self.Q)

		if self.load_Q:
			while True:
				action = np.argmax(Q[state])
				x, y = Idx2Coor(action)
				if board.is_legal(x, y):
					return x, y
				else:
					Q[state][action] = -999

		else:
			coin_flip = np.random.uniform(0,1)
			if coin_flip > self.epsilon:
				while True:
					action = np.argmax(Q[state])
					x, y = Idx2Coor(action)
					if board.is_legal(x, y):
						return x, y
					else:
						Q[state][action] = -999
			else:
				while True:
					action = np.random.randint(0,9)
					x, y = Idx2Coor(action)
					if board.is_legal(x, y):
						return x, y

	def update_Q_after_move(self, x, y, board):
		state = board.state_hash()
		action = Coor2Idx(x, y) 

		next_board = deepcopy(board)
		next_board.board[x, y] = self.type
		next_board.empty -= 1

		if self.reward(next_board) == 0:
			xo, yo = self.guess_opponent_move(next_board)
			next_board.board[xo, yo] = -self.type

		next_state = next_board.state_hash()
		if next_state not in self.Q:
			self.Q[next_state] = np.zeros(9)
		r = self.reward(next_board)

		self.Q[state][action] = (1 - self.alpha) * self.Q[state][action] \
								+ self.alpha * (r + self.gamma * np.max(self.Q[next_state])) 

	def reward(self, board):
		ret, winner = board.check_winner()
		if winner == 'Go_on':
			return 0
		elif winner == 'TIE':
			return 2
		elif (winner == PLAYERx and self.type == TYPEx) or (winner == PLAYERo and self.type == TYPEo):
			return 1
		else:
			return -1

	def guess_opponent_move(self, board):
		while True:
			action = np.random.randint(0,9)
			x, y = Idx2Coor(action)
			if board.is_legal(x, y):
				return x, y

"""
Helper functions
"""
def Coor2Idx(x, y):
	return 3 * x + y

def Idx2Coor(idx):
	return idx//3, idx%3
		