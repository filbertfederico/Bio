import re
import tkinter
import os
import random
import time

start_time = time.time()

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
            print(gene_sequence)
        elif reg_input == 3:
            gene_sequence = "hooman/haplogroup I1c.txt"
            print(gene_sequence)
        elif reg_input == 4:
            gene_sequence = "hooman/haplogroup K1a.txt"
            print(gene_sequence)
        elif reg_input == 5:
            gene_sequence = "hooman/haplogroup U3a.txt"
            print(gene_sequence)
        elif reg_input == 6:
            gene_sequence = "hooman/haplogroup K2b1.txt"
            print(gene_sequence)
        elif reg_input == 7:
            gene_sequence = "hooman/haplogroup T2b.txt"
            print(gene_sequence)
        elif reg_input == 8:
            gene_sequence = "hooman/haplogroup D1g.txt"
            print(gene_sequence)
        elif reg_input == 9:
            gene_sequence = "hooman/haplogroup R0a2m.txt"
            print(gene_sequence)
        elif reg_input == 10:
            gene_sequence = "hooman/homoSapiensGene.txt"
            print(gene_sequence)
        elif reg_input == 11:
            gene_sequence = "gene/adenomatous polyposis coli.txt"
            print(gene_sequence)
        elif reg_input == 12:
            gene_sequence = "gene/antithrombin.txt"
            print(gene_sequence)
        elif reg_input == 13:
            gene_sequence = "gene/Apolipoprotein E.txt"
            print(gene_sequence)
        elif reg_input == 14:
            gene_sequence = "gene/Cystic fibrosis.txt"
            print(gene_sequence)
        elif reg_input == 15:
            gene_sequence = "gene/hemophilia A.txt"
            print(gene_sequence)
        elif reg_input == 16:
            gene_sequence = "gene/hemophilia B.txt"
            print(gene_sequence)
        elif reg_input == 17:
            gene_sequence = "gene/insulin receptor.txt"
            print(gene_sequence)
        elif reg_input == 18:
            gene_sequence = "gene/lipoprotein lipase.txt"
            print(gene_sequence)
        elif reg_input == 19:
            gene_sequence = "gene/steroid 21-hydroxylase.txt"
            print(gene_sequence)
        else:
            print("Invalid input")

    elif input_gene == 2:
        # User input for a custom genome sequence
        gene_sequence = input("Enter the human genome sequence (in FASTA format): ")

    else:
        print("Invalid option")

select_gene_sequence(input_gene)

#regex pattern matching algorithm
def find_patterns_all(gene_sequence, patterns):
    with open(gene_sequence, 'r') as file:
        gene_sequence = file.read().replace('\n', '')
    total_length = len(gene_sequence)
    results_all = {}

    for pattern in patterns:
        matches = re.findall(pattern, gene_sequence)
        match_length = len(matches)
        percentage = (match_length / total_length) * 100
        expected_percentage = expected_results.get(pattern, {}).get('percentage', 0)

        results_all[pattern] = {
            'matches': matches,
            'percentage': percentage,
            'expected_percentage' : expected_percentage
        }
    return results_all

expected_results = {
    'TTT': {'matches': 192, 'percentage': 3.476371537208039},
    'TTC': {'matches': 308, 'percentage': 5.576679340937896},
    'TTA': {'matches': 329, 'percentage': 5.9569074778200255},
    'TTG': {'matches': 116, 'percentage': 2.100307803729857},
    'TCT': {'matches': 288, 'percentage': 5.2145573058120585},
    'TCC': {'matches': 361, 'percentage': 6.5363027340213655},
    'TCA': {'matches': 415, 'percentage': 7.514032228861126},
    'TCG': {'matches': 121, 'percentage': 2.190838312511316},
    'TAT': {'matches': 304, 'percentage': 5.504254933912729},
    'TAC': {'matches': 377, 'percentage': 6.826000362122035},
    'TAA': {'matches': 414, 'percentage': 7.495926127104835},
    'TAG': {'matches': 258, 'percentage': 4.671374253123303},
    'TGT': {'matches': 99, 'percentage': 1.7925040738728952},
    'TGC': {'matches': 123, 'percentage': 2.2270505160239003},
    'TGA': {'matches': 190, 'percentage': 3.4401593336954557},
    'TGG': {'matches': 99, 'percentage': 1.7925040738728952},
    'CTT': {'matches': 318, 'percentage':5.757740358500815},
    'CTC': {'matches': 395, 'percentage':7.151910193735289},
    'CTA': {'matches': 523, 'percentage':9.469491218540648},
    'CTG': {'matches': 180, 'percentage':3.259098316132537},
    'CCT': {'matches': 542, 'percentage':9.813507151910192},
    'CCC': {'matches': 411, 'percentage':7.441607821835959},
    'CCA': {'matches': 464, 'percentage':8.401231214919427},
    'CCG': {'matches': 141, 'percentage':2.552960347637154},
    'CAT': {'matches': 416, 'percentage':7.532138330617418},
    'CAC': {'matches': 418, 'percentage':7.568350534130001},
    'CAA': {'matches': 465, 'percentage':8.419337316675719},
    'CAG': {'matches': 199, 'percentage':3.6031142495020827},
    'CGT': {'matches': 78, 'percentage':1.4122759369907658},
    'CGC': {'matches': 155, 'percentage':2.80644577222524},
    'CGA': {'matches': 122, 'percentage':2.2089444142676085},
    'CGG': {'matches': 80, 'percentage':1.4484881405033496},
    'ATT': {'matches': 330, 'percentage': 5.975013579576317},
    'ATC': {'matches': 371, 'percentage': 6.7173637515842834},
    'ATA': {'matches': 348, 'percentage': 6.300923411189571},
    'ATG': {'matches': 162, 'percentage': 2.9331884845192833},
    'ACT': {'matches': 412, 'percentage': 7.459713923592251},
    'ACC': {'matches': 515, 'percentage': 9.324642404490312},
    'ACA': {'matches': 409, 'percentage': 7.405395618323375},
    'ACG': {'matches': 119, 'percentage': 2.1546261089987326},
    'AAT': {'matches': 376, 'percentage': 6.807894260365743},
    'AAC': {'matches': 495, 'percentage': 8.962520369364475},
    'AAA': {'matches': 361, 'percentage': 6.5363027340213655},
    'AAG': {'matches': 209, 'percentage': 3.7841752670650006},
    'AGT': {'matches': 161, 'percentage': 2.915082382762991},
    'AGC': {'matches': 282, 'percentage': 5.105920695274308},
    'AGA': {'matches': 173, 'percentage': 3.1323556038384934},
    'AGG': {'matches': 174, 'percentage': 3.1504617055947857},
    'GTT': {'matches': 104, 'percentage': 1.8830345826543544},
    'GTC': {'matches': 106, 'percentage': 1.9192467861669382},
    'GTA': {'matches': 154, 'percentage': 2.788339670468948},
    'GTG': {'matches': 53, 'percentage': 0.9596233930834691},
    'GCT': {'matches': 179, 'percentage': 3.2409922143762446},
    'GCC': {'matches': 271, 'percentage': 4.906753575955096},
    'GCA': {'matches': 207, 'percentage': 3.7479630635524175},
    'GCG': {'matches': 52, 'percentage': 0.9415172913271772},
    'GAT': {'matches': 114, 'percentage': 2.0640956002172732},
    'GAC': {'matches': 169, 'percentage': 3.0599311968133263},
    'GAA': {'matches': 201, 'percentage': 3.639326453014666},
    'GAG': {'matches': 126, 'percentage': 2.2813688212927756},
    'GGT': {'matches': 80, 'percentage': 1.4484881405033496},
    'GGC': {'matches': 151, 'percentage': 2.734021365200072},
    'GGA': {'matches': 122, 'percentage': 2.2089444142676085},
    'GGG': {'matches': 58, 'percentage': 1.0501539018649284}
}

def find_patterns_with_comparison(gene_sequence, patterns):
    with open(gene_sequence, 'r') as file:
        gene_sequence = file.read()

    total_length = len(gene_sequence)

    results = {}
    for pattern in patterns:
        matches = re.findall(pattern, gene_sequence)
        match_length = len(matches)
        percentage = (match_length / total_length) * 100

        # Compare obtained results with expected values
        expected_percentage = expected_results.get(pattern, {}).get('percentage', 0)

        if percentage > expected_percentage:
            results[pattern] = {
                'matches': matches,
                'percentage': percentage,
            }

    return results

#KMP Knuth-Morris-Prat
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix values for pattern
    lps = [0] * M
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            return i - j

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0] = 0  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1# Find patterns using KMP algorithm
def find_patterns_with_KMP(gene_sequence, patterns):
    with open(gene_sequence, 'r') as file:
        gene_sequence = file.read()

    results = {}
    for pattern in patterns:
        matches = []
        pos = KMPSearch(pattern, gene_sequence)
        while pos != -1:
            matches.append(pos)
            pos = KMPSearch(pattern, gene_sequence[pos + 1:])
            if pos != -1:
                pos += matches[-1] + 1

        results[pattern] = {
            'matches': matches,
            'count': len(matches),
        }

    return results

# Boyer-Moore algorithm for pattern searching
def searchBoyerMoore(txt, pat):
    M = len(pat)
    N = len(txt)

    # Initialize bad character skip array
    bad_char = [-1] * 256

    # Fill the bad character skip array
    for i in range(M):
        bad_char[ord(pat[i])] = i

    # Searching the pattern using bad character skip
    s = 0
    matches = []
    while s <= N - M:
        j = M - 1

        # Checking from right to left
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        if j < 0:
            matches.append(s)
            s += (M - bad_char[ord(txt[s + M])] if s + M < N else 1)
        else:
            s += max(1, j - bad_char[ord(txt[s + j])])

    return matches

# Function to find patterns using Boyer-Moore algorithm
def find_patterns_with_BoyerMoore(gene_sequence, patterns):
    with open(gene_sequence, 'r') as file:
        gene_sequence = file.read()

    results = {}
    for pattern in patterns:
        matches = searchBoyerMoore(gene_sequence, pattern)
        results[pattern] = {
            'matches': matches,
            'count': len(matches),
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
            'GGT', 'GGC', 'GGA', 'GGG']


# Print comparison
results_comparison = find_patterns_with_comparison(gene_sequence, patterns)
for pattern, result in results_comparison.items():
    if 'expected_percentage' in result:
        print(f"Pattern: {pattern}, Found {len(result['matches'])} matches, Percentage: {result['percentage']}%, Expected Percentage: {result['expected_percentage']}")
    else:
        print(f"Pattern: {pattern}, Found {len(result['matches'])} matches, Percentage: {result['percentage']}%, Expected Percentage: Not available")
print("--------------------------------------------------------------------")
print("regex algo:")
results_all = find_patterns_all(gene_sequence, patterns)
for pattern, result in results_all.items():
    print(f"Pattern: {pattern}, Found {len(result['matches'])} matches, Percentage: {result['percentage']}%")
print("-----------------------------------------------------")
print("KMP algo:")
results_KMP = find_patterns_with_KMP(gene_sequence, patterns)
for pattern, result in results_KMP.items():
    print(f"Pattern: {pattern}, Found {result['count']}")
print("-----------------------------------------------------")
print("BoyerMoore algo")
results_BoyerMoore = find_patterns_with_BoyerMoore(gene_sequence, patterns)
for pattern, result in results_BoyerMoore.items():
    print(f"Pattern: {pattern}, Found {result['count']}")

print("-----------------------------------------------------")

# # Perform comparison
# comparison_results = compare_results(results_all, results_KMP, results_BoyerMoore)

# # Display comparison results
# for pattern, result in comparison_results.items():
#     print(f"Pattern: {pattern}, Comparison: {result}")

def calculate_accuracy_per_pattern(expected, algorithm_results):
    accuracy_per_pattern = {}
    for pattern, result in algorithm_results.items():
        expected_matches = expected.get(pattern, {}).get('matches', 0)
        algorithm_matches = len(result['matches']) if 'matches' in result else 0

        if expected_matches > 0:
            accuracy = (algorithm_matches / expected_matches) * 100
        else:
            accuracy = 0
        
        accuracy_per_pattern[pattern] = accuracy
    
    return accuracy_per_pattern

# Calculate accuracy per pattern for each algorithm
accuracy_regex_per_pattern = calculate_accuracy_per_pattern(expected_results, results_all)
accuracy_KMP_per_pattern = calculate_accuracy_per_pattern(expected_results, results_KMP)
accuracy_BoyerMoore_per_pattern = calculate_accuracy_per_pattern(expected_results, results_BoyerMoore)

# Display comparison per pattern
for pattern, accuracy in accuracy_regex_per_pattern.items():
    print(f"Pattern: {pattern}, Regex Accuracy: {accuracy:.2f}% | KMP Accuracy: {accuracy_KMP_per_pattern[pattern]:.2f}% | Boyer-Moore Accuracy: {accuracy_BoyerMoore_per_pattern[pattern]:.2f}%")

# Record the end time
end_time = time.time()

# Calculate the total time taken
execution_time = end_time - start_time

print(f"Total execution time: {execution_time} seconds")