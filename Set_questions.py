
# 1. Union, Intersection, Difference, Symmetric Difference
def set_operations(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    symmetric_difference = set1 ^ set2

    return union, intersection, difference, symmetric_difference


# 2.remove common elements from two sets
def remove_common_ele(set1, set2):
    common = set1 & set2
    set1 = set1 - common
    set2 = set2 - common
    return set1, set2


# 3.check whether one set is a subset of another
def check_subset(set1, set2):
    if set1 <= set2:
        return True
    else:
        return False


# 4.print elements greater than a given number
def print_greater_ele(s, num):
    print("Elements greater than", num, ":")
    for element in s:
        if element > num:
            print(element)


# 5.Convert list with duplicates to set and back to list
def unique_list(lst):
    unique_set = set(lst)
    unique_list = list(unique_set)
    return unique_list



set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# q1
u, i, d, sd = set_operations(set1, set2)
print("1. Union:", u)
print("   Intersection:", i)
print("   Difference:", d)
print("   Symmetric Difference:", sd)

#q2
new_set1, new_set2 = remove_common_ele(set1, set2)
print("2.After removing common elements:")
print("   Set1:", new_set1)
print("   Set2:", new_set2)

#q3
print("3.Is Set1 a subset of Set2?:", check_subset({1, 2}, set1))

#q4
print("4.")
print_greater_ele(set1, 3)

#q5
lst = [1, 2, 2, 3, 4, 4, 5]
print("5. Unique list:", unique_list(lst))
