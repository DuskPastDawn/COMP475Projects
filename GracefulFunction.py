import sys

#Don't delete next two lines, so I can quickly test different cases.
#filename = sys.argv[1];
#print(filename);

filename = 'input.txt';
file = open(filename, "r")
temp = file.readline()
A = temp.rstrip().split(',');

#Converts string entries to int
for i in range(len(A)):
	A[i] = int(A[i]);
#Labeling is stored in list A
#==============================================
# Your code goes here

#First check if ints are unique - O(N)
def int_unique(arr):
    seen = set()  #Empty set variable to store numbers as we encounter them
    for num in arr:  #Loop through each number in the array
        if num in seen:  #Check to see if the number is already in the set - This is O(1) on average because the set uses a hash table
            return False  #If so, a duplicate is found, so we return False
        seen.add(num)  #Otherwise we add the number to the set
    return True #If all numbers are unique, this function returns true

#Check if differences are unique - O(N)
def dif_unique(arr):
    seen = set() #Empty set variable
    for i in range(len(arr)): #looping through the array
        if i>0: #Skipping to the 2nd item because we are comparing with one item prior in array
            diff = abs(arr[i] - arr[i-1]) #Find difference between current int and last int
            if diff in seen: #If int is in set, return false
                return False;
            seen.add(diff) #Otherwise, add the diff to set
    return True #If all differences are unique, return true

if int_unique(A) and dif_unique(A): #If both the integers and differences are unique, we print graceful
    print("Graceful")
else: #Otherwise, we print "Not Graceful"
    print("Not Graceful")

#==============================================