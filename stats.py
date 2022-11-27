from schelet import *
import time
import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt
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


writer = pd.ExcelWriter('Report.xlsx', engine = 'xlsxwriter')

def create_stats_GLDS(heuristic):
    ## fac pe problems_4_easy
    ## fac pe problems_6_easy in afara de 1
    ## fac pe problems_4 0 si 2
    solver_GLDS = GLDS()
    others = [problems_4[0],problems_4[2]]

    no_steps_4_easy = []
    no_states_4_easy = []
    time_4_easy = []
    for p in problems_4_easy:
        start_time = time.time()
        tbr = solver_GLDS.solve(p,heuristic,1000000,10000)
        end_time = time.time()
        no_steps = -1
        no_states = -1
        if isinstance(tbr,tuple):
            no_steps = tbr[0]
            no_states = tbr[1]

        if no_steps == -1 and no_states == -1:
            ## Exceeded mem
            continue
            
        no_steps_4_easy += [no_steps]
        no_states_4_easy += [no_states]
        time_4_easy += [end_time - start_time]
    
    no_steps_6_easy = []
    no_states_6_easy = []
    time_6_easy = []
    for i in range(len(problems_6_easy)):
        if i == 1:
            continue
        
        start_time = time.time()
        tbr = solver_GLDS.solve(p,heuristic,1000000,10000)
        end_time = time.time()
        no_steps = -1
        no_states = -1
        if isinstance(tbr,tuple):
            no_steps = tbr[0]
            no_states = tbr[1]

        if no_steps == -1 and no_states == -1:
            ## Exceeded mem
            continue

        no_steps_6_easy += [no_steps]
        no_states_6_easy += [no_states]
        time_6_easy += [end_time - start_time]


    no_steps_4 = []
    no_states_4 = []
    time_4 = [] 
    for p in others:
        start_time = time.time()
        tbr = solver_GLDS.solve(p,heuristic,1000000,10000)
        end_time = time.time()
        no_steps = -1
        no_states = -1

        if isinstance(tbr,tuple):
            no_steps = tbr[0]
            no_states = tbr[1]

        if no_steps == -1 and no_states == -1:
            ## Exceeded mem
            continue
            
        no_steps_4 += [no_steps]
        no_states_4 += [no_states]
        time_4 += [end_time - start_time]


    if heuristic == NPuzzle.manhattan_and_num_inversions:
        np.save("glds/no_steps_GLDS_both_4_easy.npy",np.array(no_steps_4_easy))
        np.save("glds/no_steps_GLDS_both_4.npy",np.array(no_steps_4))
        np.save("glds/no_steps_GLDS_both_6_easy.npy",np.array(no_steps_6_easy))

        np.save("glds/time_GLDS_both_4_easy.npy",np.array(time_4_easy))
        np.save("glds/time_GLDS_both_6_easy.npy",np.array(time_6_easy))
        np.save("glds/time_GLDS_both_4.npy",np.array(time_4))

        np.save("glds/no_states_GLDS_both_4_easy.npy",np.array(no_states_4_easy))
        np.save("glds/no_states_GLDS_both_6_easy.npy",np.array(no_states_6_easy))
        np.save("glds/no_states_GLDS_both_4.npy",np.array(no_states_4))
    else:
        np.save("glds/no_steps_GLDS_m_4_easy.npy",np.array(no_steps_4_easy))
        np.save("glds/no_steps_GLDS_m_4.npy",np.array(no_steps_4))
        np.save("glds/no_steps_GLDS_m_6_easy.npy",np.array(no_steps_6_easy))

        np.save("glds/time_GLDS_m_4_easy.npy",np.array(time_4_easy))
        np.save("glds/time_GLDS_m_6_easy.npy",np.array(time_6_easy))
        np.save("glds/time_GLDS_m_4.npy",np.array(time_4))

        np.save("glds/no_states_GLDS_m_4_easy.npy",np.array(no_states_4_easy))
        np.save("glds/no_states_GLDS_m_6_easy.npy",np.array(no_states_6_easy))
        np.save("glds/no_states_GLDS_m_4.npy",np.array(no_states_4))

def create_stats_A_star(heuristic):
    solver_A = AStar()
    no_steps_A = []
    no_states_A = []
    time_A = []

    no_steps_4_easy = []
    no_states_4_easy = []
    time_4_easy = []
    for p in problems_4_easy:
        start = time.time()
        no_steps,no_states = solver_A.solve(p,heuristic)
        end = time.time()
        no_steps_4_easy += [no_steps]
        no_states_4_easy += [no_states]
        time_4_easy += [end - start]
    
    no_steps_A.append(no_steps_4_easy)
    no_states_A.append(no_states_4_easy)
    time_A.append(time_4_easy)


    no_steps_5_easy = []
    no_states_5_easy = []
    time_5_easy = []
    for p in problems_5_easy:
        start = time.time()
        no_steps,no_states = solver_A.solve(p,heuristic)
        end = time.time()
        no_steps_5_easy += [no_steps]
        no_states_5_easy += [no_states]
        time_5_easy += [end - start]
    
    no_steps_A.append(no_steps_5_easy)
    no_states_A.append(no_states_5_easy)
    time_A.append(time_5_easy)


    no_steps_6_easy = []
    no_states_6_easy = []
    time_6_easy = []
    for p in problems_6_easy:
        start = time.time()
        no_steps,no_states = solver_A.solve(p,heuristic)
        end = time.time()
        no_steps_6_easy += [no_steps]
        no_states_6_easy += [no_states]
        time_6_easy += [end - start]
    
    no_steps_A.append(no_steps_6_easy)
    no_states_A.append(no_states_6_easy)
    time_A.append(time_6_easy)


    if heuristic == NPuzzle.manhattan_and_num_inversions:
        np.save("no_steps_A_star_both.npy",np.array(no_steps_A))
        np.save("time_A_star_both.npy",np.array(time_A))
        np.save("no_states_A_star_both.npy",np.array(no_states_A))
    else:
        np.save("no_steps_A_star_m.npy",np.array(no_steps_A))
        np.save("time_A_star_m.npy",np.array(time_A))
        np.save("no_states_A_star_m.npy",np.array(no_states_A))
    

def create_stats_beam(heuristic,B=[1,10,50,100]):
    # B = [1,10,50,100,500,1000]
    no_steps_B = {}
    time_B = {}
    no_states_B = {}
    for b in B:
        no_states_B[b] = []
        time_B[b] = []
        no_steps_B[b] = []
    
    solver_B  = BeamSearch()

    for b in B:
        print("Problems 4 easy")
        steps_4_easy_B = []
        time_4_easy_B = []
        states_4_easy_B = []
        for problem in problems_4_easy:
            start = time.time()
            path_len,states_no = solver_B.solve(problem,b,heuristic,time.time())
            end = time.time()
            steps_4_easy_B += [path_len]
            time_4_easy_B += [end - start]
            states_4_easy_B += [states_no]
            print("Solved in:",path_len," steps")
            print("\n")

        no_steps_B[b].append(steps_4_easy_B)
        time_B[b].append(time_4_easy_B)
        no_states_B[b].append(states_4_easy_B)

        print("Problems 5 easy")
        steps_5_easy_B = []
        time_5_easy_B = []
        states_5_easy_B = []
        for problem in problems_5_easy:
            start = time.time()
            path_len,states_no = solver_B.solve(problem,b,heuristic,time.time())
            end = time.time()
            steps_5_easy_B += [path_len]
            time_5_easy_B += [end - start]
            states_5_easy_B += [states_no]
            print("Solved in:",path_len," steps")
            print("\n")

        no_steps_B[b].append(steps_5_easy_B)
        time_B[b].append(time_5_easy_B)
        no_states_B[b].append(states_5_easy_B)

        print("Problems 6 easy")
        steps_6_easy_B = []
        time_6_easy_B = []
        states_6_easy_B = []
        for problem in problems_6_easy:
            start = time.time()
            path_len,states_no = solver_B.solve(problem,b,heuristic,time.time())
            end = time.time()
            steps_6_easy_B += [path_len]
            time_6_easy_B += [end - start]
            states_6_easy_B += [states_no]
            print("Solved in:",path_len," steps")
            print("\n")

        no_steps_B[b].append(steps_6_easy_B)
        time_B[b].append(time_6_easy_B)
        no_states_B[b].append(states_6_easy_B)

        print("Problems 4")
        steps_4_B = []
        time_4_B = []
        states_4 = []
        for problem in problems_4:
            start = time.time()
            path_len,states_no = solver_B.solve(problem,b,heuristic,time.time())
            end = time.time()
            steps_4_B += [path_len]
            time_4_B += [end - start]
            states_4 += [states_no]
            print("Solved in:",path_len," steps")
            print("\n")

        no_steps_B[b].append(steps_4_B)
        time_B[b].append(time_4_B)
        no_states_B[b].append(states_4)

        # print("Problems 5")
        # steps_5_B = []
        # time_5_B = []
        # states_5 = []
        # for problem in problems_5:
        #     start = time.time()
        #     path_len,states_no = solver_B.solve(problem,b,heuristic,time.time())
        #     end = time.time()
        #     steps_5_B += [path_len]
        #     time_5_B += [end - start]
        #     states_5 += [states_no]
        #     print("Solved in:",path_len," steps")
        #     print("\n")

        # no_steps_B.append(steps_5_B)
        # time_B.append(time_5_B)
        # no_states_B.append(states_5)

        # print("Problems 6")
        # steps_6_B = []
        # time_6_B = []
        # states_6 = []
        # for problem in problems_6:
        #     start = time.time()
        #     path_len,states_no = solver_B.solve(problem,b,heuristic,time.time())
        #     end = time.time()
        #     steps_6_B += [path_len]
        #     time_6_B += [end - start]
        #     states_6 += [states_no]
        #     print("Solved in:",path_len," steps")
        #     print("\n")

        # no_steps_B.append(steps_6_B)
        # time_B.append(time_6_B)
        # no_states_B.append(states_6)

 
    if heuristic == NPuzzle.manhattan_and_num_inversions:
        np.save("beam/no_steps_Beam_both.npy",no_steps_B)
        np.save("beam/time_Beam_both.npy",time_B)
        np.save("beam/no_states_Beam_both.npy",no_states_B)
    else:
        np.save("beam/no_steps_Beam_m.npy",no_steps_B)
        np.save("beam/time_Beam_m.npy",time_B)
        np.save("beam/no_states_Beam_m.npy",no_states_B)

def run_stats_Beam():
    create_stats_beam(NPuzzle.manhattan_and_num_inversions)
    create_stats_beam(NPuzzle.manhattan_distance)

def run_stats_A_Star():
    create_stats_A_star(NPuzzle.manhattan_and_num_inversions)
    create_stats_A_star(NPuzzle.manhattan_distance)

def run_stats_GLDS():
    create_stats_GLDS(NPuzzle.manhattan_and_num_inversions)
    create_stats_GLDS(NPuzzle.manhattan_distance)

## Metrics are calculated for tests that have not failed
def interpret_stats_A_star():
    time_A_star_both = list(np.load("time_A_star_both.npy"))
    time_A_star_m = list(np.load("time_A_star_m.npy"))
    no_steps_A_star_both = list(np.load("no_steps_A_star_both.npy"))
    no_steps_A_star_m = list(np.load("no_steps_A_star_m.npy"))
    no_states_A_star_both = list(np.load("no_states_A_star_both.npy"))
    no_states_A_star_m = list(np.load("no_states_A_star_m.npy"))

    ## o sa aiba 3 elemente cate unul pentru fiecare problema easy
    alg_name = "A_STAR"
    h1 = "Manhattan distance"
    h2 = "Manhattan distance + linear conflicts"
    problem_number = 4
    rows = []
    cols = []
    ## pt 4 5 6
    no_solution_not_found_both = []
    for time_list,no_steps_list,no_states_list in zip(time_A_star_both,no_steps_A_star_both,no_states_A_star_both): 

        time_list = list(time_list)
        no_steps_list = list(no_steps_list)
        no_states_list = list(no_states_list)

        time_variance = np.var([x for x in time_list if x > 0.000000001])
        steps_variance = np.var([x for x in no_steps_list if x != -1])
        states_variance = np.var([x for x in no_states_list if x != -1])

        time_mean = np.mean([x for x in time_list if x > 0.001])
        steps_mean = np.mean([x for x in no_steps_list if x != -1])
        states_mean = np.mean([x for x in no_states_list if x != -1])

        no_solution_not_found_both += [no_steps_list.count(-1)]

        row = "Algorithm: " +  alg_name + " Heuristic: " + h2 + " Problem size:" + str(problem_number)
        col = [time_mean,steps_mean,states_mean,time_variance,steps_variance,states_variance]

        rows += [row]
        cols += [col]

        problem_number += 1

    problem_number = 4
    no_solution_not_found_m = []
    for time_list,no_steps_list,no_states_list in zip(time_A_star_m,no_steps_A_star_m,no_states_A_star_m): 

        time_list = list(time_list)
        no_steps_list = list(no_steps_list)
        no_states_list = list(no_states_list)

        time_variance = np.var([x for x in time_list if x > 0.0000000001])
        steps_variance = np.var([x for x in no_steps_list if x != -1])
        states_variance = np.var([x for x in no_states_list if x != -1])

        time_mean = np.mean([x for x in time_list if x > 0.001])
        steps_mean = np.mean([x for x in no_steps_list if x != -1])
        states_mean = np.mean([x for x in no_states_list if x != -1])

        no_solution_not_found_m += [no_steps_list.count(-1)]


        row = "Algorithm: " +  alg_name + " Heuristic: " + h1 + " Problem size:" + str(problem_number)
        col = [time_mean,steps_mean,states_mean,time_variance,steps_variance,states_variance]

        rows += [row]
        cols += [col]

        problem_number += 1

    no_of_solutions_found_both = [(5-x) / 5 * 100 for x in no_solution_not_found_both]
    no_of_solutions_found_m = [(5-x) / 5 * 100 for x in no_solution_not_found_m]


    df = pd.DataFrame(cols,index=rows,columns=["Time mean","Steps mean","States mean","Time variance","Steps variance","States variance"])
    # df.to_excel("A_star_analysis.xlsx")
    finished_games = pd.DataFrame(map(lambda x: str(x) + "%",no_of_solutions_found_both + no_of_solutions_found_m),index=["4-easy-" + h2,"5-easy-" + h2,"6-easy-" + h2,"4-easy-" + h1,"5-easy-" + h1,"6-easy-" + h1],columns=["Solution found"])

    df.to_excel(writer, index=rows, sheet_name='A_star')
    finished_games.to_excel(writer,index=["4-easy-" + h2,"5-easy-" + h2,"6-easy-" + h2,"4-easy-" + h1,"5-easy-" + h1,"6-easy-" + h1],sheet_name='A_star_procent_finished')

    workbook  = writer.book
    worksheet = writer.sheets['A_star']
    format1 = workbook.add_format({'num_format': '0.0000'})
    worksheet.set_column(0,6, None, format1)  # Adds formatting to column C
  


def interpret_stats_Beam(B=[1,10,50,100]):
    no_steps_Beam_both = np.load("beam/no_steps_Beam_both.npy",allow_pickle='TRUE').item()
    time_Beam_both = np.load("beam/time_Beam_both.npy",allow_pickle='TRUE').item()
    no_states_Beam_both = np.load("beam/no_states_Beam_both.npy",allow_pickle='TRUE').item()

    no_steps_Beam_m = np.load("beam/no_steps_Beam_m.npy",allow_pickle='TRUE').item()
    time_Beam_m = np.load("beam/time_Beam_m.npy",allow_pickle='TRUE').item()
    no_states_Beam_m = np.load("beam/no_states_Beam_m.npy",allow_pickle='TRUE').item()

    ## o sa aiba 3 elemente cate unul pentru fiecare problema easy
    ## ret si -1 si -7
    alg_name = "Beam search"
    h1 = "Manhattan distance"
    h2 = "Manhattan distance + linear conflicts"
    problems_names = ["4-easy","5-easy","6-easy","4-normal"]
    rows = []
    cols = [] 
    no_of_solutions_found_both = {}
    no_of_solutions_found_m = {}
    for b in B:
        no_of_solutions_found_both[b] = []
        no_of_solutions_found_m[b] = []

    for b in B:
        problem_index = 0

        no_solution_not_found_both = []
        for time_list,no_steps_list,no_states_list in zip(time_Beam_both[b],no_steps_Beam_both[b],no_states_Beam_both[b]): 

            time_list = list(time_list)
            no_steps_list = list(no_steps_list)
            no_states_list = list(no_states_list)

            time_variance = np.var([x for x in time_list if x > 0.000000001])
            steps_variance = np.var([x for x in no_steps_list if (x != -1 and x!= -7)])
            states_variance = np.var([x for x in no_states_list if (x != -1 and x!= -7)])

            time_mean = np.mean([x for x in time_list if x > 0.001])
            steps_mean = np.mean([x for x in no_steps_list if (x != -1 and x!= -7)])
            states_mean = np.mean([x for x in no_states_list if (x != -1 and x!= -7)])

            no_solution_not_found_both += [no_steps_list.count(-1) + no_steps_list.count(-7)]

            row = "Algorithm: " +  alg_name + " Heuristic: " + h2 + "Beam size: " + str(b) +  " Problem size:" + problems_names[problem_index]

            col = [time_mean,steps_mean,states_mean,time_variance,steps_variance,states_variance]

            rows += [row]
            cols += [col]

            problem_index = (problem_index + 1) % len(problems_names) 

        problem_index = 0
        no_solution_not_found_m = []
        for time_list,no_steps_list,no_states_list in zip(time_Beam_m[b],no_steps_Beam_m[b],no_states_Beam_m[b]): 

            time_list = list(time_list)
            no_steps_list = list(no_steps_list)
            no_states_list = list(no_states_list)

            time_variance = np.var([x for x in time_list if x > 0.000000001])
            steps_variance = np.var([x for x in no_steps_list if (x != -1 and x!= -7)])
            states_variance = np.var([x for x in no_states_list if (x != -1 and x!= -7)])

            time_mean = np.mean([x for x in time_list if x > 0.001])
            steps_mean = np.mean([x for x in no_steps_list if (x != -1 and x!= -7)])
            states_mean = np.mean([x for x in no_states_list if (x != -1 and x!= -7)])

            no_solution_not_found_both += [no_steps_list.count(-1) + no_steps_list.count(-7)]


            row = "Algorithm: " +  alg_name + " Heuristic: " + h1 + "Beam size: " + str(b) + " Problem size:" + problems_names[problem_index]
            col = [time_mean,steps_mean,states_mean,time_variance,steps_variance,states_variance]

            rows += [row]
            cols += [col]
      
            problem_index = (problem_index + 1) % len(problems_names) 

        
        no_of_solutions_found_both[b] = [(5-x) / 5 * 100 for x in no_solution_not_found_both]
        no_of_solutions_found_m[b] = [(5-x) / 5 * 100 for x in no_solution_not_found_m]


    index_finished_games = []
    cols_finished_games = []

    for b in B:
        cols_finished_games += no_of_solutions_found_both[b]
        cols_finished_games += no_of_solutions_found_m[b]

        both_index = map(lambda x: x + h2 + " " + str(b),problems_names)
        m_index = map(lambda x: x + h1 + " " + str(b),problems_names)

        index_finished_games += both_index
        index_finished_games += m_index

    df = pd.DataFrame(cols,index=rows,columns=["Time mean","Steps mean","States mean","Time variance","Steps variance","States variance"])
    
    finished_games = pd.DataFrame(map(lambda x: str(x) + "%",cols_finished_games),index=index_finished_games,columns=["Solution found"])

    df.to_excel(writer, index=rows, sheet_name='Beam_search')
    finished_games.to_excel(writer,index=index_finished_games,sheet_name='Beam_procent_finished')

    workbook  = writer.book
    worksheet = writer.sheets['Beam_search']
    format1 = workbook.add_format({'num_format': '0.0000'})
    worksheet.set_column(0,6, None, format1)  # Adds formatting to column C
    # writer.save()

def interpret_stats_GLDS():
    no_states_4_easy_both = list(np.load("glds/no_states_GLDS_both_4_easy.npy"))
    no_states_6_easy_both = list(np.load("glds/no_states_GLDS_both_6_easy.npy"))
    no_states_4_both = list(np.load("glds/no_states_GLDS_both_4.npy"))

    no_steps_4_easy_both = list(np.load("glds/no_steps_GLDS_both_4_easy.npy"))
    no_steps_6_easy_both = list(np.load("glds/no_steps_GLDS_both_6_easy.npy"))
    no_steps_4_both = list(np.load("glds/no_steps_GLDS_both_4.npy"))

    time_4_easy_both = list(np.load("glds/time_GLDS_both_4_easy.npy"))
    time_6_easy_both = list(np.load("glds/time_GLDS_both_6_easy.npy"))
    time_4_both = list(np.load("glds/time_GLDS_both_4.npy"))

    # print(no_states_4_easy_both,no_steps_4_easy_both,time_4_easy_both)
    # print("\n")
    # print(no_states_6_easy_both,no_steps_6_easy_both,time_6_easy_both)
    # print("\n")
    # print(no_states_4_both,no_steps_4_both,time_4_both)

    print("Problem 4 easy both")
    var_states_4_easy_both = np.var(no_states_4_easy_both)
    var_steps_4_easy_both = np.var(no_steps_4_easy_both)
    var_time_4_easy_both = np.var(time_4_easy_both)

    mean_states_4_easy_both = np.mean(no_states_4_easy_both)
    mean_steps_4_easy_both = np.mean(no_steps_4_easy_both)
    mean_time_4_easy_both = np.mean(time_4_easy_both)
    
    print("Variance for states,steps,time: ",[var_states_4_easy_both,var_steps_4_easy_both,var_time_4_easy_both])
    print("Mean for states,steps,time: ",[mean_states_4_easy_both,mean_steps_4_easy_both,mean_time_4_easy_both])
    

    print("\nProblem 6 easy both")
    var_states_6_easy_both = np.var(no_states_6_easy_both)
    var_steps_6_easy_both = np.var(no_steps_6_easy_both)
    var_time_6_easy_both = np.var(time_6_easy_both)

    mean_states_6_easy_both = np.mean(no_states_6_easy_both)
    mean_steps_6_easy_both = np.mean(no_steps_6_easy_both)
    mean_time_6_easy_both = np.mean(time_6_easy_both)

    print("Variance for states,steps,time: ",[var_states_6_easy_both,var_steps_6_easy_both,var_time_6_easy_both])
    print("Mean for states,steps,time: ",[mean_states_6_easy_both,mean_steps_6_easy_both,mean_time_6_easy_both])
    
    print("\nProblem 4 normal both")
    var_states_4_both = np.var(no_states_4_both)
    var_steps_4_both = np.var(no_steps_4_both)
    var_time_4_both = np.var(time_4_both)

    mean_states_4_both = np.mean(no_states_4_both)
    mean_steps_4_both = np.mean(no_steps_4_both)
    mean_time_4_both = np.mean(time_4_both)

    print("Variance for states,steps,time: ",[var_states_4_both,var_steps_4_both,var_time_4_both])
    print("Mean for states,steps,time: ",[mean_states_4_both,mean_steps_4_both,mean_time_4_both])
    

def beam_vs_GLDS_bar_plot():
    # creating the dataset
    data = {'GLDS with Manhattan + no. of inversions, problem size: 4-easy': 100,
    'GLDS with Manhattan + no. of inversions, problem size: 6-easy': 80,
    'GLDS with Manhattan + no. of inversions, problem size: 4-normal': 40,
    'GLDS with (Manhattan + no. of inversions) / Manhatatn, other problem sizes and difficulties': 0,
   
    }
    total_glds_both = ((5 + 2 + 4) / 20) * 100
    total_glds_m = 0
    
    beam ={
    " 4-easyManhattan distance + linear conflicts 1":	0.0,
    " 5-easyManhattan distance + linear conflicts 1":	0.0,
    " 6-easyManhattan distance + linear conflicts 1":	80.0,
    " 4-normalManhattan distance + linear conflicts 1":	0.0,
    " 4-easyManhattan distance 1":	0.0,
    " 5-easyManhattan distance 1":	0.0,
    " 6-easyManhattan distance 1":	40.0,
    " 4-normalManhattan distance 1":	0.0,
    " 4-easyManhattan distance + linear conflicts 10":	100.0,
    " 5-easyManhattan distance + linear conflicts 10":	40.0,
    " 6-easyManhattan distance + linear conflicts 10":	100.0,
    " 4-normalManhattan distance + linear conflicts 10":	100.0,
    " 4-easyManhattan distance 10":	100.0,
    " 5-easyManhattan distance 10":	100.0,
    " 6-easyManhattan distance 10":	100.0,
    " 4-normalManhattan distance 10":	100.0,
    " 4-easyManhattan distance + linear conflicts 50":	100.0,
    " 5-easyManhattan distance + linear conflicts 50":	20.0,
    " 6-easyManhattan distance + linear conflicts 50":	80.0,
    " 4-normalManhattan distance + linear conflicts 50":	100.0,
    " 4-easyManhattan distance 50":	100.0,
    " 5-easyManhattan distance 50":	100.0,
    " 6-easyManhattan distance 50":	100.0,
    " 4-normalManhattan distance 50":	100.0,
    " 4-easyManhattan distance +  linear conflicts 100":	100.0,
    " 5-easyManhattan distance +  linear conflicts 100":	20.0,
    " 6-easyManhattan distance +  linear conflicts 100":	100.0,
    " 4-normalManhattan distance + linear conflicts 100":	100.0,
    " 4-easyManhattan distance 100":	100.0,
    " 5-easyManhattan distance 100":	100.0,
    " 6-easyManhattan distance 100":	100.0,
    " 4-normalManhattan distance 100":	100.0
    }

    beam_man = {
    " 4-easyManhattan distance 500":	100.0,
    " 5-easyManhattan distance 500":	100.0,
    " 6-easyManhattan distance 500":	100.0,
    " 4-normalManhattan distance 500":	100.0,
    " 4-easyManhattan distance 100":	100.0,
    " 5-easyManhattan distance 100":	100.0,
    " 6-easyManhattan distance 100":	100.0,
    " 4-normalManhattan distance 100":	100.0,
    " 4-easyManhattan distance 50":	100.0,
    " 5-easyManhattan distance 50":	100.0,
    " 6-easyManhattan distance 50":	100.0,
    " 4-normalManhattan distance 50":	100.0,
    " 4-easyManhattan distance 10":	100.0,
    " 5-easyManhattan distance 10":	100.0,
    " 6-easyManhattan distance 10":	100.0,
    " 4-normalManhattan distance 10":	100.0,
    " 4-easyManhattan distance 1":	0.0,
    " 5-easyManhattan distance 1":	0.0,
    " 6-easyManhattan distance 1":	40.0,
    " 4-normalManhattan distance 1":	0.0,
    }
    total_no_finished_beam_man = ((5 * 16 + 2) / (20 * 5)) * 100

    beam_both ={
    " 4-easyManhattan distance +  linear conflicts 500":	100.0,
    " 5-easyManhattan distance +  linear conflicts 500":	0.0,
    " 6-easyManhattan distance +  linear conflicts 500":	100.0,
    " 4-normalManhattan distance + linear conflicts 500":	100.0,
    " 4-easyManhattan distance +  linear conflicts 100":	100.0,
    " 5-easyManhattan distance +  linear conflicts 100":	20.0,
    " 6-easyManhattan distance +  linear conflicts 100":	100.0,
    " 4-normalManhattan distance + linear conflicts 100":	100.0,
    " 4-easyManhattan distance + linear conflicts 50":	100.0,
    " 5-easyManhattan distance + linear conflicts 50":	20.0,
    " 6-easyManhattan distance + linear conflicts 50":	80.0,
    " 4-normalManhattan distance + linear conflicts 50":	100.0,
    " 4-easyManhattan distance + linear conflicts 10":	100.0,
    " 5-easyManhattan distance + linear conflicts 10":	40.0,
    " 6-easyManhattan distance + linear conflicts 10":	100.0,
    " 4-normalManhattan distance + linear conflicts 10":	100.0,
    " 4-easyManhattan distance + linear conflicts 1":	0.0,
    " 5-easyManhattan distance + linear conflicts 1":	0.0,
    " 6-easyManhattan distance + linear conflicts 1":	80.0,
    " 4-normalManhattan distance + linear conflicts 1":	0.0,
    }

    total_no_finished_beam_both = ((5 * 11 + 4*2 + 2 + 1 * 2 ) / (5 * 20)) * 100


    courses = ["Beam search\nwith Manhattan distance","Beam search\nwith\nManhattan distance + no. inversions","GLDS\nwith Manhattan distance","GLDS\nwith\nManhattan distance + no. inversions"]
    values = [total_no_finished_beam_man,total_no_finished_beam_both,total_glds_m,total_glds_both]

    fig = plt.figure(figsize = (10, 5))

    # creating the bar plot
    plt.bar(courses, values, color ='maroon',width = 0.4)
    plt.xlabel("Algorithms")
    plt.ylabel("Procent finished")
    plt.title("GLDS vs Beam search finished games")
    plt.show()

def beam_vs_GLDS_box_plot(chose_problem_size,B=[1,10,50,100],mode="GLDS"):
    data_BLDS = {}

    if mode != "GLDS":
        ## pickle nu iti pastreaza tuplurile trebuie sa le iei tu cate 3
        data_BLDS =np.load("BLDS_results.npy",allow_pickle='TRUE').item()

    no_states_4_easy_both_GLDS = list(np.load("glds/no_states_GLDS_both_4_easy.npy"))
    no_states_6_easy_both_GLDS = list(np.load("glds/no_states_GLDS_both_6_easy.npy"))
    no_states_4_both_GLDS = list(np.load("glds/no_states_GLDS_both_4.npy"))

    no_steps_4_easy_both_GLDS = list(np.load("glds/no_steps_GLDS_both_4_easy.npy"))
    no_steps_6_easy_both_GLDS = list(np.load("glds/no_steps_GLDS_both_6_easy.npy"))
    no_steps_4_both_GLDS = list(np.load("glds/no_steps_GLDS_both_4.npy"))

    time_4_easy_both_GLDS = list(np.load("glds/time_GLDS_both_4_easy.npy"))
    time_6_easy_both_GLDS = list(np.load("glds/time_GLDS_both_6_easy.npy"))
    time_4_both_GLDS = list(np.load("glds/time_GLDS_both_4.npy"))

    no_steps_Beam_both = np.load("beam/no_steps_Beam_both.npy",allow_pickle='TRUE').item()
    time_Beam_both = np.load("beam/time_Beam_both.npy",allow_pickle='TRUE').item()
    no_states_Beam_both = np.load("beam/no_states_Beam_both.npy",allow_pickle='TRUE').item()

    no_steps_Beam_m = np.load("beam/no_steps_Beam_m.npy",allow_pickle='TRUE').item()
    time_Beam_m = np.load("beam/time_Beam_m.npy",allow_pickle='TRUE').item()
    no_states_Beam_m = np.load("beam/no_states_Beam_m.npy",allow_pickle='TRUE').item()

    b = 100

    # no_steps_Beam_both_100_4_easy = no_steps_Beam_both[b][0]
    # no_steps_Beam_both_100_5_easy = no_steps_Beam_both[b][1]
    # no_steps_Beam_both_100_6_easy = no_steps_Beam_both[b][2]
    # no_steps_Beam_both_100_4_normal = no_steps_Beam_both[b][3]

    # no_states_Beam_both_100_4_easy = no_states_Beam_both[b][0]
    # no_states_Beam_both_100_5_easy = no_states_Beam_both[b][1]
    # no_states_Beam_both_100_6_easy = no_states_Beam_both[b][2]
    # no_states_Beam_both_100_4_normal = no_states_Beam_both[b][3]

    # time_Beam_both_100_4_easy = time_Beam_both[b][0]
    # time_Beam_both_100_5_easy = time_Beam_both[b][1]
    # time_Beam_both_100_6_easy = time_Beam_both[b][2]
    # time_Beam_both_100_4_normal = time_Beam_both[b][3]



    # no_steps_Beam_m_100_4_easy = no_steps_Beam_m[b][0]
    # no_steps_Beam_m_100_5_easy = no_steps_Beam_m[b][1]
    # no_steps_Beam_m_100_6_easy = no_steps_Beam_m[b][2]
    # no_steps_Beam_m_100_4_normal = no_steps_Beam_m[b][3]

    # no_states_Beam_m_100_4_easy = no_states_Beam_m[b][0]
    # no_states_Beam_m_100_5_easy = no_states_Beam_m[b][1]
    # no_states_Beam_m_100_6_easy = no_states_Beam_m[b][2]
    # no_states_Beam_m_100_4_normal = no_states_Beam_m[b][3]

    # time_Beam_m_100_4_easy = time_Beam_m[b][0]
    # time_Beam_m_100_5_easy = time_Beam_m[b][1]
    # time_Beam_m_100_6_easy = time_Beam_m[b][2]
    # time_Beam_m_100_4_normal = time_Beam_m[b][3]


    ## la GLDS a trebuit sa maresc spatiul de stari la 1 000 000 ca altfel nu intra niciun test in memorie

    def generate_plot(data,string_y,problem_size,heuristic):
        fig = plt.figure(figsize =(10, 7))
        ax = fig.add_subplot(111)
        ax.set_xlabel('Algorithms')
        ax.set_ylabel(string_y)
        ax.set_title("Problem size:" + str(problem_size)  + "\nHeuristic: " + heuristic + "\n1-GLDS 2-Beam Search B = 10 3-Beam Search B = 50 4-Beam Search B = 100")
        bp = ax.boxplot(data)
        plt.show()


    if mode == "GLDS":
    ## 0 adica not working python crashes
        if chose_problem_size == 4:
            data_4_easy_time_both = [time_4_easy_both_GLDS,time_Beam_both[10][0],time_Beam_both[50][0],time_Beam_both[100][0]]
            generate_plot(data_4_easy_time_both,'Time (s)',4,"Manhattan Distance + no. inversions")
    
            data_4_easy_steps_both = [no_steps_4_easy_both_GLDS,no_steps_Beam_both[10][0],no_steps_Beam_both[50][0],no_steps_Beam_both[100][0]]
            generate_plot(data_4_easy_steps_both,'No steps',4,"Manhattan Distance + no. inversions")

            data_4_easy_states_both = [no_states_4_easy_both_GLDS,no_states_Beam_both[10][0],no_states_Beam_both[50][0],no_states_Beam_both[100][0]]
            generate_plot(data_4_easy_states_both,'No states',4,"Manhattan Distance + no. inversions")

            data_4_easy_time_m = [[0 for i in range(5)],time_Beam_m[10][0],time_Beam_m[50][0],time_Beam_m[100][0]]
            generate_plot(data_4_easy_time_m,'Time (s)',4,"Manhattan Distance")
    
            data_4_easy_steps_m = [[0 for i in range(5)],no_steps_Beam_m[10][0],no_steps_Beam_m[50][0],no_steps_Beam_m[100][0]]
            generate_plot(data_4_easy_steps_m,'No steps',4,"Manhattan Distance")

            data_4_easy_states_m = [[0 for i in range(5)],no_states_Beam_m[10][0],no_states_Beam_m[50][0],no_states_Beam_m[100][0]]
            generate_plot(data_4_easy_states_m,'No states',4,"Manhattan Distance")
        elif chose_problem_size == 5:

            data_5_easy_time_both = [[0 for i in range(5)],time_Beam_both[10][1],time_Beam_both[50][1],time_Beam_both[100][1]]
            generate_plot(data_5_easy_time_both,'Time (s)',5,"Manhattan Distance + no. inversions")

            data_5_easy_steps_both = [[0 for i in range(5)],[x for x in no_steps_Beam_both[10][1] if x != -7],[x for x in no_steps_Beam_both[50][1] if x != -7],[x for x in no_steps_Beam_both[100][1] if x != -7]]
            generate_plot(data_5_easy_steps_both,'No steps',5,"Manhattan Distance + no. inversions")

            data_5_easy_states_both = [[0 for i in range(5)],no_states_Beam_both[10][1],no_states_Beam_both[50][1],no_states_Beam_both[100][1]]
            generate_plot(data_5_easy_states_both,'No states',5,"Manhattan Distance + no. inversions")

            data_5_easy_time_m = [[0 for i in range(5)],time_Beam_m[10][1],time_Beam_m[50][1],time_Beam_m[100][1]]
            generate_plot(data_5_easy_time_m,'Time (s)',5,"Manhattan Distance")

            data_5_easy_steps_m = [[0 for i in range(5)],[x for x in no_steps_Beam_m[10][1] if x != -7],[x for x in no_steps_Beam_m[50][1] if x != -7],[x for x in no_steps_Beam_m[100][1] if x != -7]]
            generate_plot(data_5_easy_steps_m,'No steps',5,"Manhattan Distance")

            data_5_easy_states_m = [[0 for i in range(5)],no_states_Beam_m[10][1],no_states_Beam_m[50][1],no_states_Beam_m[100][1]]
            generate_plot(data_5_easy_states_m,'No states',5,"Manhattan Distance")

        elif chose_problem_size == 6:
            data_6_easy_time_both = [time_6_easy_both_GLDS,time_Beam_both[10][2],time_Beam_both[50][2],time_Beam_both[100][2]]
            generate_plot(data_6_easy_time_both,'Time (s)',6,"Manhattan Distance + no. inversions")
    
            data_6_easy_steps_both = [no_steps_6_easy_both_GLDS,no_steps_Beam_both[10][2],no_steps_Beam_both[50][2],no_steps_Beam_both[100][2]]
            generate_plot(data_6_easy_steps_both,'No steps',6,"Manhattan Distance + no. inversions")

            data_6_easy_states_both = [no_states_6_easy_both_GLDS,no_states_Beam_both[10][2],no_states_Beam_both[50][2],no_states_Beam_both[100][2]]
            generate_plot(data_6_easy_states_both,'No states',6,"Manhattan Distance + no. inversions")

            data_6_easy_time_m = [[0 for i in range(5)],time_Beam_m[10][2],time_Beam_m[50][2],time_Beam_m[100][2]]
            generate_plot(data_6_easy_time_m,'Time (s)',6,"Manhattan Distance")
    
            data_6_easy_steps_m = [[0 for i in range(5)],no_steps_Beam_m[10][2],no_steps_Beam_m[50][2],no_steps_Beam_m[100][2]]
            generate_plot(data_6_easy_steps_m,'No steps',6,"Manhattan Distance")

            data_6_easy_states_m = [[0 for i in range(5)],no_states_Beam_m[10][2],no_states_Beam_m[50][2],no_states_Beam_m[100][2]]
            generate_plot(data_6_easy_states_m,'No states',6,"Manhattan Distance")
        elif chose_problem_size == 7: ## 7 == 4-normal
            
            data_4_time_both = [time_4_both_GLDS,time_Beam_both[10][3],time_Beam_both[50][3],time_Beam_both[100][3]]
            generate_plot(data_4_time_both,'Time (s)',4,"Manhattan Distance + no. inversions")
    
            data_4_steps_both = [no_steps_4_both_GLDS,no_steps_Beam_both[10][3],no_steps_Beam_both[50][3],no_steps_Beam_both[100][3]]
            generate_plot(data_4_steps_both,'No steps',4,"Manhattan Distance + no. inversions")

            data_4_states_both = [no_states_4_both_GLDS,no_states_Beam_both[10][3],no_states_Beam_both[50][3],no_states_Beam_both[100][3]]
            generate_plot(data_4_states_both,'No states',4,"Manhattan Distance + no. inversions")

            data_4_time_m = [[0 for i in range(5)],time_Beam_m[10][3],time_Beam_m[50][3],time_Beam_m[100][3]]
            generate_plot(data_4_time_m,'Time (s)',4,"Manhattan Distance")
    
            data_4_steps_m = [[0 for i in range(5)],no_steps_Beam_m[10][3],no_steps_Beam_m[50][3],no_steps_Beam_m[100][3]]
            generate_plot(data_4_steps_m,'No steps',4,"Manhattan Distance")

            data_4_states_m = [[0 for i in range(5)],no_states_Beam_m[10][3],no_states_Beam_m[50][3],no_states_Beam_m[100][3]]
            generate_plot(data_4_states_m,'No states',4,"Manhattan Distance")

    else:
        b = 100
        tmp = data_BLDS[b]["4-easy"][0]
        print(tmp)
        blds_4_easy_time = [tmp[i] for i in range(len(tmp)) if (i + 1) % 3 == 0]
        blds_4_easy_steps = [tmp[i] for i in range(len(tmp)) if i % 3 == 0]
        blds_4_easy_state = [tmp[i] for i in range(len(tmp)) if (i + 2) % 3 == 0]
        print(blds_4_easy_time)
        print(blds_4_easy_state)
        print(blds_4_easy_steps)

        data_4_easy_time_both = [blds_4_easy_time,time_4_easy_both_GLDS,time_Beam_both[b][0]]
        generate_plot(data_4_easy_time_both,'Time (s)',4,"Manhattan Distance + no. inversions")

        data_4_easy_state_both = [blds_4_easy_state,no_states_4_easy_both_GLDS,no_states_Beam_both[b][0]]
        generate_plot(data_4_easy_state_both,'Number of states',4,"Manhattan Distance + no. inversions")

        data_4_easy_steps_both = [blds_4_easy_steps,no_steps_4_easy_both_GLDS,no_steps_Beam_both[b][0]]
        generate_plot(data_4_easy_steps_both,'Path len',4,"Manhattan Distance + no. inversions")

def create_stats_BLDS():
    solver_BLDS = BLDS()

    results = {}
    results[10] = {}
    results[50] = {}
    results[100] = {}
    results[500] = {}

    def solve_with_time(solver,problem_set,heuristic,b,limit):
        tbr = []
        for p in problem_set:
            start = time.time()
            res = solver.solve(p,heuristic,b,limit)
            end = time.time()
            tbr += [res[0],res[1],end - start]
        return tbr

    ## tuple in care primul element e lungimea caii si al doilea nr de stari folosite si ultimul timpul de rulare

    for b in [10,50,100,500]:
        res_4_easy_m = solve_with_time(solver_BLDS,problems_4_easy,NPuzzle.manhattan_distance,b,1000000)
        res_5_easy_m = solve_with_time(solver_BLDS,problems_5_easy,NPuzzle.manhattan_distance,b,1000000)
        res_6_easy_m = solve_with_time(solver_BLDS,problems_6_easy,NPuzzle.manhattan_distance,b,1000000)

        res_4_m = solve_with_time(solver_BLDS,problems_4,NPuzzle.manhattan_distance,b,1000000)
        res_5_m = solve_with_time(solver_BLDS,problems_5,NPuzzle.manhattan_distance,b,1000000)


        if b == 10:
            res_4_easy_both = solve_with_time(solver_BLDS,problems_4_easy[:3],NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_5_easy_both = solve_with_time(solver_BLDS,problems_5_easy[:2],NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_6_easy_both = solve_with_time(solver_BLDS,problems_6_easy,NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_4_both = solve_with_time(solver_BLDS,problems_4,NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_6_both = [(-1,-1,-1) for i in range(5)]
            res_5_both = [(-1,-1,-1) for i in range(5)]

            res_6_m = [(-1,-1,-1) for i in range(5)]            
        elif b == 50:
            res_4_easy_both = solve_with_time(solver_BLDS,problems_4_easy,NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_5_easy_both = [(-1,-1,-1) for i in range(5)]
            res_6_easy_both = solve_with_time(solver_BLDS,problems_6_easy[:3],NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_4_both = solve_with_time(solver_BLDS,problems_4,NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_6_both = [(-1,-1,-1) for i in range(5)]
            res_5_both = [(-1,-1,-1) for i in range(5)]


            res_6_m = solve_with_time(solver_BLDS,problems_6[:3],NPuzzle.manhattan_distance,b,1000000)
        
        elif b == 100:
            res_4_easy_both = solve_with_time(solver_BLDS,problems_4_easy,NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_5_easy_both = [(-1,-1,-1) for i in range(5)]
            res_6_easy_both = solve_with_time(solver_BLDS,problems_6_easy,NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_4_both = solve_with_time(solver_BLDS,problems_4,NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_6_both = [(-1,-1,-1) for i in range(5)]
            res_5_both = [(-1,-1,-1) for i in range(5)]


            res_6_m = solve_with_time(solver_BLDS,problems_6[:4],NPuzzle.manhattan_distance,b,1000000)
        
        elif b == 500:
            res_4_easy_both = solve_with_time(solver_BLDS,problems_4_easy,NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_5_easy_both = solve_with_time(solver_BLDS,problems_5_easy[:2],NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_6_easy_both = solve_with_time(solver_BLDS,problems_6_easy,NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_4_both = solve_with_time(solver_BLDS,problems_4,NPuzzle.manhattan_and_num_inversions,b,1000000)
            res_6_both = [(-1,-1,-1) for i in range(5)]
            res_5_both = [(-1,-1,-1) for i in range(5)]


            res_6_m = solve_with_time(solver_BLDS,problems_6[:4],NPuzzle.manhattan_distance,b,1000000)
        

        results[b]["4-easy"] = [res_4_easy_both,res_4_easy_m]
        results[b]["5-easy"] = [res_5_easy_both,res_5_easy_m]
        results[b]["6-easy"] = [res_6_easy_both,res_6_easy_m]

        results[b]["4"] = [res_4_both,res_4_m]
        results[b]["5"] = [res_5_both,res_5_m]
        results[b]["6"] = [res_6_both,res_6_m]


    np.save("BLDS_results",results)
    return results



def main():
    # run_stats_A_Star()
    # run_stats_Beam()
    # interpret_stats_A_star()
    # interpret_stats_Beam([1,10,50,100])
    # run_stats_GLDS()
    # interpret_stats_GLDS()
    # writer.save()
    # print(data_BLDS)
    # data_BLDS = create_stats_BLDS()
    # print(data_BLDS)
    beam_vs_GLDS_box_plot(4,mode="BLDS")


if __name__ == "__main__":
    main()