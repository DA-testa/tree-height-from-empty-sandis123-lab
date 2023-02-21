# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    for vertex in range(n):
        height = 0
        current=vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def main():
    n= int(input())
    parents = list(map(int, input().split()))
    nodes_list=[]
    for i in range(n):
        nodes_list.append(nodes(parents[i]))
    for child_index in range(n):
        parent_index=parents[child_index]
        if parent_index== -1:
            root= child_index
        else:
            nodes_list[parent_index].addChild(nodes_list[child_index])
    if len(nodes_list) ==0:
        return 0
    height = maxDepth(nodes_list[root]) +1
    print(height)
    return 0
            
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
