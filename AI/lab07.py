import operator
import math
import random
import numpy as np
from deap import algorithms, base, creator, tools, gp


# equation: 5X^3 - 6X^2 + 8X = 1
def equation(x):
    return 5 * x ** 3 - 6 * x ** 2 + 8 * x


# division operator, handling division by zero
def division_operator(numerator, denominator):
    if denominator == 0:
        return 1
    return numerator / denominator


# evaluation function
def eval_func(individual, points):
    func = toolbox.compile(expr=individual)
    errors = [(func(x) - equation(x)) ** 2 for x in points]
    return math.fsum(errors) / len(points),


# Create the DEAP toolbox
def create_toolbox():
    pset = gp.PrimitiveSet("MAIN", 1)
    pset.addPrimitive(operator.add, 2)
    pset.addPrimitive(operator.sub, 2)
    pset.addPrimitive(operator.mul, 2)
    pset.addPrimitive(division_operator, 2)
    pset.addPrimitive(operator.neg, 1)
    pset.addPrimitive(math.cos, 1)
    pset.addPrimitive(math.sin, 1)
    pset.addEphemeralConstant("rand101", lambda: random.randint(-1, 1))
    pset.renameArguments(ARG0='x')

    creator.create("FitnessMin", base.Fitness, weights =(-1.0,))
    creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("compile", gp.compile, pset=pset)
    toolbox.register("evaluate", eval_func, points=[x / 10. for x in range(-10, 10)])
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
    toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
    toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

    return toolbox


if __name__ == "__main__":
    random.seed(7)

    # Create the toolbox
    toolbox = create_toolbox()

    # Initialize the population
    population = toolbox.population(n=450)

    # Create the hall of fame to store the best individual
    hall_of_fame = tools.HallOfFame(1)

    # Create statistics for tracking the evolution
    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    stats_size = tools.Statistics(len)
    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
    mstats.register("avg", np.mean)
    mstats.register("std", np.std)
    mstats.register("min", np.min)
    mstats.register("max", np.max)

    # Set the probability of crossover and mutation
    probab_crossover = 0.4
    probab_mutate = 0.2
    # Set the number of generations
    number_gen = 10
    # Run the evolutionary algorithm
    algorithms.eaSimple(population, toolbox, cxpb=probab_crossover, mutpb=probab_mutate,
                        ngen=number_gen, stats=mstats, halloffame=hall_of_fame, verbose=True)

    # Select new population
    selected = toolbox.select(population, len(population))
    population = [toolbox.clone(individual) for individual in selected]

    # Apply crossover and mutation
    for individual in population:
        if random.random() < probab_crossover:
            toolbox.mate(individual, selected[0])
        if random.random() < probab_mutate:
            toolbox.mutate(individual)

    # Retrieve the best individual from the hall of fame
    best_individual = hall_of_fame[0]
    best_expression = toolbox.compile(expr=best_individual)
    print("Best Individual Expression:")
    print(best_expression)
