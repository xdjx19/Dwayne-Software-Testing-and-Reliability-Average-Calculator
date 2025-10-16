# Original (for reference)
def original_avg(numbers):
    return sum(numbers) / len(numbers)

# Mutant 1: Changed "+" to "-" when summing list
def mutant1_avg(numbers):
    total = 0
    for num in numbers:
        total = total - num  # Changed + to -
    return total / len(numbers)

# Mutant 2: Changed division "/" to integer division "//"
def mutant2_avg(numbers):
    return sum(numbers) // len(numbers)  # Changed / to //

# Mutant 3: Removed division entirely (returns sum)
def mutant3_avg(numbers):
    return sum(numbers)  # No division

# Mutant 4: Divides by fixed 5 instead of list length
def mutant4_avg(numbers):
    return sum(numbers) / 5  # Fixed divisor

# Mutant 5: Multiplied result by 2
def mutant5_avg(numbers):
    return (sum(numbers) / len(numbers)) * 2  # Multiplied by 2

# Mutant 6: Multiplied result by 0.5
def mutant6_avg(numbers):
    return (sum(numbers) / len(numbers)) * 0.5  # Multiplied by 0.5

# Mutant 7: Used only first two inputs in sum
def mutant7_avg(numbers):
    if len(numbers) >= 2:
        return (numbers[0] + numbers[1]) / len(numbers)  # Only first two
    return sum(numbers) / len(numbers)

# Mutant 8: Skipped last input in list
def mutant8_avg(numbers):
    if len(numbers) > 1:
        return sum(numbers[:-1]) / len(numbers)  # Skip last element
    return sum(numbers) / len(numbers)

# Mutant 9: Used random element count instead of len(list)
def mutant9_avg(numbers):
    import random
    fake_length = random.randint(1, 10)  # Random length
    return sum(numbers) / fake_length

# Mutant 10: Added rounding to nearest integer
def mutant10_avg(numbers):
    return round(sum(numbers) / len(numbers))  # Rounded

# Mutant 11: Added +1 to final result
def mutant11_avg(numbers):
    return (sum(numbers) / len(numbers)) + 1  # Added 1

# Mutant 12: Subtracted 1 from final result
def mutant12_avg(numbers):
    return (sum(numbers) / len(numbers)) - 1  # Subtracted 1

# Mutant 13: Returns the largest number instead of average
def mutant13_avg(numbers):
    return max(numbers)  # Returns max instead

# Mutant 14: Returns smallest number instead of average
def mutant14_avg(numbers):
    return min(numbers)  # Returns min instead

# Mutant 15: Ignores zero values in list
def mutant15_avg(numbers):
    non_zero = [x for x in numbers if x != 0]  # Filter zeros
    if non_zero:
        return sum(non_zero) / len(non_zero)
    return 0

# Mutant 16: Treats all negatives as positives
def mutant16_avg(numbers):
    absolute_numbers = [abs(x) for x in numbers]  # Absolute values
    return sum(absolute_numbers) / len(absolute_numbers)

# Mutant 17: Adds sum twice before dividing
def mutant17_avg(numbers):
    total = sum(numbers) + sum(numbers)  # Sum twice
    return total / len(numbers)

# Mutant 18: Used wrong list index (off-by-one)
def mutant18_avg(numbers):
    if len(numbers) > 0:
        # Off-by-one error in indexing
        return sum(numbers) / (len(numbers) - 1) if len(numbers) > 1 else numbers[0]
    return 0

# Mutant 19: Adds a random constant before dividing
def mutant19_avg(numbers):
    import random
    return (sum(numbers) + random.randint(1, 10)) / len(numbers)  # Random add

# Mutant 20: Multiplied each value by 3 before summing
def mutant20_avg(numbers):
    multiplied = [x * 3 for x in numbers]  # Multiply each by 3
    return sum(multiplied) / len(multiplied)

# Mutant 21: Multiplied result by 0
def mutant21_avg(numbers):
    return (sum(numbers) / len(numbers)) * 0  # Always returns 0

# Mutant 22: Added +10 to final output
def mutant22_avg(numbers):
    return (sum(numbers) / len(numbers)) + 10  # Added 10

# Mutant 23: Used reversed list
def mutant23_avg(numbers):
    reversed_list = list(reversed(numbers))  # Reverse list
    return sum(reversed_list) / len(reversed_list)

# Mutant 24: Average calculated using sum² instead of sum
def mutant24_avg(numbers):
    squared_sum = sum(x * x for x in numbers)  # Sum of squares
    return squared_sum / len(numbers)

# Mutant 25: Skips first element in averaging
def mutant25_avg(numbers):
    if len(numbers) > 1:
        return sum(numbers[1:]) / len(numbers[1:])  # Skip first
    return sum(numbers) / len(numbers)

# Mutant 26: Divides by (length + 1)
def mutant26_avg(numbers):
    return sum(numbers) / (len(numbers) + 1)  # Length + 1

# Mutant 27: Divides by (length - 1)
def mutant27_avg(numbers):
    if len(numbers) > 1:
        return sum(numbers) / (len(numbers) - 1)  # Length - 1
    return sum(numbers) / len(numbers)

# Mutant 28: Added sum of input twice
def mutant28_avg(numbers):
    total = sum(numbers) + sum(numbers)  # Double sum
    return total / len(numbers)

# Mutant 29: Subtracted constant 5 from output
def mutant29_avg(numbers):
    return (sum(numbers) / len(numbers)) - 5  # Subtract 5

# Mutant 30: Ignores duplicate values
def mutant30_avg(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    return sum(unique_numbers) / len(unique_numbers)