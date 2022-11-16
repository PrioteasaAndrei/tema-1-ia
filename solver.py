from schelet import *
import time

f = open("files/problems4-easy.txt", "r")
input = f.readlines()
f.close()
problems = [NPuzzle.read_from_line(line) for line in input]
problems[1].display()
print(problems[1].evaluate_state(NPuzzle.manhattan_and_num_inversions))



# solver = AStar()
solver  = BeamSearch()

# a_star_solver.solve(problems[1],NPuzzle.manhattan_and_num_inversions)
for problem in problems:
    out = solver.solve(problem,10,NPuzzle.manhattan_and_num_inversions)
    print("Solved in:",out," steps")
    print("\n")

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
