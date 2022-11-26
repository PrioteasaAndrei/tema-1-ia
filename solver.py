from schelet import *
import time
import sys
import numpy as np

print(sys.getrecursionlimit())
sys.setrecursionlimit(100000)

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
print(solver_G.solve(problems_5[2],NPuzzle.manhattan_and_num_inversions,500000,100000))

'''
problems_5_easy[0] - python crashes
problems_5_easy[1] - python crashes
analog toate
'''
 

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