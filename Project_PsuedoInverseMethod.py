import csv
import numpy as np

# READ CSV FILES
def read_adjacency_matrix_from_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile);
        matrix = [list(map(int, row)) for row in reader];
    return np.array(matrix);

#FIND ALL TRIPLES
def find_all_triples(adj_matrix_AB, adj_matrix_BC, adj_matrix_CA):
    triples = []
    for i in range(adj_matrix_AB.shape[0]):
        for j in range(adj_matrix_BC.shape[0]):
            for k in range(adj_matrix_CA.shape[0]):     
                if (adj_matrix_AB[i][j] == 1 and adj_matrix_BC[j][k] == 1 )  and (adj_matrix_BC[j][k] == 1 and adj_matrix_CA[k][i] == 1) :
                    triples.append((f"A{i+1}", f"B{j+1}", f"C{k+1}"));
    return triples

# CREATE TRIPLES MATRIX A (A.x = 1)
def create_Tuple_matrix(adj_matrix_AB, adj_matrix_BC, adj_matrix_CA):
    num_rows = adj_matrix_AB.shape[0] + adj_matrix_BC.shape[0] + adj_matrix_CA.shape[0];
    triples = find_all_triples(adj_matrix_AB, adj_matrix_BC, adj_matrix_CA);
    num_cols = len(triples);
    matrix_A = np.zeros((num_rows, num_cols), dtype=int);
    for i in range(num_cols):
        currA,currB,currC = triples[i]; 
        charA,numA = currA[0],int(currA[1:]);
        charB,numB = currB[0],int(currB[1:]);
        charC,numC = currC[0],int(currC[1:]);
        print(i,numA,numB,numC);
        matrix_A[numA-1][i]=1;
        matrix_A[adj_matrix_AB.shape[0]+numB-1][i]=1;
        matrix_A[adj_matrix_AB.shape[0] + adj_matrix_BC.shape[0]+numC-1][i]=1;
    return matrix_A,triples;


def matrixInverse(A):
    U, S, Vh = np.linalg.svd(A, full_matrices=False);
    S_inv = np.diag(1 / S);
    A_inv = Vh.T @ S_inv @ U.T;
    return A_inv;

def least_squares(inverseA, b):
    x = np.dot(inverseA,b);
    return x;

def main():
    adj_matrix_AB = read_adjacency_matrix_from_csv('setAB.csv');
    print("Matrix AB:");
    print(adj_matrix_AB);
    print(len(adj_matrix_AB));
    adj_matrix_BC = read_adjacency_matrix_from_csv('setBC.csv');
    print("Matrix BC:");
    print(adj_matrix_BC);
    adj_matrix_CA = read_adjacency_matrix_from_csv('setCA.csv');
    print("Matrix CA:");
    print(adj_matrix_CA);
    matrix_A,triples = create_Tuple_matrix(adj_matrix_AB,adj_matrix_BC,adj_matrix_CA)
    print("Matrix A:");
    print(matrix_A);
    inverseA = matrixInverse(matrix_A);
    print("MatrixA Inverse:");
    print(inverseA);
    b = np.ones((matrix_A.shape[0],1 ), dtype=int);
    x = least_squares(inverseA,b);
    print(x);
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