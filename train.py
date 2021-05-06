import numpy as np
import pickle
from tqdm import tqdm
from copy import deepcopy
import sys

from basics.board import Board
from agents.tabularQ import TabularQPlayer

PLAYERx = 0
PLAYERo = 1
TYPEx = 1
TYPEo = -1

class Learning():
	def __init__(self, tolerance=1e-4, iteration=1000):
		self.tolerance = tolerance
		self.iteration = iteration

	def learning_by_playing(self):
		alpha = 0.9; gamma = 0.9; epsilon = 0.2
		last_Q0 = dict()
		last_Q1 = dict()

		print("Start learning...")
		for i in tqdm(range(self.iteration)):
			prev_Q0 = deepcopy(last_Q0)
			prev_Q1 = deepcopy(last_Q1)

			p0 = TabularQPlayer("TPQ0", TYPEx, alpha=alpha, gamma=gamma, epsilon=epsilon, from_last_Q=last_Q0, load_Q=False)
			p1 = TabularQPlayer("TPQ1", TYPEo, alpha=alpha, gamma=gamma, epsilon=epsilon, from_last_Q=last_Q1, load_Q=False)
			board = Board()
			players = [p0, p1]

			rounds = 0
			while not self.game_ends(board):
				# print(rounds)
				if rounds % 2 == 0:
					player = players[0]
				else:
					player = players[1]
				x, y = player.play(board)
				board.move(player, x, y, visual=False)
				rounds += 1

			last_Q0 = deepcopy(p0.Q)
			last_Q1 = deepcopy(p1.Q)

			# if self.loss(prev_Q0, last_Q0) < self.tolerance:
			# 	print(f"Loss: {self.loss(prev_Q0, last_Q0)} => Already converges!")
			# 	break

		print("Finish learning!")

		# Save Q values
		with open(f"pickles/TPQ_{alpha}_{gamma}_{epsilon}_{self.iteration}.pkl", "wb") as f:
			pickle.dump(last_Q0, f)
		# print(last_Q0)
		print("Q value saved, ready for play!")

	def game_ends(self, board):
		return board.check_winner()[0]

	# Not used yet
	def loss(self, Q1, Q2):
		if Q1 == {}:
			return 999

		q1_avg = np.zeros(9); q1_cnt = 0
		for state in Q1:
			q1_avg += Q1[state]
			q1_cnt += 1
		q1_avg = np.sum(q1_avg / q1_cnt)

		q2_avg = np.zeros(9); q2_cnt = 0
		for state in Q2:
			q2_avg += Q2[state]
			q2_cnt += 1
		q2_avg = np.sum(q2_avg / q2_cnt)

		return np.abs(q1_avg - q2_avg)
		

if __name__ == '__main__':
	num_it = int(sys.argv[1])
	learning = Learning(iteration=num_it)
	learning.learning_by_playing()
