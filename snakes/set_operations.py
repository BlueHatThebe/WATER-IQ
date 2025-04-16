# Create the initial list and convert to a set
numbers = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8]
unique_numbers = set(numbers)
print("Unique numbers set:", unique_numbers)

# Find the sum of all unique numbers
sum_unique = sum(unique_numbers)
print("Sum of unique numbers:", sum_unique)

# Find the maximum and minimum numbers
max_number = max(unique_numbers)
min_number = min(unique_numbers)
print("Maximum number:", max_number)
print("Minimum number:", min_number)

# Remove the largest number and print the updated set
unique_numbers.remove(max_number)
print("Set after removing largest number:", unique_numbers)

# Create new_numbers set
new_numbers = {4, 5, 6, 9, 10}

# Union
union_set = unique_numbers.union(new_numbers)
print("Union of sets:", union_set)

# Intersection
intersection_set = unique_numbers.intersection(new_numbers)
print("Intersection of sets:", intersection_set)

# Difference
difference_set = unique_numbers.difference(new_numbers)
print("Difference (unique_numbers - new_numbers):", difference_set)

# Symmetric Difference
symmetric_diff_set = unique_numbers.symmetric_difference(new_numbers)
print("Symmetric difference:", symmetric_diff_set)