import sys

#Don't delete next two lines, so I can quickly test different cases.
#filename = sys.argv[1];
#print(filename);

filename = 'input.txt'
file = open(filename, "r")
temp = file.readline()
A = temp.rstrip().split(',')
#Sequence is stored in list A

#Global variable to store the repeated coord
repCoord = (0,0)

#Recursive function that is run to see if the path is wandering
def is_wandering(path, start=0, end=None, visited=None, position=(0, 0)):

    #If this is the first of the calls for the function (before the recursion), 
    # then this intializes the set and adds the beginning coordinate. It also initalizes the value for end
    if visited is None:  
        visited = set()
        visited.add((0, 0))
        end = len(path) - 1

    #At an end of the recursive tree, we are running a call on a single step
    #This code then executes, processes the step, checks to see 
    if start == end:  # Base case: single move
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
            global repCoord
            repCoord = (x,y) #Stores the revisited position in a global variable
            return False
        visited.add((x, y))
        return True

    # Divide: Split the path into two halves
    mid = start + (end - start) // 2

    # Process the left half
    #At the beginning of a path, we split it up, dive in to the left half until we isolate just one step
    #After that, we then recursively rise back up through the calls and search the right halfs
    left_result = is_wandering(path, start, mid, visited, position)
    
    #If statement that helps use rise through the recursive statements if we've found our repeated position
    if not left_result:
        return False

    #Calculate the next position and move on to the next 
    x, y = position
    for i in range(start, mid + 1):
        if path[i] == 'L':
            x -= 1
        elif path[i] == 'R':
            x += 1
        elif path[i] == 'U':
            y += 1
        elif path[i] == 'D':
            y -= 1

    # Process the right half
    return is_wandering(path, mid + 1, end, visited, (x, y))

#Function that takes in the position where the path was found to not be wandering
#It then iterates through the path once more to find which indexes were responible for leading the path to those coordinates
def findIndex(path, coord): #O(n)
    end = len(path) - 1
    v,w = coord
    x=0
    y=0
    index1 = -1
    index2 = -1
    #For loop to iterate through the range and calculate the positions
    for i in range(0, end):
        if path[i] == 'L':
            x -= 1
        elif path[i] == 'R':
            x += 1
        elif path[i] == 'U':
            y += 1
        elif path[i] == 'D':
            y -= 1

        #If the calculated position equals the passed coordinate, we store the index
        if (x,y) == (v,w):
            if index1 == -1:
                index1 = i
            elif index2 == -1:
                index2 = i
    #If statement to make sure we return the indexes in the right order
    if index1 > index2:
        return index2, index1
    else:
        return index1, index2


if is_wandering(A):
    print("The path is wandering")
else:
    x,y = findIndex(A, repCoord)
    print("The path is not wandering. There is a loop from index " + str(x) + " to " + str(y))