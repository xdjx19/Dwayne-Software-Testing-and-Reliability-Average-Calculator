#!/usr/bin/env python3
import os
import importlib.util
from avgcalc import average as original_average

# Folder containing all mutants
mutants_folder = "mutants_folder"

# Test cases for MR
scaling_inputs = [
    [1, 2, 3],
    [2, 4, 6],
    [5, 10],
    [3.5, 3.5, 3.5],
    [10, 20, 30, 40, 50, 100]
]

permutation_inputs = [
    [1, 2, 3],
    [5, 10, 15],
    [2, 4, 6, 8, 10],
    [7, 7, 7],
    [10, 20, 30, 40, 50, 120]
]

# Collect mutants
mutant_files = sorted(f for f in os.listdir(mutants_folder) if f.endswith(".py"))
results = {}

for mf in mutant_files:
    path = os.path.join(mutants_folder, mf)
    spec = importlib.util.spec_from_file_location("mutant", path)
    mutant_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mutant_module)

    killed = False

    # Test scaling MR
    for nums in scaling_inputs:
        try:
            orig = original_average(nums)
            mut = mutant_module.mutated_average(nums)
            if mut != orig:  # detect any change
                killed = True
                break
        except Exception:
            killed = True
            break

    # Test permutation MR if not already killed
    if not killed:
        for nums in permutation_inputs:
            try:
                orig = original_average(nums)
                mut = mutant_module.mutated_average(nums[::-1])
                if mut != orig:
                    killed = True
                    break
            except Exception:
                killed = True
                break

    results[mf] = "Killed" if killed else "Survived"

# Print results
print("\nMutation Test Results:")
for k, v in results.items():
    print(f"{k:<15} -> {v}")