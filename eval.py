import sys

from agents.tabularQ import TabularQPlayer
from agents.human import HumanPlayer
from basics.board import Board
from basics.game import Game

PLAYERx = 0
PLAYERo = 1
TYPEx = 1
TYPEo = -1

if __name__ == '__main__':
	num_it = sys.argv[1]
	Q_pkl = f"pickles/TPQ_0.9_0.9_0.2_{num_it}.pkl"
	
	p0 = TabularQPlayer("TPQ", TYPEx, alpha=0.9, gamma=0.9, epsilon=0.2, from_last_Q=None, load_Q=Q_pkl)
	p1 = HumanPlayer("Fernando", TYPEo)

	board = Board()
	game = Game(board, [p0, p1])

	game.starts(visual=True)