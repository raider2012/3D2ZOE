import csv
import random
import pandas as pd

#Anirban Chakroborty
#Raghvesh Prasad

# Define file path
csv_path = "input/input.csv";
n = pd.read_csv("input/size.csv",header=None);
try:
    intn = int(n.iloc[0, 0]);
except ValueError:
    print("Invalid Set Sizes");

# Generate triples
boys = [f"Boy_{i+1}" for i in range(16)];
girls = [f"Girl_{i+1}" for i in range(16)];
pets = [f"Pet_{i+1}" for i in range(16)];

triples = [];
for _ in range(16):
    triple = (random.choice(boys), random.choice(girls), random.choice(pets));
    triples.append(triple);

# Write to CSV
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile);
    writer.writerows(triples);