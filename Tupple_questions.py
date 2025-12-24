
# I am Using the same python program for the tupple questions by using different functions to implenent differet sub-questions
# 1.Find maximum and minimum elements in a tuple
def find_max_min(t):
    maximum = t[0]
    minimum = t[0]

    for i in t:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i

    return maximum, minimum


# 2.Convert a list of tuples into a dictionary
def listoftuplestodict(lst):
    d = {}
    for key, value in lst:
        d[key] = value
    return d


# 3.Count occurrence of an element in a tuple without built-in methods
def count_occ(t, element):
    count = 0
    for i in t:
        if i == element:
            count += 1
    return count


# 4.Create a tuple with mutable elements and modify the mutable data
def modifymutableintuple():
    t = (1, 2, [10, 20, 30], 4)

    print("Before modification:", t)
    t[2][0] = 100
    print("After modification:", t)


# 5.Swap two tuples
def swap_tuples(t1, t2):
    t1, t2 = t2, t1
    return t1, t2



t = (10, 5, 20, 3, 15)
lst = [("a", 1), ("b", 2), ("c", 3)]
element = 2
t_occ = (1, 2, 3, 2, 4, 2, 5)
t1 = (1, 2, 3)
t2 = (4, 5, 6)

max_val, min_val = find_max_min(t)
print("1. Maximum:", max_val, "Minimum:", min_val)

print("2. Dictionary:", listoftuplestodict(lst))

print("3. Occurrence of", element, ":", count_occ(t_occ, element))

print("4. Tuple with mutable element:")
modifymutableintuple()

t1, t2 = swap_tuples(t1, t2)
print("5. Swapped Tuples:")
print("t1:", t1)
print("t2:", t2)
