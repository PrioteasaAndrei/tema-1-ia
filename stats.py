from schelet import *
import time
import numpy as np
import sys

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


B = [1,10,50,100,500,1000]
no_steps_B = []
no_steps_A = []
no_states_A = []
no_states_B = []
time_B = []
time_A = []

## TODO: plot si verifica ca nu ai dat copy paste prost

for b in B:
    print("Problems 4 easy")
    steps_4_easy_B = []
    time_4_easy_B = []
    states_4_easy_B = []
    for problem in problems_4_easy:
        start = time.time()
        path_len,states_no = solver_B.solve(problem,b,NPuzzle.manhattan_and_num_inversions)
        end = time.time()
        steps_4_easy_B += [path_len]
        time_4_easy_B += [end - start]
        states_4_easy_B += [states_no]
        print("Solved in:",path_len," steps")
        print("\n")

    no_steps_B.append(steps_4_easy_B)
    time_B.append(time_4_easy_B)
    no_states_B.append(states_4_easy_B)

    print("Problems 5 easy")
    steps_5_easy_B = []
    time_5_easy_B = []
    states_5_easy_B = []
    for problem in problems_5_easy:
        start = time.time()
        path_len,states_no = solver_B.solve(problem,b,NPuzzle.manhattan_and_num_inversions)
        end = time.time()
        steps_5_easy_B += [path_len]
        time_5_easy_B += [end - start]
        states_5_easy_B += [states_no]
        print("Solved in:",path_len," steps")
        print("\n")

    no_steps_B.append(steps_5_easy_B)
    time_B.append(time_5_easy_B)
    no_states_B.append(states_5_easy_B)

    print("Problems 6 easy")
    steps_6_easy_B = []
    time_6_easy_B = []
    states_6_easy_B = []
    for problem in problems_6_easy:
        start = time.time()
        path_len,states_no = solver_B.solve(problem,b,NPuzzle.manhattan_and_num_inversions)
        end = time.time()
        steps_6_easy_B += [path_len]
        time_6_easy_B += [end - start]
        states_6_easy_B += [states_no]
        print("Solved in:",path_len," steps")
        print("\n")

    no_steps_B.append(steps_6_easy_B)
    time_B.append(time_6_easy_B)
    no_states_B.append(states_6_easy_B)

    print("Problems 4")
    steps_4_B = []
    time_4_B = []
    states_4 = []
    for problem in problems_4:
        start = time.time()
        path_len,states_no = solver_B.solve(problem,b,NPuzzle.manhattan_and_num_inversions)
        end = time.time()
        steps_4_B += [path_len]
        time_4_B += [end - start]
        states_4 += [states_no]
        print("Solved in:",path_len," steps")
        print("\n")

    no_steps_B.append(steps_4_B)
    time_B.append(time_4_B)
    no_states_B.append(states_4)

    print("Problems 5")
    steps_5_B = []
    time_5_B = []
    states_5 = []
    for problem in problems_5:
        start = time.time()
        path_len,states_no = solver_B.solve(problem,b,NPuzzle.manhattan_and_num_inversions)
        end = time.time()
        steps_5_B += [path_len]
        time_5_B += [end - start]
        states_5 += [states_no]
        print("Solved in:",path_len," steps")
        print("\n")

    no_steps_B.append(steps_5_B)
    time_B.append(time_5_B)
    no_states_B.append(states_5)

    print("Problems 6")
    steps_6_B = []
    time_6_B = []
    states_6 = []
    for problem in problems_6:
        start = time.time()
        path_len,states_no = solver_B.solve(problem,b,NPuzzle.manhattan_and_num_inversions)
        end = time.time()
        steps_6_B += [path_len]
        time_6_B += [end - start]
        states_6 += [states_no]
        print("Solved in:",path_len," steps")
        print("\n")

    no_steps_B.append(steps_6_B)
    time_B.append(time_6_B)
    no_states_B.append(states_6)


## no_steps_format_B
## easy - 4,5,6 - normal - 4,5,6

## time_format_B
## easy - 4,5,6 - normal - 4,5,6

np.save("no_steps_A_star.npy",np.array(no_steps_A))
np.save("no_steps_Beam.npy",np.array(no_steps_B))
np.save("time_A_star.npy",np.array(time_A))
np.save("time_Beam.npy",np.array(time_B))
np.save("no_states_Beam.npy",np.array(no_states_B))
