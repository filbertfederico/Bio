import re
import tkinter
import os
import random

print("Human Codon Mutation")
print("1: Pick preselected human genome")
print("2: input human genome(fasta)")
input_gene = int(input("pick an option: "))

def select_gene_sequence(input_gene):
    global gene_sequence  # Declare gene_sequence as a global variable

    if input_gene == 1: 
        print("1. Random")
        print("2. Mediterranian")
        print("3. Nordic")
        print("4. West Europe")
        print("5. Caucasus and North Africa")
        print("6. Oceania")
        print("7. Middle East-Iran")
        print("8. Middle East-Arab Peninsula")
        print("9. Central and Northeast Asia")

        reg_input = int(input("Pick a region: "))
        if reg_input == 1:
            directory = "gene/" 
            files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
            random_file = random.choice(files)
            gene_sequence = random_file  # Set gene_sequence to the randomly chosen file
            print("Random file: ", random_file)
        elif reg_input == 2:
            gene_sequence = "hooman/haplogroup HV-T16311C.txt"
        elif reg_input == 3:
            gene_sequence = "hooman/haplogroup I1c.txt"
        elif reg_input == 4:
            gene_sequence = "hooman\haplogroup K1a.txt"
        elif reg_input == 5:
            gene_sequence = "hooman\haplogroup U3a.txt"
        elif reg_input == 6:
            gene_sequence = "hooman\haplogroup K2b1.txt"
        elif reg_input == 7:
            gene_sequence = "hooman\haplogroup T2b.txt"
        elif reg_input == 8:
            gene_sequence = "hooman\haplogroup D1g.txt"
        elif reg_input == 9:
            gene_sequence = "hooman/haplogroup R0a2m.txt"
        else:
            print("Invalid input")

# Assuming you call the function somewhere in your code
select_gene_sequence(input_gene)

def find_patterns(gene_sequence, patterns):
    with open(gene_sequence, 'r') as file:
        gene_sequence = file.read()

    total_length = len(gene_sequence)
    results = {}

    for pattern in patterns:
        matches = re.findall(pattern, gene_sequence)
        match_length = len(''.join(matches))
        percentage = (match_length / total_length) * 100
        results[pattern] = {
            'matches': matches,
            'percentage': percentage
        }

    return results

# pattern usage:
patterns = ['TTT', 'TTC', 'TTA', 'TTG',
            'TCT', 'TCC', 'TCA', 'TCG',
            'TAT', 'TAC', 'TAA', 'TAG',
            'TGT', 'TGC', 'TGA', 'TGG',
            'CTT', 'CTC', 'CTA', 'CTG',
            'CCT', 'CCC', 'CCA', 'CCG',
            'CAT', 'CAC', 'CAA', 'CAG',
            'CGT', 'CGC', 'CGA', 'CGG',
            'ATT', 'ATC', 'ATA', 'ATG',
            'ACT', 'ACC', 'ACA', 'ACG',
            'AAT', 'AAC', 'AAA', 'AAG',
            'AGT', 'AGC', 'AGA', 'AGG',
            'GTT', 'GTC', 'GTA', 'GTG',
            'GCT', 'GCC', 'GCA', 'GCG',
            'GAT', 'GAC', 'GAA', 'GAG',
            'GGT', 'GGC', 'GGA', 'GGG',]  # These are the patterns we're looking for

results = find_patterns(gene_sequence, patterns)
for pattern, result in results.items():
    print(f"Pattern: {pattern}, Found {len(result['matches'])} match(es), Percentage: {result['percentage']}%")