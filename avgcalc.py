#!/usr/bin/env python3
"""
Average Calculator + simple metamorphic test helpers

Usage examples (when running):
 - Enter values separated by spaces or commas:
     1 2 3
     or
     1,2,3
 - Enter 'done' or leave blank to quit.
"""

from typing import List, Iterable
import math
import random

def parse_number_list(s: str) -> List[float]:
    """Parse a string with numbers separated by spaces and/or commas into a list of floats.
       Raises ValueError if any token is not a valid number.
    """
    if not s:
        return []
    # replace commas with spaces, split by whitespace
    tokens = s.replace(",", " ").split()
    numbers = [float(tok) for tok in tokens]
    return numbers

def average(numbers: Iterable[float]) -> float:
    """Return average of numbers. Raises ValueError if list is empty."""
    nums = list(numbers)
    if len(nums) == 0:
        raise ValueError("Cannot compute average of an empty list.")
    return sum(nums) / len(nums)

# --- Metamorphic relation helpers (useful for testing) ---

def scale_inputs(numbers: Iterable[float], k: float) -> List[float]:
    """Return a new list where every element is multiplied by k."""
    return [x * k for x in numbers]

def permute_inputs(numbers: Iterable[float], seed: int = None) -> List[float]:
    """Return a permutation (shuffled copy) of the input list.
       Optional seed for reproducible shuffles.
    """
    arr = list(numbers)
    rnd = random.Random(seed)
    rnd.shuffle(arr)
    return arr

def approx_equal(a: float, b: float, tol: float = 1e-9) -> bool:
    """Floating point tolerant comparison."""
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)

def verify_scaling_mr(original: Iterable[float], k: float, tol: float = 1e-9) -> bool:
    """Check scaling MR: average(scale(inputs, k)) == k * average(inputs)"""
    orig_avg = average(original)
    scaled_avg = average(scale_inputs(original, k))
    return approx_equal(scaled_avg, k * orig_avg, tol)

def verify_permutation_mr(original: Iterable[float], permuted: Iterable[float], tol: float = 1e-9) -> bool:
    """Check permutation MR: average(permuted) == average(original)"""
    return approx_equal(average(original), average(permuted), tol)

# --- Command-line interaction ---

def interactive_calculator():
    print("Average Calculator")
    print("Enter numbers separated by spaces or commas (e.g. '1 2 3' or '1,2,3').")
    print("Type 'quit' or 'done' or just press Enter on an empty line to exit.\n")

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

            # store into a variable as requested
            stored_numbers = nums  # <- this variable stores the user's inputs
            avg_value = average(stored_numbers)  # <- computed average stored here

            print(f"Stored numbers: {stored_numbers}")
            print(f"Average: {avg_value}\n")

            # Example quick MR checks (optional; useful for assignment/demos)
            # Scaling example: check x2
            k = 2.0
            scaling_ok = verify_scaling_mr(stored_numbers, k)
            print(f"Scaling MR (multiply inputs by {k}) holds? -> {scaling_ok}")

            # Permutation example: shuffle and check
            permuted = permute_inputs(stored_numbers, seed=42)
            permutation_ok = verify_permutation_mr(stored_numbers, permuted)
            print(f"Permutation MR (reorder) holds? -> {permutation_ok} (permuted: {permuted})\n")

        except ValueError as e:
            print(f"Input error: {e}. Please enter only numbers separated by spaces or commas.\n")

if __name__ == "__main__":
    interactive_calculator()