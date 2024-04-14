import pandas as pd
import csv
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

#Anirban Chakroborty
#Raghvesh Prasad

def basecheck(inputFile,sizeFile):
    n = pd.read_csv(sizeFile,header=None);
    try:
        intn = int(n.iloc[0, 0]);
    except ValueError:
        return "SIZE";
    
    df = pd.read_csv(inputFile, header=None);
    setA = df.iloc[:, 0].values;
    setB = df.iloc[:, 1].values;
    setC = df.iloc[:, 2].values;

    if(len(set(setA)) > intn or len(set(setA)) < intn):
        return "SIZEA";
    if(len(set(setB)) > intn or len(set(setB)) < intn):
        return "SIZEB";
    if(len(set(setC)) > intn or len(set(setC)) < intn):
        return "SIZEC";
    if(len(set(setA))==len(set(setB))==len(set(setC))==intn):
        return "SUCCESS";
    else:
        return "FAILURE";

def read_triples_from_csv(file_path):
    triples = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 3:  # Ensure each row has exactly 3 elements
                triples.append(tuple(row))
    return triples

def evaluate_x(A, b, binary_rep):
    x = np.array([[int(digit)] for digit in binary_rep]);
    if np.allclose(np.dot(A, x), b):
        return x;
    return None;


#Have a list of every binary representation of x given a size of n and see which x value gives a solution i,e satisfies Ax = 1
#Waits for the first solution available, or if all returns None, than no solution is available.
# Attempt to solve Ax = 1 by brute forcing every dot product of A * x until every product equals 1 in each row.

#Multithreaded
def solve_for_x_multithreaded(A, b):
    n = A.shape[1];  # Number of variables
    binary_representations = [bin(i)[2:].zfill(n) for i in range(2 ** n)];
    results = [];
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(evaluate_x, A, b, rep) for rep in binary_representations];
        for future in as_completed(futures):
            result = future.result();
            if result is not None:
                results.append(result);
    
    if results:
        return results[0];
    else:
        return None;

#Bruteforce
def solve_for_x(A, b):
    #Start with x = column vectors of all 0
    x = np.zeros((A.shape[1], 1));
    #loop ove 2^n (NP COMPLETE PROBLEM)
    for i in range(2**x.shape[0]):
        binary_rep = bin(i)[2:].zfill(x.shape[0]);
        #changing x using the above binary number
        x = np.array([[int(digit)] for digit in binary_rep]);
        # Check if A.x = b
        if np.allclose(np.dot(A, x), b):
            return x;
    return None;

def main():
    #Input Files
    inputFile = "input/input.csv";
    sizeFile = "input/size.csv";
    
    #Base Validations
    startBaseValidation = time.time();
    eval = basecheck(inputFile,sizeFile)
    if(eval == "FAILURE"):
        print("No Soultions available, All elements are not connected.");
        return;
    elif(eval == "SIZE"):
        print("INPUT SIZE ERROR, please correct size.csv");
        return;
    elif(eval == "SIZEA"):
        print("SET A not completely connected, please correct input.csv");
        return;
    elif(eval == "SIZEB"):
        print("SET B not completely connected, please correct input.csv");
        return;
    elif(eval == "SIZEC"):
        print("SET C not completely connected, please correct input.csv");
        return;
    endBaseValidation = time.time();
    print(f"Base Validation successfull, time taken : {endBaseValidation-startBaseValidation:.2f} seconds.");
    
    #Read Input
    startReadInput = time.time();
    triples = read_triples_from_csv(inputFile)
    print(triples)
    #Transformation of input from triples to 0-1 Matrix for ZOE.
    individuals = set(sum(triples, ()));
    individual_to_index = {ind: i for i, ind in enumerate(individuals)};
    A = np.zeros((len(individuals), len(triples)), dtype=int);
    for j, triple in enumerate(triples):
        for individual in triple:
            i = individual_to_index[individual];
            A[i, j] = 1; #If the variable is involved in the triple.
            #Always three 1s in a column(definition of triple), and at least one '1' in a row
    print(A);
    endReadInput = time.time();
    print(f"Matrix A created, time taken : {endReadInput-startReadInput:.2f} seconds.");
    #b = column vecotrs of all 1s
    b = np.ones(len(individuals));

    #Normal Brute Force method, should take longer as it computes dot product from top to bottom.
    startBF = time.time();
    x_solution_normal = solve_for_x(A, b)

    if x_solution_normal is not None:  # Check if any solution found, if so, transfrom input back into triples and returns the distinct triples back
        print("Solution for x found:", x_solution_normal);
        matching_triples = [triples[i] for i in range(len(x_solution_normal)) if x_solution_normal[i] == 1];
        print("Matching triples:", matching_triples);
    else:
        print("No solution found.");
        print(x_solution_normal);
    endBF = time.time();
    print(f"Brute Force execution time: {endBF - startBF:.2f} seconds.");

    print("Now starting Multithreaded version");
    # Multithreaded Brute Force
    startMultiThreadedBF = time.time();
    x_solution = solve_for_x_multithreaded(A, b);
    if np.any(x_solution):  # Check if any solution found, if so, transfrom input back into triples and returns the distinct triples back
        print("Solution for x found:", x_solution);
        print("Solution for x found.");
        matching_triples = [triples[i] for i in range(len(x_solution)) if x_solution[i] == 1];
        print("Matching triples:", matching_triples);
    else:
        print("No solution found.");
        print(x_solution);
    endMultiThreadedBF = time.time();
    print(f"Multithreaded Brute Force execution time: {endMultiThreadedBF - startMultiThreadedBF:.2f} seconds.");

if __name__ == "__main__":
    main();