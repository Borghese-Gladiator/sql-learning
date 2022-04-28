'''
Python Practice and Reference
'''

# Decimal Formatting - prints 6 decimal places formatted
print("{:.6f}".format(1 / 3))
print(f'{1 / 3:.6f}')

# Sorting - sort() sorts in place
[1, 2, 3].sort()

# Sorting - sorted() returns sorted array
sorted([1, 2, 3])
sorted("I like to sort".split())
sorted(["JAMES", "James", "james"], reverse=True)

# Dates - convert 12-hour format to 24-hour format
from datetime import datetime
oldDate = datetime.strptime("12:00:00AM", '%I:%M:%S%p')
newDate = oldDate.strftime('%H:%M:%S')

# Count - counts number of elements with specified value
[1, 2, "a", "b"].count("a")

# 2D Array Iteration - middle diagonals
def getLeftDiagonal(arr):
    left = 0
    for i in range(len(arr)):
        left += arr[i][i]
    return left

def getLeftDiagonal(arr):
    right = 0
    for i in range(len(arr)):
        right += arr[i][len(arr) - 1 - i]
    return right

def diagonalDifference(arr):
    return abs(getLeftDiagonal(arr) - getLeftDiagonal(arr))

# 2D Array Iteration - all diagonals
array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
]
dim = len(array)
for k in range(dim): # top half
    for j in range(k):
        i = k - j
        print(array[i][j])
for k  in(dim - 2, 0, -1): # bottom half
    for j in range(k):
        i = k - j
        print(array[dim - j - 1][dim - i - 1])

# 2D Array Iteration - diagonals
def diagonalOrder(matrix):
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

# Enumerate
for idx, val in enumerate(["One", "Two", "Three"]):
    print(idx, val)

# Median
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