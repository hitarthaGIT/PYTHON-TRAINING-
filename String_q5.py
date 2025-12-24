s = "Python"

try:
    s[0] = 'J'  
except TypeError as e:
    print("Error:", e)

print("Original String:", s)
