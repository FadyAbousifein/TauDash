def generate_combinations(n):
    if n == 0:
        return ['']  # Base case: Return an empty string for length 0
    else:
        combinations = []
        for comb in generate_combinations(n - 1):
            combinations.append(comb + 'a')  # Append 'a' to each combination
            combinations.append(comb + 'b')  # Append 'b' to each combination
        return combinations

# Get the maximum value of n
max_length = int(input("Enter the maximum range of length (n): "))

# Generate combinations for each value of n
for length in range(1, max_length + 1):
    combinations = generate_combinations(length)
    print(f"All possible combinations for length {length}:")
    for comb in combinations:
        print(comb)
    print()
