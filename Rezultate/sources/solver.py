from schelet import *
import time
import sys
import numpy as np
import threading
print(sys.getrecursionlimit())
sys.setrecursionlimit(10 ** 7)
from stats import *
## 5 GB RAM
threading.stack_size(5242880)


f = open("files/problems4-easy.txt", "r")
input = f.readlines()
f.close()
problems_4_easy = [NPuzzle.read_from_line(line) for line in input]

f = open("files/problems5-easy.txt", "r")
input = f.readlines()
f.close()
problems_5_easy = [NPuzzle.read_from_line(line) for line in input]

f = open("files/problems6-easy.txt", "r")
input = f.readlines()
f.close()
problems_6_easy = [NPuzzle.read_from_line(line) for line in input]

f = open("files/problems4.txt", "r")
input = f.readlines()
f.close()
problems_4 = [NPuzzle.read_from_line(line) for line in input]

f = open("files/problems5.txt", "r")
input = f.readlines()
f.close()
problems_5 = [NPuzzle.read_from_line(line) for line in input]

f = open("files/problems6.txt", "r")
input = f.readlines()
f.close()
problems_6 = [NPuzzle.read_from_line(line) for line in input]

solver_A = AStar()
solver_B  = BeamSearch()
solver_G = GLDS()
solver_BLDS = BLDS()

should_work_GLDS = [problems_4_easy[0],problems_4_easy[1],problems_4_easy[2],problems_4_easy[3],problems_4_easy[4],problems_6_easy[0],problems_6_easy[2],problems_6_easy[3],problems_6_easy[4]]
should_work_GLDS += [problems_4[0],problems_4[2]]

def tests_can_apply_move():
    ht = HanoiTowers(4,['P' for i in range(4)])
    ht.r[0] = 'G'
    ht.r[1] = 'P'
    ht.r[2] = 'Q'
    ht.r[3] = 'R'

    print(ht.can_apply_move(0,'P'))
    print(ht.can_apply_move(0,'Q'))
    print(ht.can_apply_move(0,'R'))
    print(ht.can_apply_move(0,'G'))


    print("----------------------------------")

    ht.r[0] = 'Q'
    ht.r[1] = 'R'
    ht.r[2] = 'Q'
    ht.r[3] = 'G'

    print(ht.can_apply_move(0,'P')) ## True
    print(ht.can_apply_move(2,'P')) ## False
    print(ht.can_apply_move(3,'R')) ## False
    print(ht.can_apply_move(1,'Q')) ## False
 


    print("----------------------------------")

    ht.r[0] = 'G'
    ht.r[1] = 'R'
    ht.r[2] = 'R'
    ht.r[3] = 'P'
 
    print(ht.can_apply_move(2,'P')) ## False
    print(ht.can_apply_move(2,'G')) ## False
    print(ht.can_apply_move(0,'R')) ## True
    print(ht.can_apply_move(3,'Q')) ## True
    print(ht.can_apply_move(3,'G')) ## False
    print(ht.can_apply_move(2,'Q')) ## False
    print(ht.can_apply_move(1,'P')) ## True
    print(ht.can_apply_move(0,'P')) ## True
    print(ht.can_apply_move(3,'P')) ## False

def tests_can_move():
    ht = HanoiTowers(4,['P' for i in range(4)])

    ht.r[0] = 'G'
    ht.r[1] = 'R'
    ht.r[2] = 'R'
    ht.r[3] = 'P'

    ht.move(1,'Q').display()
    ht.move(0,'P').display()
    ht.move(1,'P').display()
    ht.move(0,'R').display()

    ht.move(1,'Q').move(2,'P').move(1,'P').move(0,'P').display()


def tests_get_neigh():
    ht = HanoiTowers(4,['P' for i in range(4)])

    ht.r[0] = 'Q'
    ht.r[1] = 'Q'
    ht.r[2] = 'P'
    ht.r[3] = 'P'

    for neigh in ht.get_neighbours():
        print(neigh.evaluate_state(HanoiTowers.heuristic2))
        neigh.display()


def tests_BLDS_hanoi(b):
    ht = HanoiTowers(4,['P' for i in range(4)])

    ht.r[0] = 'G'
    ht.r[1] = 'R'
    ht.r[2] = 'R'
    ht.r[3] = 'P'

    solver_BLDS = BLDS()
    print("4 Disks")
    print(solver_BLDS.solve(ht,HanoiTowers.heuristic2,b,1000000))

    print("5 Disks")
    ht_5 = HanoiTowers(5,['P' for i in range(5)])
    print(solver_BLDS.solve(ht_5,HanoiTowers.heuristic2,b,1000000))

    print("8 Disks")
    ht_8 = HanoiTowers(8,['P' for i in range(8)])
    print(solver_BLDS.solve(ht_8,HanoiTowers.heuristic2,b,1000000))

    print("10 Disks")
    ht_10 = HanoiTowers(10,['P' for i in range(10)])
    print(solver_BLDS.solve(ht_10,HanoiTowers.heuristic2,b,1000000))

    print("15 Disks")    
    ht_15 = HanoiTowers(15,['P' for i in range(15)])
    print(solver_BLDS.solve(ht_15,HanoiTowers.heuristic2,b,1000000))


import sys
class recursion_depth:
    def __init__(self, limit):
        self.limit = limit
        self.default_limit = sys.getrecursionlimit()
    def __enter__(self):
        sys.setrecursionlimit(self.limit)
    def __exit__(self, type, value, traceback):
        sys.setrecursionlimit(self.default_limit)



'''
Decomenteaza pentru a rula A*
'''
# for p in problems_4_easy:
#     print(solver_A.solve(p,NPuzzle.manhattan_distance))


'''
Decomenteaza pentru a rula Beam Search
'''
# for p in problems_5:
#     print(solver_B.solve(p,100,NPuzzle.manhattan_distance,time.time()))



'''
Decomenteaza pentru a rula GLDS
'''
# print("With m 4 normal")
# with recursion_depth(10000000):
#     for p in problems_4:
#         start_time = time.time()
#         rez = solver_G.solve(p,NPuzzle.manhattan_distance,1000000,1000)
#         end_time = time.time()
#         print(rez,end_time - start_time)

'''
Decomenteaza pentru a rula Beam Search
# '''
# for p in problems_4:
#     print(solver_BLDS.solve(p,NPuzzle.manhattan_distance,100,1000000))



tests_can_apply_move()
tests_can_move()
tests_get_neigh()

tests_BLDS_hanoi(1000)

# for no_disks in range(4,16):
#         print("No disk:",no_disks)
#         start = time.time()
#         tbr = solver_BLDS.solve(HanoiTowers(no_disks,['P' for i in range(no_disks)]),HanoiTowers.heuristic2,50,1000000)
#         end = time.time()
#         print(tbr,end-start)