#!/usr/bin/env python3
from typing import List, Iterable
import math
import random

def parse_number_list(s: str) -> List[float]:
    if not s:
        return []
    tokens = s.replace(",", " ").split()
    return [float(tok) for tok in tokens]

def mutated_average(numbers: Iterable[float]) -> float:
    """Original average function used by mutant runner"""
    nums = list(numbers)
    if len(nums) == 0:
        raise ValueError("Cannot compute average of an empty list.")
    return sum(nums) / len(nums)

# --- Metamorphic relation helpers ---

def scale_inputs(numbers: Iterable[float], k: float) -> List[float]:
    return [x * k for x in numbers]

def permute_inputs(numbers: Iterable[float], seed: int = None) -> List[float]:
    arr = list(numbers)
    rnd = random.Random(seed)
    rnd.shuffle(arr)
    return arr

def approx_equal(a: float, b: float, tol: float = 1e-9) -> bool:
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)

def verify_scaling_mr(original: Iterable[float], k: float, tol: float = 1e-9) -> bool:
    orig_avg = mutated_average(original)
    scaled_avg = mutated_average(scale_inputs(original, k))
    return approx_equal(scaled_avg, k * orig_avg, tol)

def verify_permutation_mr(original: Iterable[float], permuted: Iterable[float], tol: float = 1e-9) -> bool:
    return approx_equal(mutated_average(original), mutated_average(permuted), tol)

# --- Command-line interaction ---
def interactive_calculator():
    print("Average Calculator")
    print("Enter numbers separated by spaces or commas.")
    print("Type 'quit', 'done', or press Enter to exit.\n")
    while True:
        s = input("Enter numbers: ").strip()
        if s.lower() in ("quit", "done", ""):
            print("Exiting. Goodbye!")
            break
        try:
            nums = parse_number_list(s)
            if not nums:
                print("No numbers parsed. Try again.")
                continue

            avg_value = mutated_average(nums)
            print(f"Stored numbers: {nums}")
            print(f"Average: {avg_value}\n")

            # MR examples
            k = 2.0
            print(f"Scaling MR (x{k}) holds? -> {verify_scaling_mr(nums, k)}")
            permuted = permute_inputs(nums, seed=42)
            print(f"Permutation MR holds? -> {verify_permutation_mr(nums, permuted)} (permuted: {permuted})\n")
        except ValueError as e:
            print(f"Input error: {e}. Enter only numbers separated by spaces or commas.\n")

if __name__ == "__main__":
    interactive_calculator()