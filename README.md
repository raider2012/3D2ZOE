# 3D2ZOE
This solves a 3D Matching problem by converting the triples Set into a ZOE problem of the form A.x = b (column vector of 1s)

The solution to solve for x is either brute force or calculating the psuedo-inverse.

The brute force solution in bruteforcemultiv2.py is the latest script to include csv input of any triple input, as long as
the csv is delineated by 3 seperate variables. Version 2 of brute force generates a list of every binary representation
of x given a size of n (variables) and see which x value gives a solution. Make sure memory is properly allocated for
the bruteforcemultiv2.py.

The csv name can be changed in bruteforcemultiv2.py to whatever you need to test. Make sure the csv is in the same 
directory as the script.
