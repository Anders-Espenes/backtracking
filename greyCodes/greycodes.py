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


from functools import reduce
from operator import concat


def safe(res, n ,num):
    if (n == 0):
        res.append(num[0])
        return

    # ignore the bit.
    safe(res, n - 1, num)

    # invert the bit.
    num[0] = num[0] ^ (1 << (n - 1))
    safe(res, n - 1, num)

def generate_patterns(n):
    # Find a next 
    res = [] # Empty list to contain the generated patterns
    num = [0]
    safe(res, n, num)
    return res


def reflective_greycode_generation(n, L1=[[0],[1]]):
    if(len(L1[0]) < n):  # Stop when we have reached the desired number of bits
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
    n = 3

    test = chunk_list([0,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,0,0], 3)
    temp = reflective_greycode_generation(n)
    print_list(temp)
    if(temp == test):
     print("Success")
    else: 
     print("Failure")
