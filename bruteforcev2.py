import numpy as np
from itertools import product

# Define the new set of 16 triples, probably should use csv input, code it later.
triples = [
    ('Boy_4', 'Girl_9', 'Pet_3'),
    ('Boy_14', 'Girl_11', 'Pet_7'),
    ('Boy_6', 'Girl_7', 'Pet_10'),
    ('Boy_10', 'Girl_1', 'Pet_6'),
    ('Boy_2', 'Girl_12', 'Pet_6'),
    ('Boy_2', 'Girl_6', 'Pet_4'),
    ('Boy_6', 'Girl_10', 'Pet_14'),
    ('Boy_10', 'Girl_1', 'Pet_5'),
    ('Boy_4', 'Girl_8', 'Pet_3'),
    ('Boy_9', 'Girl_5', 'Pet_4'),
    ('Boy_12', 'Girl_4', 'Pet_2'),
    ('Boy_9', 'Girl_2', 'Pet_1'),
    ('Boy_15', 'Girl_11', 'Pet_15'),
    ('Boy_11', 'Girl_2', 'Pet_3'),
    ('Boy_2', 'Girl_12', 'Pet_7'),
    ('Boy_3', 'Girl_4', 'Pet_2')
]

# Construct the A matrix
individuals = sorted(set(sum(triples, ())))
individual_to_index = {ind: i for i, ind in enumerate(individuals)}
A = np.zeros((len(individuals), len(triples)), dtype=int)
for j, triple in enumerate(triples):
    for individual in triple:
        i = individual_to_index[individual]
        A[i, j] = 1

# Define the b vector (Ax = b, where b is a vector of ones)
b = np.ones(len(individuals))

print(A)
print(b)

# Attempt to solve Ax = 1
def solve_for_x(A, b):
    n = A.shape[1]  # Number of variables
    for combo in product([0, 1], repeat=n):
        x = np.array(combo)
        if np.all(np.dot(A, x) == b):
            return x
    return None  # No solution found

x_solution = solve_for_x(A, b) 

if x_solution is not None: # Print out the solution
    print("Solution for x found:", x_solution)
    matching_triples = [triples[i] for i in range(len(x_solution)) if x_solution[i] == 1]
    print("Matching triples:", matching_triples)
else:
    print("No solution found.")
