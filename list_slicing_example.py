mixed_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e', 2.16] #list of mixed data types


first_three_elements = mixed_data[:3]  # slicing the list to get the first three elements
print(first_three_elements)

second_to_fifth_elements = mixed_data[1:5]  # slicing the list to get the elements from index 1 to 4 (5th index not included)
print(second_to_fifth_elements)

last_two_elements = mixed_data[-2:]  # slicing the list to get the last two elements
print(last_two_elements)


# Loop to iterate through mixed_data
for element in mixed_data:
    # Print each element along with its data type
    print(f'Element: {element}, Type: {type(element)}')