from schelet import *
import time
import sys
import numpy as np

print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000000)

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

## MEM pe problems_4[1] ,problems_4[3]
## problems_6[0] MEM | TLE
# print(len(should_work_GLDS))
# for p in should_work_GLDS:

## 7 merge pe manhattan
## TODO: pune de mana
# print(solver_G.solve(problems_4_easy[0],NPuzzle.manhattan_distance,1000000,100000))

'''
problems_5_easy[0] - python crashes
problems_5_easy[1] - python crashes
analog toate
'''
 
## manhattan
 ## la problem 6 nu trece ultima cu b 100
 ## la problem 6 nu trece niciuna cu b 10
 ## la problem 6 nu trec ultimele 2 cu b 50
## la problem 6 nu trece ultima de la 6
# print(solver_BLDS.solve(problems_4_easy[1],NPuzzle.manhattan_distance,100,100000))
'''
## problem_4_easy BLDS both b 10: primele 3 trec
## problem_4_easy BLDS both b 50: toate
## problem_4_easy BLDS both b 100: toate
## problem_4_easy BLDS both b 500: toate

## problem_5_easy BLDS both b 10: primele 2
## problem_5_easy BLDS both b 100: niciuna
## problem_5_easy BLDS both b 50: niciuna
## problem_5_easy BLDS both b 500: primele 2

## problem_6_easy BLDS both b 10: toate
## problem_6_easy BLDS both b 50: primele 3
## problem_6_easy BLDS both b 100: toate
## problem_6_easy BLDS both b 500: toate

## problem_4 BLDS both b 10: toate
## problem_5 BLDS both b 50: toate
## problem_4 BLDS both b 100: toate
## problem_4 BLDS both b 500: toate


pe problem_5 si 6 nimic
'''

# for p in problems_6:
#     print(solver_BLDS.solve(p,NPuzzle.manhattan_and_num_inversions,50,1000000))


# index = 0
# for p in problems_4_easy + problems_5_easy + problems_6_easy + problems_4 + problems_5 + problems_6:
#     print(index)
#     if index >= 15:
#         print(solver_BLDS.solve(p,NPuzzle.manhattan_and_num_inversions,100,1000000))
#     index += 1

# random.seed(4242)
# for i in range(10):
#     p = genOne(3, 4)
#     p.display()
#     print("Manhattan: ",p.evaluate_state(NPuzzle.manhattan_distance))
#     print("Manhattan + no_linear_conflicts: ",p.evaluate_state(NPuzzle.manhattan_and_num_inversions))
#     print("\n")

# p = NPuzzle([1,2," ",7,5,3,8,4,6])
# print("Manhattan: ",p.evaluate_state(NPuzzle.manhattan_distance))
# print("Both: ",p.evaluate_state(NPuzzle.manhattan_and_num_inversions))
# p = NPuzzle([" ",2,3,1,4,5,7,8,6])
# print("Manhattan: ",p.evaluate_state(NPuzzle.manhattan_distance))
# print("Both: ",p.evaluate_state(NPuzzle.manhattan_and_num_inversions))
# p = NPuzzle([1,2,3,4,6," ",7,5,8])
# print("Manhattan: ",p.evaluate_state(NPuzzle.manhattan_distance))
# print("Both: ",p.evaluate_state(NPuzzle.manhattan_and_num_inversions))
# p = NPuzzle([1,3,6,4,2,8,7,5," "])
# print("Manhattan: ",p.evaluate_state(NPuzzle.manhattan_distance))
# print("Both: ",p.evaluate_state(NPuzzle.manhattan_and_num_inversions))
# p = NPuzzle([1,2,3,4," ",5,7,8,6])
# print("Manhattan: ",p.evaluate_state(NPuzzle.manhattan_distance))
# print("Both: ",p.evaluate_state(NPuzzle.manhattan_and_num_inversions))
# p = NPuzzle([1,2,3,4,5,6,7," ",8])
# print("Manhattan: ",p.evaluate_state(NPuzzle.manhattan_distance))
# print("Both: ",p.evaluate_state(NPuzzle.manhattan_and_num_inversions))
# p = NPuzzle([" ",2,3,1,4,5,7,8,6])
# print("Manhattan: ",p.evaluate_state(NPuzzle.manhattan_distance))
# print("Both: ",p.evaluate_state(NPuzzle.manhattan_and_num_inversions))
# p = NPuzzle([1,2,3,4,5,6,7,8," "])
# print("Manhattan: ",p.evaluate_state(NPuzzle.manhattan_distance))
# print("Both: ",p.evaluate_state(NPuzzle.manhattan_and_num_inversions))
# p = NPuzzle([2," ",3,1,4,5,7,8,6])
# print("Manhattan: ",p.evaluate_state(NPuzzle.manhattan_distance))
# print("Both: ",p.evaluate_state(NPuzzle.manhattan_and_num_inversions))
# p = NPuzzle([1,2,3,4," ",5,7,8,6])
# print("Manhattan: ",p.evaluate_state(NPuzzle.manhattan_distance))
# print("Both: ",p.evaluate_state(NPuzzle.manhattan_and_num_inversions))


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

    ht.move(3,'R').display()
 

def tests_get_neigh():
    ht = HanoiTowers(4,['P' for i in range(4)])

    ht.r[0] = 'Q'
    ht.r[1] = 'Q'
    ht.r[2] = 'P'
    ht.r[3] = 'P'

    for neigh in ht.get_neighbours():
        print(neigh.evaluate_state(HanoiTowers.heuristic2))
        neigh.display()

# tests_can_apply_move()
# tests_can_move()

def tests_GLDS_hanoi():
    ht = HanoiTowers(4,['P' for i in range(4)])

    ht.r[0] = 'G'
    ht.r[1] = 'R'
    ht.r[2] = 'R'
    ht.r[3] = 'P'

    solver_BLDS = BLDS()
    print("4 Disks")
    print(solver_BLDS.solve(ht,HanoiTowers.heuristic2,100,1000000))

    print("5 Disks")
    ht_5 = HanoiTowers(5,['P' for i in range(5)])
    print(solver_BLDS.solve(ht_5,HanoiTowers.heuristic2,100,1000000))

    print("8 Disks")
    ht_8 = HanoiTowers(8,['P' for i in range(8)])
    print(solver_BLDS.solve(ht_8,HanoiTowers.heuristic2,1000,1000000))

    print("10 Disks")
    ht_10 = HanoiTowers(10,['P' for i in range(10)])
    print(solver_BLDS.solve(ht_10,HanoiTowers.heuristic2,1000,1000000))

    print("15 Disks")    
    ht_15 = HanoiTowers(15,['P' for i in range(15)])
    print(solver_BLDS.solve(ht_15,HanoiTowers.heuristic2,1000,1000000))
tests_GLDS_hanoi()
# tests_get_neigh()
# tests_can_move()
    