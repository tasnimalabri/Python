#loop that counts how many elements in a list is equal to zero. 
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 
 
# Driver Code
lst = [0, 6, 8, 10, 8, 20, 10, 0, 8]
x = 0
print('{} has occurred {} times'.format(x, countX(lst, x)))