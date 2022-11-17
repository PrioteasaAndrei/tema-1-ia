from schelet import *
import time

# random.seed(4242)
# avg_time = 0
# time_counter = 0

# for i in range(10):
#     print("Iteration:",i)
#     p = genOne(3, 4)
#     # p.display()
#     print(p.evaluate_state(NPuzzle.manhattan_and_num_inversions))
#     start = time.time()
#     solver.solve(p,100,NPuzzle.manhattan_and_num_inversions)
#     end = time.time()
#     print("Solution found in:",end - start)
#     avg_time *= time_counter
#     avg_time += (end - start)
#     avg_time /= time_counter + 1
#     time_counter += 1

# print("Average time:",avg_time)

solver_A = AStar()
solver_B = BeamSearch()
f = open("files/problems5-easy.txt", "r")
input = f.readlines()
f.close()
problems_4 = [NPuzzle.read_from_line(line) for line in input]

## cu manhatten simplu merge pe 5 si 6
# print(solver_B.solve(problems_4[4],10,NPuzzle.manhattan_and_num_inversions))
for p in problems_4:
    print(solver_A.solve(p,NPuzzle.manhattan_distance))
# print(solver_A.solve(problems_4[4],NPuzzle.manhattan_and_num_inversions))