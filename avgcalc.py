# Get numbers from user
numbers = []
print("Enter numbers one by one (type 'done' when finished):")

while True:
    user_input = input("Enter a number: ")
    
    # Check if user wants to stop
    if user_input.lower() == 'done':
        break
    
    try:
        # Convert input to float and add to list
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number or 'done' to finish.")

# Calculate and display average
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"\nNumbers entered: {numbers}")
    print(f"Average: {average}")
else:
    print("\nNo numbers were entered.")