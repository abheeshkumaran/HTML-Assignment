#_________________________________________sum of elements

def find_sum_of_elements(input_list):
    return sum(input_list)

# Example usage
my_list = [10, 20, 5, 30, 15]
sum_of_elements = find_sum_of_elements(my_list)
print("The sum of elements is:", sum_of_elements)
#_________________________________________duplicate

def find_duplicate_elements(input_list):
    # Create an empty dictionary to store occurrences of elements
    element_count = {}
    duplicates = []

    # Iterate through the list
    for element in input_list:
        # If the element is already in the dictionary, it's a duplicate
        if element in element_count:
            duplicates.append(element)
        # Otherwise, add the element to the dictionary with a count of 1
        else:
            element_count[element] = 1

    return list(set(duplicates))  # Remove duplicates from duplicates list

# Example usage
my_list = [1, 2, 3, 4, 2, 3, 5, 6, 7, 8, 1]
duplicate_elements = find_duplicate_elements(my_list)
print("Duplicate elements:", duplicate_elements)
#_________________________________________empty list

my_list = []
if not my_list:
    print("List is empty")
else:
    print("List is not empty")
#_________________________________________average

my_list = [1, 2, 3, 4, 5]
average = sum(my_list) / len(my_list)
print("Average:", average)    
