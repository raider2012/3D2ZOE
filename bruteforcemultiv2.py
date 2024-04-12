import csv

import numpy as np
import random
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

#Anirban Chakraborty

def read_triples_from_csv(file_path):

    triples = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 3:  # Ensure each row has exactly 3 elements
                triples.append(tuple(row))
    return triples


def generate_worst_case(num_triples=16):
    boys = [f"Boy_{i + 1}" for i in range(num_triples)]
    girls = [f"Girl_{i + 1}" for i in range(num_triples)]
    pets = [f"Pet_{i + 1}" for i in range(num_triples)]

    triples = list(zip(boys, girls, pets))
    random.shuffle(triples)  # Randomize the triples
    return triples


def evaluate_x_configuration(A, b, binary_rep):
    x = np.array([[int(digit)] for digit in binary_rep])
    if np.allclose(np.dot(A, x), b):
        return x
    return None


#Have a list of every binary representation of x given a size of n and see which x value gives a solution
def solve_for_x_multithreaded(A, b):
    n = A.shape[1]  # Number of variables
    binary_representations = [bin(i)[2:].zfill(n) for i in range(2 ** n)]

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(evaluate_x_configuration, A, b, rep) for rep in binary_representations]

        for future in as_completed(futures):
            result = future.result()
            if result is not None:
                return result
    return None


if __name__ == "__main__":
    start_time = time.time()  # Start time
    
    #working solution
    """triples = [('Boy_11', 'Girl_11', 'Pet_11'),
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
            ('Boy_13', 'Girl_13', 'Pet_13')]"""
    
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    #Chane the name of the csv as needed
    filename = "input.csv"  
    filepath = os.path.join(script_dir, filename)
    # Read triples from the CSV
    triples = read_triples_from_csv(filepath)
    print(triples)

    #triples = generate_worst_case(num_triples=32)

    #
    individuals = set(sum(triples, ()))
    individual_to_index = {ind: i for i, ind in enumerate(individuals)}
    A = np.zeros((len(individuals), len(triples)), dtype=int)
    for j, triple in enumerate(triples):
        for individual in triple:
            i = individual_to_index[individual]
            A[i, j] = 1

    b = np.ones(len(individuals))

    x_solution = solve_for_x_multithreaded(A, b)

    end_time = time.time()  # End time

    if np.any(x_solution):  # Check if any solution found
        print("Solution for x found.")
        matching_triples = [triples[i] for i in range(len(x_solution)) if x_solution[i] == 1]
        print("Matching triples:", matching_triples)
    else:
        print("No solution found.")

    print(f"Execution time: {end_time - start_time:.2f} seconds.")
