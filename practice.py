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

# any - checking if condition holds for any element
if any(val > 2 for val in range(10)):
  print(f"ANY: {any(val > 2 for val in range(10))}")

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
[('c', 2), ('b', 2), ('a', 3)].sort(key=cmp_to_key(letter_cmp))
print(sorted([('c', 2), ('b', 2), ('a', 3)], key=cmp_to_key(letter_cmp)))

from operator import itemgetter
L=[[0, 1, 'f'], [4, 2, 't'], [9, 4, 'afsd']]
sorted(L, key=itemgetter(2), reverse=True)

class Pokemon:
  def __init__(self, name, category, attack):
    self.name = name
    self.category = category
    self.attack = attack
  def __repr__(self):
    # string representation function
    return repr((self.name, self.category, self.attack))
pokemon_list = [
  Pokemon('Beedrill', 'Poison', 90),
  Pokemon('Charmander', 'Fire', 52),
  Pokemon('Blastoise', 'Water', 83),
]
print(sorted(pokemon_list, key=lambda x: x.attack))

# Sort with key on first and second element of each tuple
l = [(3, 'aaa'), (1, 'bbbb'), (3, 'ab'), (2, 'aaa')]
sorted(l, key = lambda x: (x[0], x[1]))
# Sort number in descending order and word in ascending order
sorted(l, key = lambda x: (-x[0], x[1]))

# Regex
import re
## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
match = re.search(r'igs', 'piiig') # not found, match == None

## . = any char but \n
match = re.search(r'..g', 'piiig') # found, match.group() == "iig"

## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"

## i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiig') # found, match.group() == "piii"

## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"

## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # found, match.group() == "1 2   3"
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found, match.group() == "12  3"
match = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, match.group() == "123"

## ^ = matches the start of string, so this fails:
match = re.search(r'^b\w+', 'foobar') # not found, match == None
## but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar') # found, match.group() == "bar"

if match:
  print(match.group())  ## 'alice-b@google.com'

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
  print(match.group())   ## 'alice-b@google.com' (the whole match)
  print(match.group(1))  ## 'alice-b' (the username, group 1)
  print(match.group(2))  ## 'google.com' (the host, group 2)

## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
  # do something with each found email string
  print(email)

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
  print(tuple[0])  ## username
  print(tuple[1])  ## host

'''
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group
'''

'''
[arn]	Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	\
'''

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
x = re.search(r"\bS\w+", txt) # Match object, None if nothing found
print(x.string)
print(x.span())
print(x.group())
