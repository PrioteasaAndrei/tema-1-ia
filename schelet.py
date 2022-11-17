import random, math
from functools import reduce
from copy import copy
from builtins import isinstance
# from resource import setrlimit, RLIMIT_AS, RLIMIT_DATA
from heapq import heappop, heappush
import sys

class NPuzzle:
	"""
	Reprezentarea unei stări a problemei și a istoriei mutărilor care au adus starea aici.
	
	Conține funcționalitate pentru
	- afișare
	- citirea unei stări dintr-o intrare pe o linie de text
	- obținerea sau ștergerea istoriei de mutări
	- obținerea variantei rezolvate a acestei probleme
	- verificarea dacă o listă de mutări fac ca această stare să devină rezolvată.
	"""

	NMOVES = 4
	UP, DOWN, LEFT, RIGHT = range(NMOVES)
	ACTIONS = [UP, DOWN, LEFT, RIGHT]
	names = "UP, DOWN, LEFT, RIGHT".split(", ")
	BLANK = ' '
	delta = dict(zip(ACTIONS, [(-1, 0), (1, 0), (0, -1), (0, 1)]))
	
	PAD = 2
	
	def __init__(self, puzzle : list[int | str], movesList : list[int] = []):
		"""
		Creează o stare nouă pe baza unei liste liniare de piese, care se copiază.
		
		Opțional, se poate copia și lista de mutări dată.
		"""
		self.N = len(puzzle)
		self.side = int(math.sqrt(self.N))
		self.r = copy(puzzle)
		self.moves = copy(movesList)
	
	def display(self, show = True) -> str:
		l = "-" * ((NPuzzle.PAD + 1) * self.side + 1)
		aslist = self.r
		
		slices = [aslist[ slice * self.side : (slice+1) * self.side ]  for slice in range(self.side)]
		s = ' |\n| '.join([' '.join([str(e).rjust(NPuzzle.PAD, ' ') for e in line]) for line in slices]) 
	
		s = ' ' + l + '\n| ' + s + ' |\n ' + l
		if show: print(s)
		return s
	def display_moves(self):
		print([names[a] if a is not None else None for a in moves])
		
	def print_line(self):
		return str(self.r)
	
	@staticmethod
	def read_from_line(line : str):
		list = line.strip('\n][').split(', ')
		numeric = [NPuzzle.BLANK if e == "' '" else int(e) for e in list]
		return NPuzzle(numeric)
	
	def clear_moves(self):
		"""Șterge istoria mutărilor pentru această stare."""
		self.moves.clear()

	
	def apply_move_inplace(self, move : int):
		"""Aplică o mutare, modificând această stare."""
		blankpos = self.r.index(NPuzzle.BLANK)
		y, x = blankpos // self.side, blankpos % self.side
		ny, nx = y + NPuzzle.delta[move][0], x + NPuzzle.delta[move][1]
		if ny < 0 or ny >= self.side or nx < 0 or nx >= self.side: return None
		newpos = ny * self.side + nx
		piece = self.r[newpos]
		self.r[blankpos] = piece
		self.r[newpos] = NPuzzle.BLANK
		self.moves.append(move)
		return self
	
	def apply_move(self, move : int):
		"""Construiește o nouă stare, rezultată în urma aplicării mutării date."""
		return self.clone().apply_move_inplace(move)

	def solved(self):
		"""Întoarce varianta rezolvată a unei probleme de aceeași dimensiune."""
		return NPuzzle(list(range(self.N))[1:] + [NPuzzle.BLANK])

	def verify_solved(self, moves : list[int]) -> bool:
		""""Verifică dacă aplicarea mutărilor date pe starea curentă duce la soluție"""
		return reduce(lambda s, m: s.apply_move_inplace(m), moves, self.clone()) == self.solved()

	def get_neighbours(self):
		tbr = []
		for i in NPuzzle.ACTIONS:
			a = self.apply_move(i)
			if a is not None:
				tbr += [a]
		
		return tbr

	def evaluate_state(self,heuristic):
		return heuristic(self.r,self.side)
	
	@staticmethod
	def manhattan_distance(board,N):
		## de modificat pt moss
		return sum(abs((val-1)%N - i%N) + abs((val-1)//N - i//N)
        		for i, val in enumerate(board) if val != " ")
	

	@staticmethod
	def num_inversions(board,N):
		numInversions = 0
		# print("N in inversion",N)
		for i in range(N*N - 1):
			for j in range(i+1,N*N):
				if board[i] == " " or board[j] == " ":
					continue
				if board[i] > board[j]:
					# print("inversion between",board[i],board[j])
					numInversions += 1

		return numInversions

	@staticmethod
	def manhattan_and_num_inversions(board,N):
		## posibil fara // 2
		return 2*NPuzzle.num_inversions(board,N) + NPuzzle.manhattan_distance(board,N)

	def clone(self):
		return NPuzzle(self.r, self.moves)
	def __str__(self) -> str:
		return str(self.N-1) + "-puzzle:" + str(self.r)
	def __repr__(self) -> str: return str(self)
	def __eq__(self, other):
		return self.r == other.r
	def __lt__(self, other):
		return True
	def __hash__(self):
		return hash(tuple(self.r))
	


# MLIMIT = 3 * 10 ** 9 # 2 GB RAM limit
# setrlimit(RLIMIT_DATA, (MLIMIT, MLIMIT))


# generare
def genOne(side, difficulty):
	state = NPuzzle(list(range(side * side))[1:] + [NPuzzle.BLANK])
	for i in range(side ** difficulty + random.choice(range(side ** (difficulty//2)))):
		s = state.apply_move(random.choice(NPuzzle.ACTIONS))
		if s is not None: state = s
	state.clear_moves()
	return state

# print("Generare:")
random.seed(4242)
# p = genOne(3, 4)
# p.display()

# p.r = [1,2,3,5," ",7,6,8,4]
# print("Original")
# p.display()
# print(p.verify_solved([]))
# print("After moves")
# for i in p.get_neighbours():
# 	i.display()
# print(p.evaluate_state(NPuzzle.manhatten_and_num_inversions))
# problemele easy au fost generate cu dificultatile 4, 3, respectiv 2 (pentru marimile 4, 5, 6)
# celelalte probleme au toate dificultate 6

#########################################################################################################

'''
0 inseamna vecinul de sus
1 inseamna vecinul de jos
2 inseamna vecinul din stanga
3 inseamna vecinul din dreapta

'''
## hash(str(.r)) pate
## pune doar pozita libera ca cheie
## limita dictionar
class AStar:
	
	def __init__(self) -> None:
		pass

	def get_dict_memory(self,discovered):
		size = sys.getsizeof(discovered)
		size += sum(map(sys.getsizeof, discovered.values())) + sum(map(sys.getsizeof, discovered.keys()))
		return size

	def solve(self,n_puzzle,h,verbose=False):
		discovered = {n_puzzle: (None, 0)} ## closed
		frontier = []
		heappush(frontier, (0 + n_puzzle.evaluate_state(h), n_puzzle))
		
		found_solution = False

		while frontier:

			if len(discovered) >= 100000 and n_puzzle.side == 4:
				found_solution = False
				break
			elif len(discovered) >= 500000 and n_puzzle.side == 5:
				found_solution = False
				break
			elif len(discovered) >= 1000000 and n_puzzle.side == 6:
				found_solution = False
				break

			(current_cost_f,node) = heappop(frontier)
			if verbose:
				print("Currently trying:",node.r)
			current_g = discovered[node][1]

			## or stop after certain number of steps
			## node.r == node.solved().r
			## node.verify_solved([]) == True
			if node.r == node.solved().r:
				print("FOUND A SOLUTION",current_g)
				found_solution = True
				return current_g,len(discovered)

			for neigh in node.get_neighbours():
				neigh_g = current_g + 1
				
				if neigh not in discovered or neigh_g < discovered[neigh][1]:
					discovered[neigh] = (node, neigh_g)
					heappush(frontier, (neigh_g + neigh.evaluate_state(h), neigh))
            

		if not found_solution:
			print("Couldn't find solution")


## TODO: Fix not working pt B = 1
## TODO: vezi de ce ce aia goala

class BeamSearch:
	
	def __init__(self) -> None:
		pass

	def solve(self,n_puzzle,B,h):
		discovered = {n_puzzle: (n_puzzle.evaluate_state(h),None)} ## closed
		beam = []
		## beam : score, node , parent
		beam += [(n_puzzle.evaluate_state(h), n_puzzle, None)]
		
		found_solution = False
		depth = 0

		while beam:

			if len(discovered) >= 100000 and n_puzzle.side == 4:
				found_solution = False
				break
			elif len(discovered) >= 500000 and n_puzzle.side == 5:
				found_solution = False
				break
			elif len(discovered) >= 1000000 and n_puzzle.side == 6:
				found_solution = False
				break

			all_neighbours = []
			for score,node,parent in beam:
				for neigh in node.get_neighbours():
					if neigh not in discovered:
						heappush(all_neighbours, (neigh.evaluate_state(h), neigh, node))
						if neigh.r == neigh.solved().r:

							print(n_puzzle.verify_solved(neigh.moves))

							found_solution = True
							discovered[neigh] = (neigh.evaluate_state(h),node)

							print("Found solution")
							return len(neigh.moves),len(discovered)

			selected = []
			if len(all_neighbours) == 0:
				print('aaa')
			
			for i in range(min(B,len(all_neighbours))):
				(score,node,parent) = heappop(all_neighbours)
				print(score)
				selected += [(score,node,parent)]
				discovered[node] = (score,parent)

			beam = selected 


		if not found_solution:
			print("Couldn't find solution")
			return -1,-1