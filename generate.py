# Generating and writing to CSV directly, without any additional script detail

import csv
import random

# Define file path
csv_path = 'C:/Users/Anirban Chakraborty/Documents/GitHub/3D2ZOE/input.csv'

# Generate 32 triples
boys = [f"Boy_{i+1}" for i in range(16)]
girls = [f"Girl_{i+1}" for i in range(16)]
pets = [f"Pet_{i+1}" for i in range(16)]

triples = []
for _ in range(16):
    triple = (random.choice(boys), random.choice(girls), random.choice(pets))
    triples.append(triple)

# Write to CSV
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(triples)

csv_path
