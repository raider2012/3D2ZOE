import numpy as np
from itertools import product

#Anirban Chakraborty

# Define the new set of 16 triples, probably should use csv input, code it later. Need to have several inputs
# testing edge cases

#working solution
triples = [('Boy_11', 'Girl_11', 'Pet_11'),
           ('Boy_5', 'Girl_5', 'Pet_5'),
           ('Boy_10', 'Girl_10', 'Pet_10'),
           ('Boy_7', 'Girl_7', 'Pet_7'),
           ('Boy_8', 'Girl_8', 'Pet_8'),
           ('Boy_12', 'Girl_12', 'Pet_12'),
           ('Boy_9', 'Girl_9', 'Pet_9'),
           ('Boy_4', 'Girl_4', 'Pet_4'),
           ('Boy_1', 'Girl_1', 'Pet_1'),
           ('Boy_6', 'Girl_6', 'Pet_6'),
           ('Boy_3', 'Girl_3', 'Pet_3'),
           ('Boy_15', 'Girl_15', 'Pet_15'),
           ('Boy_14', 'Girl_14', 'Pet_14'),
           ('Boy_16', 'Girl_16', 'Pet_16'),
           ('Boy_2', 'Girl_2', 'Pet_2'),
           ('Boy_13', 'Girl_13', 'Pet_13')]

# Construct the A matrix, and set the value to 1 if the element is part of a triple
individuals = sorted(set(sum(triples, ())))
individual_to_index = {ind: i for i, ind in enumerate(individuals)}
A = np.zeros((len(individuals), len(triples)), dtype=int)
for j, triple in enumerate(triples):
    for individual in triple:
        i = individual_to_index[individual]
        A[i, j] = 1

# Define the b vector (Ax = b, where b is a vector of 1s)
b = np.ones(len(individuals))

print(A)
print(b)


# Attempt to solve Ax = 1 by brute forcing every dot product of A * x until every product equals 1 in each row.
def solve_for_x(A, b):
    n = A.shape[1]  # Number of variables
    for combo in product([0, 1], repeat=n):
        x = np.array(combo)
        if np.all(np.dot(A, x) == b):
            return x
    return None  # No solution found


if __name__ == "__main__":
    x_solution_normal = solve_for_x(A, b)

    if x_solution_normal is not None:  # Print out the solution, or no solution
        print("Solution for x found:", x_solution_normal)
        matching_triples = [triples[i] for i in range(len(x_solution_normal)) if x_solution_normal[i] == 1]
        print("Matching triples:", matching_triples)
    else:
        print("No solution found.")
