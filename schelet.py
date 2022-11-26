import random, math
from functools import reduce
from copy import *
from builtins import isinstance
# from resource import setrlimit, RLIMIT_AS, RLIMIT_DATA
from heapq import *
import sys
import time


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

	# @staticmethod
	# def line_conflict( i, line, dest):
	# 	conflicts = 0
	# 	conflict_graph = {}
	# 	for j, u in enumerate(line):
	# 		if u == 0:
	# 			continue
	# 		x, y = dest(u)
	# 		if i != x:
	# 			continue

	# 		for k in range(j + 1, self.n):
	# 			# opposing tile
	# 			v = line[k]
	# 			if v == 0:
	# 				continue
	# 			tx, ty = dest(v)
	# 			if tx == x and ty <= y:
	# 				u_degree, u_nbrs = conflict_graph.get(u) or (0, set())
	# 				u_nbrs.add(v)
	# 				conflict_graph[u] = (u_degree + 1, u_nbrs)
	# 				v_degree, v_nbrs = conflict_graph.get(v) or (0, set())
	# 				v_nbrs.add(u)
	# 				conflict_graph[v] = (v_degree + 1, v_nbrs)
	# 	while sum([v[0] for v in conflict_graph.values()]) > 0:
	# 		popped = max(conflict_graph.keys(),key=lambda k: conflict_graph[k][0])
	# 		for neighbour in conflict_graph[popped][1]:
	# 			degree, vs = conflict_graph[neighbour]
	# 			vs.remove(popped)
	# 			conflict_graph[neighbour] = (degree - 1, vs)
	# 			conflicts += 1
	# 		conflict_graph.pop(popped)
		
	# 	return conflicts

	# @staticmethod
	# def row_dest(v):
	# 	return )
	
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


#########################################################################################################

'''
0 inseamna vecinul de sus
1 inseamna vecinul de jos
2 inseamna vecinul din stanga
3 inseamna vecinul din dreapta

'''
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
		last_len = len(discovered)

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

			if node.r == node.solved().r:
				print("FOUND A SOLUTION",current_g)
				found_solution = True
				return current_g,len(discovered)

			for neigh in node.get_neighbours():
				neigh_g = current_g + 1
				
				if neigh not in discovered or neigh_g < discovered[neigh][1]:
					discovered[neigh] = (node, neigh_g)
					heappush(frontier, (neigh_g + neigh.evaluate_state(h), neigh))
            
			if last_len == len(discovered):
				print("GROAPA")
				# return -2,-2
				break

		if not found_solution:
			print("Couldn't find solution")
			return -1,-1


class BeamSearch:
	
	def __init__(self) -> None:
		pass
	## pune start time si end time sa isi dea singur break din if
	def solve(self,n_puzzle,B,h,start_time):
		discovered = {n_puzzle: (n_puzzle.evaluate_state(h),None)} ## closed
		beam = []
		## beam : score, node , parent
		beam += [(n_puzzle.evaluate_state(h), n_puzzle, None)]
		
		found_solution = False
		depth = 0

		while beam:
			last_len = len(discovered)
			
			end = time.time()

			if end - start_time > 30:
				# print("Time limit exceded")
				return -7,-7

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

							# print("Found solution")
							return len(neigh.moves),len(discovered)
					

			selected = []
			# if len(all_neighbours) == 0:
			# 	print('aaa')
			
			i = 0
			while i < min(B,len(all_neighbours)):
				(score,node,parent) = heappop(all_neighbours)
				if node not in discovered:
					# print(score)
					selected += [(score,node,parent)]
					discovered[node] = (score,parent)
					i+=1
				else:
					# print("here",i)
					continue


			beam = selected 

			## groapa
			if last_len == len(discovered):
				# print("GROAPA")
				break


		if not found_solution:
			# print("Couldn't find solution")
			return -1,-1


class GLDS:
	
	def __init__(self) -> None:
		pass

	def solve(self,start,h,limit,discrepancy_limit):
		discovered = {start: (start.evaluate_state(h),None)} ## closed
		discrepancy = 0
		total_no_states = 0
		start_time = time.time()

		while discrepancy < discrepancy_limit:
			# print("Discrepancy",discrepancy)
			tbr = self.iteration(start,discrepancy,h,discovered,limit,time.time())

			if tbr == "MEM | TLE":
				return "MEM | TLE"
			
			if isinstance(tbr,int):
				total_no_states += tbr

				if total_no_states > limit:
					return "MEM"
				
				discrepancy += 1
				continue

			return (tbr[0],tbr[1])

	def iteration(self,state,discrepancy,h,discovered,limit,start_time):
		succ = []
		for neigh in state.get_neighbours():
			if neigh.r == neigh.solved().r:
				# print("SOLUTION DISCOVERED")
				discovered[neigh] = (neigh.evaluate_state(h),state)
				return (1, len(succ) + 1)

			if neigh not in discovered:
				## (score,node,parent)
				heappush(succ,(neigh.evaluate_state(h),neigh,state))
		
		
		if len(succ) == 0:
			# print("SUCC IS EMPTY")
			return 0

		if len(discovered) > limit:
			# print("OVER THE LIMIT")
			return "MEM | TLE"
		
		score,best_node,best_parent = heappop(succ)

		if discrepancy == 0:
			discovered[best_node] = (score,state)
			tbr = self.iteration(best_node,0,h,discovered,limit,start_time)
			discovered.pop(best_node)

			if tbr == "MEM | TLE":
				return "MEM | TLE"
			
			if isinstance(tbr,int):
				return len(succ) + tbr + 1

			return (tbr[0] + 1,tbr[1] + 1 + len(succ))
			
		else:
			no_states = 0
			initial_len = len(succ)	
			while len(succ) > 0:

				if time.time() - start_time > 40:
					return "MEM | TLE"

				next_score,next_best_node,next_best_parent = heappop(succ)
				
				discovered[next_best_node] = (next_score,state)
				tbr = self.iteration(next_best_node,discrepancy-1,h,discovered,limit,start_time)
				discovered.pop(next_best_node)

				if isinstance(tbr,int):
					no_states += tbr
					continue

				if tbr == "MEM | TLE":
					return "MEM | TLE"

				return (tbr[0] + 1,tbr[1] + initial_len + no_states)
				
				

			discovered[best_node] = (score,state)
			tbr = self.iteration(best_node,discrepancy,h,discovered,limit,start_time)
			discovered.pop(best_node)
			

			if tbr == "MEM | TLE":
				return "MEM | TLE"

			if isinstance(tbr,int):
				return tbr + no_states + initial_len
			

			return (tbr[0] + 1, tbr[1] + initial_len + no_states)



## TODO: vezi sa aduni bine numarul de stari si de pasi
class BLDS:

	def __init__(self) -> None:
		pass

	def solve(self,start,h,B,limit):
		visited = {start: (start.evaluate_state(h),None)}
		discrepancy = 0
		total_no_states = 0
		while True:
			tbr = self.iteration([(start.evaluate_state(h),start,None)],discrepancy,B,h,visited,limit,time.time())
			if tbr == "MEM | TLE":
				return "MEM | TLE"
			
			if isinstance(tbr,int):
				total_no_states += tbr

				if total_no_states > limit:
					return "MEM"
				
				discrepancy += 1
				continue

			return (tbr[0],tbr[1])


	def iteration(self,level,discrepancy,B,h,visited,limit,start_time):
		succ = []
		for score,s,parent in level:
			for neigh in s.get_neighbours():
				if neigh.r == neigh.solved().r:
					visited[neigh] = (neigh.evaluate_state(h),s)
					return (1,len(succ) + 1)
				if neigh not in visited:
					heappush(succ,(neigh.evaluate_state(h),neigh,s))

		if len(succ) == 0:
			return 0

		if len(visited) + min(B,len(succ)) > limit:
			return "MEM | TLE"

		if discrepancy == 0:
			new_level = []

			## aici trebuie doar scoase
			i = 0
			while i < min(B,len(succ)):
				(score,node,parent) = heappop(succ)
				if node not in visited:
					# heappush(new_level,(score,node,parent))
					new_level += [(score,node,parent)]
					visited[node] = (score,parent)	
					i+=1
				else:
					continue	

				
			tbr = self.iteration(new_level,0,B,h,visited,limit,start_time)
			
			for score,node,parent in new_level:
				visited.pop(node)

			## returns

			if tbr == "MEM | TLE":
				return tbr

			if isinstance(tbr,int):
				return len(succ) + tbr + 1

			return (tbr[0] + 1,tbr[1] + 1 + len(succ))
		
		else:
			already_explored = B
			no_states = 0
			while already_explored < len(succ):

				if time.time() - start_time > 40:
					return "MEM | TLE"

				## aici e bine
				n = min(len(succ) - already_explored,B)
				nivel_urm = nsmallest(succ,already_explored + n)[n:]

				for score,node,parent in nivel_urm:
					visited[node] = (score,parent)

				tbr = self.iteration(nivel_urm,discrepancy - 1,B,h,visited,limit,start_time)

				for score,node,parent in nivel_urm:
					visited.pop(node)

				if isinstance(tbr,tuple):
					## aici nu stiu daca e len de succ
					return (tbr[0] + 1,tbr[1] + 1 + len(succ))

				already_explored += len(nivel_urm)
			


			## doar scoase aici
			new_level = []

			## aici trebuie doar scoase
			i = 0
			while i < min(B,len(succ)):
				(score,node,parent) = heappop(succ)
				if node not in visited:
					# heappush(new_level,(score,node,parent))
					new_level += [(score,node,parent)]
					visited[node] = (score,parent)	
					i+=1
				else:
					continue	

			for score,node,parent in new_level:
				visited[node] = (score,parent)

			tbr = self.iteration(new_level,discrepancy,B,h,visited,limit,start_time)

			for score,node,parent in new_level:
				visited.pop(node)

			## returns

			if isinstance(tbr,tuple):
				## aici nu stiu daca e len de succ
				return (tbr[0] + 1,tbr[1] + 1 + len(succ))

			if isinstance(tbr,int):
				tbr + 1 + len(succ)

			if tbr == "MEM | TLE":
				return tbr
					

				
				
			
			
		