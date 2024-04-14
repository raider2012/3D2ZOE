import csv
import numpy as np
import pandas as pd
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


# READ INPUT FILE
def read_triples_from_csv(file_path):
    triples = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 3:  # Ensure each row has exactly 3 elements
                triples.append(tuple(row))
    return triples

def matrixInverse(A):
    U, S, Vh = np.linalg.svd(A, full_matrices=False);
    S_inv = np.diag(1 / S);
    A_inv = Vh.T @ S_inv @ U.T;
    return A_inv;

def least_squares(inverseA, b):
    x = np.dot(inverseA,b);
    return x;

def main():
    #Input Files
    inputFile = 'input/input_working.csv';
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
    triples = read_triples_from_csv(inputFile);
    print(triples);

    individuals = set(sum(triples, ()))
    individual_to_index = {ind: i for i, ind in enumerate(individuals)}
    matrix_A = np.zeros((len(individuals), len(triples)), dtype=int)
    for j, triple in enumerate(triples):
        for individual in triple:
            i = individual_to_index[individual]
            matrix_A[i, j] = 1 
    
    print(matrix_A)
    endReadInput = time.time();
    print(f"Matrix A created, time taken : {endReadInput-startReadInput:.2f} seconds.");

    startPsuedoInv = time.time();
    inverseA = matrixInverse(matrix_A);
    print("MatrixA Inverse:");
    print(inverseA);
    print(inverseA.shape)
    b = np.ones((matrix_A.shape[0],1 ), dtype=int);
    print(b.shape)
    x = least_squares(inverseA,b);
    print(x);
    endPsuedoInv = time.time();
    print(f"Matrix A created, time taken : {endPsuedoInv-startPsuedoInv:.2f} seconds.");

    indexesM = [];
    tripleSoln = [];
    for i in range(x.shape[0]):
        if (abs(x[i][0]-1)<1e-6):
            indexesM.append(i);
    
    for i in range(len(indexesM)):
        tripleSoln.append(triples[indexesM[i]]);
    print("Triples Set T = " , triples);
    print("Distinct Triples Set M = ",tripleSoln);
    

if __name__ == "__main__":
    main();