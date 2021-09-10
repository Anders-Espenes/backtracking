# Problem 4 Greynodes something something
'''
Grey Nodes:
    is an ordering of the binary numeral system such that:
        Two successive values DIFFER in only one bit

Problem 4
Consider the problem of generating N-bit Grey codes: 
    Given a number N, generate bit patterns from 0 to 2N-1such that successive patterns differ by one bit:  
    ̈Input: N = 2 Output: 00 01 11 10
    Input: N = 3 Output: 000 001 011 010 110 111 101 100
    1.    Implement a backtracking solution.
    2.    Count the number of visited and promising nodes in the search tree.
    3.    Not every problem that looks like a constraint satisfaction problem is one that may need backtracking: 
          n-bit  Gray  Codes  can  be  generated  from  list  of  (N-1)-bit  
          Gray  codes  using  the  following  greedy algorithm  
          (we  need  to  show  this  algorithm  generates  all  Gray  codes  and  nothing  else!). 
    Implement the following algorithm:
        a)  Let the list of (N-1)-bit Gray codes be L1. Create another list L2 which is reverse of L1.
        b)  Modify the list L1 by prefixing a ‘0’ in all codes of L1.
        c)  Modify the list L2 by prefixing a ‘1’ in all codes of L2.
        d)  Concatenate L1 and L2. The concatenated list is required list of n-bit Gray 
            codesHow much faster does the greedy algorithm find a solution? 
            Can you give an (inductive) proof of the correctness of this algorithms?

'''


'''
Problem Notes:

Given a number N, generate bit patterns from 0 to 2^(N-1) such that successive patterns differ by one bit

Input N = 2                 Input: N = 3
Output: 00 01 11 10         Output: 000 001 011 010 110 111 101 100

'''

''' 
Iterative method
Each bit is inverted if the next higher bit of the input value is set to one
'''


from typing import Counter


def makeroot(bits):
    return [tuple([0 for i in range(bits)])]

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
def unique(code):
  temp = Counter(map(tuple, code)) # Counts the occurence of item in list of lists, creates a tuple, item is a pattern, value is nr of occurences
  return next((False for v in temp.values() if v != 1), True) # If any item have more than 1 occurence return True, else return false


# Reject If: somthing is not uniqe or distance between adjacent patterns is greater than 1
def reject(code):
    if(unique(code) and  # True if no pattern have occurence greater than 1
    distance(code)): # Check if distance between patterns == 1
        return True
    return False

# TODO:
# Check if all patterns have been found
def accept(codelen, code):
 if (len(code[-1]) < codelen):
     pass

# TODO:
def output(code):
    print("code: ")
    for codepoint in code:
        for codeelement in codepoint:
            codechar = "1" if codeelement else "0"
            print(codechar),
        print

def backtrack(codelen, code):
    if not reject(code): # If code is not
       return
    if accept(codelen, code):
   #     output(code)
        return code
   # for extension in code:
   #     backtrack(codelen, extension)
    return "No solution found"

#TODO: BUG: With N=4 generates [0,1,0,0] then [1,1,0,1] should be [1,1,0,0]
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


if __name__ == '__main__':
    n = 5

    test = chunk_list([0,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,0,0], 3)
    test2 = chunk_list([0,0,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,0], 4)
    temp = reflective_greycode_generation(n)
    print_list(temp)
    if(distance(temp) and unique(temp)):
     print("Reflective Success")
    else: 
     print("Reflective Failure")

   #temp = backtrack(n,[[0],[1]])
   #print_list(temp)
   #if(temp == test):
   #    print("Backtracking Success")
   #else:
   #    print("Backtracking Failure")
   # code = [[0, 1, 0, 0], [1, 1, 0, 0]]
    #print(backtrack(2, code))
