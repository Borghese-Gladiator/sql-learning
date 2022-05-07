'''
Python Practice and Reference
'''

# Iterate over numbers
print("DIGIT ITERATION")
def superDigit(n: str, k: int):
  p = int(n * k)
  s = 0
  while p > 0 or s > 9:
      if p == 0:
          p = s
          s = 0
      s += p % 10
      p //= 10
  return s
superDigit("148", 3)

# Exception
try:
  "+".join([1, 2, 3, 4, 5])
except Exception as e:
  print(f"EXCEPTION SYNTAX: {e}")

# Lambda
print("LAMBDA: {}".format((lambda s: s[::-1])("gnirts a ma I")))
(lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6)

# Map - reverses each string in list
list(map(lambda s: s[::-1], ["cat", "dog", "hedgehog", "gecko"]))
list(
  map(
    (lambda a, b, c: a + b + c),
    [1, 2, 3],
    [10, 20, 30],
    [100, 200, 300]
  )
)

# Lambda with if statement - Use map to see which numbers are divisible by 3
bool_list = map(lambda x: 1 if x%3==0 else 0, list(range(20)))

# Filter
list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333]))
list(filter(lambda x: x % 2 == 0, range(10)))
list(filter(lambda s: s.isupper(), ["cat", "Cat", "CAT", "dog", "Dog", "DOG", "emu", "Emu", "EMU"]))

# Count unique values
from collections import Counter
a_tuple = (1, 2, 3) # immutable, more memory efficient
a_set = {1, 2, 3}
len(set(list(range(20))))
len(Counter(list(range(20))).keys())

# Zip Use Cases 
a_list = ["A", "A", "A"]
b_list = [0, 1, 2]
print("ZIP")
for a, b in zip(a_list, b_list):
  print(a, b)

# Combinatoric Iterators - permutation, combination
print("COMBINATORIC ITERATORS")
import itertools
x = [1, 2, 3]
y = ['A', 'B']
print(list(itertools.product(x, y)))
print(list(itertools.permutations(x)))

y = ['A', 'B', 'C', 'D']
print(list(itertools.combinations(y, 3)))

z = ['A', 'B', 'C']
print(list(itertools.combinations_with_replacement(z, 2)))

# Decimal Formatting - prints 6 decimal places formatted
"{:.6f}".format(1 / 3)
print(f'DECIMAL FORMATTING: {1 / 3:.6f}')

# Sorting - sort() sorts in place
[1, 2, 3].sort()

# Sorting - sorted() returns sorted array
sorted([1, 2, 3])
sorted("I like to sort".split())
sorted(["JAMES", "James", "james"], reverse=True)

# Dates - convert 12-hour format to 24-hour format
print("DATETIMES")
from datetime import datetime
oldDate = datetime.strptime("12:00:00AM", '%I:%M:%S%p')
newDate = oldDate.strftime('%H:%M:%S')

# Dates - check if gap is greater than one year
from datetime import timedelta
one_year_delta = timedelta(days = 365)
datetime.strptime("20050109", '%Y%m%d') - datetime.strptime("20050109", '%Y%m%d') < one_year_delta

# Count - counts number of elements with specified value
[1, 2, "a", "b"].count("a")

# 2D Array Iteration - middle diagonals
def getLeftDiagonal(arr):
    left = 0
    for i in range(len(arr)):
        left += arr[i][i]
    return left

def getRightDiagonal(arr):
    right = 0
    for i in range(len(arr)):
        right += arr[i][len(arr) - 1 - i]
    return right

def diagonalDifference(arr):
    return abs(getLeftDiagonal(arr) - getRightDiagonal(arr))

# 2D Array Iteration - diagonals
def diagonalOrder(matrix):
    ROW = len(matrix)
    COL = len(matrix[0])
    # There will be ROW+COL-1 lines in the output
    for line in range(1, (ROW + COL)):
        # Get column index of the first element
        # in this line of output. The index is 0
        # for first ROW lines and line - ROW for
        # remaining lines
        start_col = max(0, line - ROW)
 
        # Get count of elements in this line.
        # The count of elements is equal to
        # minimum of line number, COL-start_col and ROW
        count = min(line, (COL - start_col), ROW)
 
        # Print elements of this line
        for j in range(0, count):
            print(matrix[min(ROW, line) - j - 1]
                        [start_col + j], end="\t")
 
        print()

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
]
# diagonalDifference(matrix) # only works on square matrices
diagonalOrder(matrix)

# 2D Iteration - Columns
columns = list(zip(*matrix)) # list of tuples
colMatrix = []
for i in range(len(matrix[0])):
  colMatrix.append([row[i] for row in matrix])

# 2D Iteration - printing matrix
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))

# Enumerate
print("ENUMERATE")
for idx, val in enumerate(["One", "Two", "Three"]):
    print(idx, val)

# Median
print("MEDIAN")
lst = sorted([3, 2, 1])
if len(lst) % 2 == 0:
    # Applying formula which is sum of middle two divided by 2
    print(lst[len(lst) // 2] + lst[(len(lst) - 1) // 2]) / 2
else:
    # If length is odd then get middle value
    print(lst[len(lst) // 2])

# List Initialization - initializes array of zeroes
result = [0] * 100

# Character Code - Caesar cipher
print("CAESAR CIPHER")
def encryptChar(c, k):
    if c.isupper():
        c_index = ord(c) - ord('A')
        return chr((c_index + k) % 26 + ord('A'))
    elif c.islower():
        c_index = ord(c) - ord('a')
        return chr((c_index + k) % 26 + ord('a'))
    elif c.isdigit():
        return (int(c) + k) % 10
    else:
        return c

def caesarCipher(s, k):
    # Write your code here
    result = ""
    for c in s:
        result += encryptChar(c, k)
    return result

# String Reversal
def isPalindrome(s1):
    return s1 == s1[::-1]

# List Equality - without order
import collections
collections.Counter([0,2,1]) == collections.Counter([0,2,1])

# List Equality - with order
print(f"LIST EQUALITY: [0,1,2] == [0,2,1] is {[0,1,2] == [0,2,1]}")

# Split Word into characters
print("SPLIT WORD INTO CHARACTERS")
word = "blah"
wordList = [char for char in word]

# Custom Sort
print("CUSTOM SORT FUNCTION")
from functools import cmp_to_key
def letter_cmp(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] == b[1]:
        if a[0] > b[0]:
            return 1
        else:
            return -1
    else:
        return 1
letter_cmp_key = cmp_to_key(letter_cmp)
[('c', 2), ('b', 2), ('a', 3)].sort(key=letter_cmp_key)
sorted([('c', 2), ('b', 2), ('a', 3)], key=cmp_to_key(letter_cmp))

# Regex