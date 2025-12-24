#using indexing
def palindrome_indexing(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


# using slicing
def palindrome_slicing(s):
    return s == s[::-1]


s = input("Enter a string: ")
result_indexing = palindrome_indexing(s)
result_slicing = palindrome_slicing(s)

print("Using Indexing:", "Palindrome" if result_indexing else "Not a Palindrome")
print("Using Slicing:", "Palindrome" if result_slicing else "Not a Palindrome")
