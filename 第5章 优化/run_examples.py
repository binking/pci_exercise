# -*-coding: utf8 -*-
import time
import optimization


# Test print schedule
def test_print_schedule():
    # test_solution = [1,4,3,2,7,3,6,3,2,4,5,3]
    test_solution = [4, 3, 3, 3, 4, 3, 3, 4, 4, 0, 4, 1]
    optimization.printschedule(test_solution)
    print "=" * 20
    test_solution = [4, 3, 3, 3, 4, 3, 3, 0, 0, 0, 0, 0]
    optimization.printschedule(test_solution)

def test_get_minutes():
    test_time = "12:19"
    print optimization.getminutes(test_time)

def test_randomoptimize():
    """
    lowest cost: 3762
    :return: 
    """
    num_of_people = len(optimization.people)
    # test_domain = [(0,9) for _ in range(num_of_people * 2)]
    test_domain = [(0,9)] * (num_of_people * 2)
    for t in range(1000, 10000, 1000):
        epoch_time = time.time()
        solution = optimization.randomoptimize(test_domain, optimization.schedulecost, times=t)
        print "Using %d random samples, low cost is %.4f, and takes %.2f seconds" % (
            t, optimization.schedulecost(solution), time.time() - epoch_time)
# Lowest cost of random opt: 3047

def test_hillclimb():
    """
    [4, 6, 3, 7, 4, 6, 3, 6, 4, 6, 4, 6] 2452
    :return: 
    """
    try_times = 100
    history_solutions = []
    history_costs = []
    num_of_people = len(optimization.people)
    test_domain = [(0, 9) for _ in range(num_of_people * 2)]
    for i in range(try_times):
        print "run %d-th time" % i
        optimal_solu, low_cost = optimization.hillclimb(test_domain, optimization.schedulecost)
        history_solutions.append(optimal_solu)
        history_costs.append(low_cost)
    lowest_cost = min(history_costs)
    best_solu = history_solutions[history_costs.index(lowest_cost)]
    print best_solu, lowest_cost, optimization.schedulecost(best_solu)
    optimization.printschedule(best_solu)

def test_annealingoptimize():
    """
    [4.0, 5.0, 3.0, 7.0, 1.0, 5.0, 3.0, 5.0, 4.0, 5.0, 4.0, 6.0] 2903
    :return: 
    """
    try_times = 10
    history_solutions = []
    history_costs = []
    num_of_people = len(optimization.people)
    test_domain = [(0, 9) for _ in range(num_of_people * 2)]
    for i in range(try_times):
        print "Run %d time" % i
        optimal_solu, low_cost = optimization.annealingoptimize(test_domain, optimization.schedulecost)
        history_solutions.append(optimal_solu)
        history_costs.append(low_cost)
    lowest_cost = min(history_costs)
    best_solu = history_solutions[history_costs.index(lowest_cost)]
    print history_costs
    print best_solu, lowest_cost
    optimization.printschedule(best_solu)

def test_ga():
    """
    [2, 3, 0, 3, 1, 3, 2, 4, 2, 3, 2, 3] 2560
    [4, 5, 3, 5, 4, 5, 3, 6, 4, 5, 4, 6] 2533
    :return: 
    """
    num_of_people = len(optimization.people)
    test_domain = [(0, 9) for _ in range(num_of_people * 2)]
    ga_solution, ga_cost = optimization.geneticoptimize(
        test_domain, optimization.schedulecost, popsize=100, elite=0.2, step=1, maxiter=100, mutprob=0.5)
    print "\t", ga_solution, ga_cost
    optimization.schedulecost(ga_solution)
    optimization.printschedule(ga_solution)

if __name__ == '__main__':
    # test_print_schedule()
    # test_get_minutes()
    # test_randomoptimize()
    # test_hillclimb()
    test_annealingoptimize()
    test_ga()