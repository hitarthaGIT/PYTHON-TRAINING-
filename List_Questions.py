# I am using the same python file for all the questions in List, I am using different functions for each sub question

import copy

# 1. Remove duplicate elements from a list without using set
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


#2.Create a new list containing only even numbers using list comprehension
def get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]


# 3.Find the second largest element in a list
def second_largest(lst):
    largest = second = -1
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second


# 4.Calculate the sum of each inner list in a nested list
def sum_of_nested_lists(nested_list):
    sums = []
    for inner_list in nested_list:
        sums.append(sum(inner_list))
    return sums


# 5.Demonstrate shallow copy and deep copy
def demonstrate_copy():
    original = [[1, 2], [3, 4]]

    shallow_copy = copy.copy(original)
    deep_copy = copy.deepcopy(original)

    original[0][0] = 100

    print("Original List:", original)
    print("Shallow Copy:", shallow_copy)
    print("Deep Copy:", deep_copy)



lst = [1, 2, 3, 2, 4, 1, 5]
numbers = [10, 15, 20, 25, 30]
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("1. Remove Duplicates:", remove_duplicates(lst))
print("2. Even Numbers:", get_even_numbers(numbers))
print("3. Second Largest:", second_largest(numbers))
print("4. Sum of Nested Lists:", sum_of_nested_lists(nested))
print("5. Shallow vs Deep Copy:")
demonstrate_copy()
