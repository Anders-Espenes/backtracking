# Problem 4 Greynodes something something
from typing import Counter
from copy import deepcopy


# Performs an XOR operaton on two lists, lists must be same length
# * does not append the 0 to the returned list, as we only want the 1s from the XOR operation
def xor(L1, L2):
    L3 = []
    for i, j in zip(L1, L2):
        if(i != j):
            L3.append(1)
    return L3


# Check if the distance between each pattern is == 1
def distance(code):
    for i, j in zip(*[iter(code)]*2): # Loops two items at once
        if(len(xor(i, j)) != 1): # If distance is not 1 between two patterns next to each other
            return False # Distance was not 1
    return True

# Check if every pattern is unique
# TODO: Change it to only check if one pattern is unique not the whole thing
def unique(code):
  temp = Counter(map(tuple, code)) # Counts the occurence of item in list of lists, creates a tuple, item is a pattern, value is nr of occurences
  return next((False for v in temp.values() if v != 1), True) # If any item have more than 1 occurence return True, else return false


# Reject If: somthing is not uniqe or distance between adjacent patterns is greater than 1
def reject(code):
    if(unique(code) and  # True if no pattern have occurence greater than 1
    distance(code)): # True if distance between adjacent patterns == 1
        return True
    return False


# Takes in copy of pattern list, checks if value is promising
def promising(temp, pattern, bit, i):
    if (len):
        pattern.append(i)
    else:
        pattern.insert(bit, i)
    temp.append(pattern)
    if(unique(temp)): # Test value
        return True # Value is promising
    return False # Value is not promising


def extensions(code):
    for i in range(len(code[-1]) - 1, -1, -1): # Start backwards
        nextcodepoint = list(code[-1])  # Create copy
        nextcodepoint[i] = nextcodepoint[i] + 1 - nextcodepoint[i] * 2
        yield code + [nextcodepoint]

def accept(codelen, code):
    if len(code) != codelen: # Check if the number of patterns is correct
        return False
    return (len(xor(code[0], code[-1])) == 1) # Check if distance between first and last pattern is 1

def promising(pattern):
    return reject(pattern)

# Finishes when all patterns are unique and one bit shift difference with adjacent patterns
def backtrack(codelen, code):
    if not reject(code): # Check if pattern fullfilles the requirements for grey code
        return
    if accept(codelen, code): # Check if finished
        print_list(code)
        exit() # TODO: Find a better solution to this, is not good coding
    for extension in extensions(code):
        if backtrack(codelen, extension):
            return extension


    

# Uses a reflect and prefix method to generate grey code
def reflective_greycode_generation(n, L1=[[]]):
    if(len(L1[-1]) < n):  # Stop when we have reached the desired number of bits
        L2 = L1.copy()  # Copy and reverse
        L2.reverse()    
        L1 = [[0] + elt for elt in L1] # Add prefix 0 to original code
        L2 = [[1] + elt for elt in L2] # Add prefix 1 to orignal code reversed
        L1 = L1 + L2 # Concatinate to create new code with additional bit
        L1 = reflective_greycode_generation(n, L1) # Add new bit
    return L1

def print_list(list):
    [print(v) for v in list]
    

def chunk_list(list, n):
    return([list[i:i + n] for i in range(0, len(list), n)])


def makeroot(bits):
    return [[0 for _ in range(bits)]]


if __name__ == '__main__':
    n = 2

    temp = reflective_greycode_generation(n)
    print_list(temp)
    if(distance(temp) and unique(temp)):
     print("Reflective Success")
    else: 
     print("Reflective Failure")

    backtrack(2**n, makeroot(n))
