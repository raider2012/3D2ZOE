# 3D2ZOE
This solves a 3D Matching problem by converting the triples Set into a ZOE problem of the form A.x = b (column vector of 1s)
The solution to solve for x is either brute force or calculating the psuedo-inverse.

# INPUTS 
Both the solutions have same input sets:
2 csv files input.csv and size.csv both to be added under input/.
input/input.csv -> Contains rows with connections over each set in the form of triples (e.g: A_element1,B_element1,C_element1 is one row in the file).
input/size.csv -> Contains a single numerical value 'n' indicating the size of all thre sets.(|A|=|B|=|C|= the numerical value in the csv file).
input/input.csv can be generated using GenerateRandomInput.py but has a high chance of running into the EDGE CASES.

# The brute force solution : Project_3DTOZOE_Main.py  
This generates a list of every binary representation of x given a size of 'n' (variables) and see which x value gives a solution. 
Make sure memory is properly allocated for the Project_3DTOZOE_Main.py.

# The Pseudo-Inverse solution : Project_PseudoInverseMethod.py
This creates a pseudo-Inverse of matrix A using Singular Value Decomposition.
Finally, vector x is computed using A^{-1} . b

# EDGE CASES
1. INPUT size.csv not a numerical value.
2. INPUT input.csv doesnt connect all the elements in set A, B and C.
