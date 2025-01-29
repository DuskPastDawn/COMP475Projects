import sys

#Don't delete next two lines, so I can quickly test different cases.
#filename = sys.argv[1];
#print(filename);

filename = 'input.txt'
file = open(filename, "r")
temp = file.readline()
A = temp.rstrip().split(',')
#Sequence is stored in list A

def is_wandering(path, start=0, end=None, visited=None, position=(0, 0)):
    """
    Determines if the path is wandering using divide-and-conquer.
    """
    if visited is None:  # Initialize visited set and end index for the first call
        visited = set()
        visited.add((0, 0))
        end = len(path) - 1

    if start == end:  # Base case: processing a single move (L, R, U, or D)
        x, y = position
        if path[start] == 'L':
            x -= 1
        elif path[start] == 'R':
            x += 1
        elif path[start] == 'U':
            y += 1
        elif path[start] == 'D':
            y -= 1
        
        # Check if the position is revisited
        if (x, y) in visited:
            return False # Not wandering (revisited position)

        # if the position hasn't been revisited, store the position and return true
        visited.add((x, y)) 
        return True

    # Divide: Split the path into two halves
    mid = start + (end - start) // 2

    # Process the left half recursively (starts at the beginning of the array to middle)
    left_result = is_wandering(path, start, mid, visited, position)
    if not left_result:
        return False # if at any point a path is revisited, return false

    # Compute the position at the end of the left half
    x, y = position
    for i in range(start, mid + 1): #O(n/2) worst case
        if path[i] == 'L':
            x -= 1
        elif path[i] == 'R':
            x += 1
        elif path[i] == 'U':
            y += 1
        elif path[i] == 'D':
            y -= 1

    # Process the right half (starts at mid + 1, ends at right half of array)
    return is_wandering(path, mid + 1, end, visited, (x, y))

if is_wandering(A):
    print("The path is wandering")
else:
    print("The path is not wandering")
