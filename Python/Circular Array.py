# Python3 program to demonstrate the use of 
# circular array without using extra memory space
 
# function to print circular list starting
# from given index ind.

def prints(a, n, ind):

    i = ind

     

    # print from ind-th index to (n+i)th index.

    while i < n + ind :

        print(a[(i % n)], end = " ")

        i = i + 1
 
# Driver Code

a = ['A', 'B', 'C', 'D', 'E', 'F']

n = len(a);

prints(a, n, 3);
 
# This code is contributed by rishabh_jain