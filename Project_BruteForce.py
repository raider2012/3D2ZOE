import csv
import numpy as np


# READ CSV FILES
def read_adjacency_matrix_from_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile);
        matrix = [list(map(int, row)) for row in reader];
    return np.array(matrix);


# FIND ALL TRIPLES
def find_all_triples(adj_matrix_AB, adj_matrix_BC, adj_matrix_CA):
    triples = []
    for i in range(adj_matrix_AB.shape[0]):
        for j in range(adj_matrix_BC.shape[0]):
            for k in range(adj_matrix_CA.shape[0]):
                if (adj_matrix_AB[i][j] == 1 and adj_matrix_BC[j][k] == 1) and (
                        adj_matrix_BC[j][k] == 1 and adj_matrix_CA[k][i] == 1):
                    triples.append((f"A{i + 1}", f"B{j + 1}", f"C{k + 1}"));
    return triples


# CREATE TRIPLES MATRIX A (A.x = 1)
def create_Tuple_matrix(adj_matrix_AB, adj_matrix_BC, adj_matrix_CA):
    num_rows = adj_matrix_AB.shape[0] + adj_matrix_BC.shape[0] + adj_matrix_CA.shape[0];
    triples = find_all_triples(adj_matrix_AB, adj_matrix_BC, adj_matrix_CA);
    num_cols = len(triples);
    matrix_A = np.zeros((num_rows, num_cols), dtype=int);
    for i in range(num_cols):
        currA, currB, currC = triples[i];
        charA, numA = currA[0], int(currA[1:]);
        charB, numB = currB[0], int(currB[1:]);
        charC, numC = currC[0], int(currC[1:]);
        matrix_A[numA - 1][i] = 1;
        matrix_A[adj_matrix_AB.shape[0] + numB - 1][i] = 1;
        matrix_A[adj_matrix_AB.shape[0] + adj_matrix_BC.shape[0] + numC - 1][i] = 1;
    return matrix_A, triples;


def bruteForceX(A, b):
    # Start with x = column vectors of all 0
    x = np.zeros((A.shape[1], 1));
    # loop ove 2^n (NP COMPLETE PROBLEM)
    for i in range(2 ** x.shape[0]):
        binary_rep = bin(i)[2:].zfill(x.shape[0]);
        # changing x using the above binary number
        x = np.array([[int(digit)] for digit in binary_rep]);
        # Check if A.x = b
        if np.allclose(np.dot(A, x), b):
            return x;

    return np.zeros((A.shape[1], 1));


def main():
    adj_matrix_AB = read_adjacency_matrix_from_csv('setAB.csv');
    print("Matrix AB:");
    print(adj_matrix_AB);
    adj_matrix_BC = read_adjacency_matrix_from_csv('setBC.csv');
    print("Matrix BC:");
    print(adj_matrix_BC);
    adj_matrix_CA = read_adjacency_matrix_from_csv('setCA.csv');
    print("Matrix CA:");
    print(adj_matrix_CA);
    matrix_A, triples = create_Tuple_matrix(adj_matrix_AB, adj_matrix_BC, adj_matrix_CA)
    print("Matrix A:");
    print(matrix_A);

    b = np.ones((matrix_A.shape[0], 1), dtype=int);
    x = bruteForceX(matrix_A, b);

    if (np.all(x == 0)):
        print("No Solutions found.");
        return;

    print(x);

    print("Triples Set T = ", triples);
    indexesM = [];
    tripleSoln = [];
    for i in range(len(x)):
        if (x[i][0] == 1):
            indexesM.append(i);

    for i in range(len(indexesM)):
        tripleSoln.append(triples[indexesM[i]]);
    print("Distinct Triples Set M = ", tripleSoln);


if __name__ == "__main__":
    main();
