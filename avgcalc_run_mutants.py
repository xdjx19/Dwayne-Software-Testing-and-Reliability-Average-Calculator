import subprocess
import os

# Define test sets for both MRs
tests = [
    # (MR type, original_input, transformed_input, relation_check)
    ("scaling", [1, 2, 3], [2, 4, 6], lambda o1, o2: abs(o2 - 2*o1) < 1e-6),
    ("permutation", [1, 2, 3], [3, 2, 1], lambda o1, o2: abs(o2 - o1) < 1e-6),
]

mutants_folder = "mutants_folder"
mutant_files = sorted(f for f in os.listdir(mutants_folder) if f.endswith(".py"))

results = []

for mutant in mutant_files:
    mutant_path = os.path.join(mutants_folder, mutant)
    mutant_killed = False
    
    for mr_name, src, follow, check in tests:
        # Run mutant with source input
        src_output = subprocess.check_output(["python", mutant_path], input=",".join(map(str, src)) + "\n", text=True)
        src_avg = float(src_output.strip().split()[-1])

        # Run mutant with follow-up input
        follow_output = subprocess.check_output(["python", mutant_path], input=",".join(map(str, follow)) + "\n", text=True)
        follow_avg = float(follow_output.strip().split()[-1])

        # Check relation
        if not check(src_avg, follow_avg):
            mutant_killed = True
            break  # No need to test further

    status = "Killed" if mutant_killed else "Survived"
    results.append((mutant, status))

# Print results
print("\nMutation Test Results:")
for m, s in results:
    print(f"{m:<15} -> {s}")
