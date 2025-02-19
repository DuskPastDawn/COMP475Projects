import sys

#Generates a list of triangular numbers up to a given limit
def get_triangular_numbers(n):
    #Generate triangular numbers
    triangular = []
    i = 1
    while (i * (i + 1)) // 2 <= n:                   #Equation for finding triangular number for each i up to the number n
        triangular.append((i * (i + 1)) // 2)        #Adds to list of triangular numbers
        i += 1
    return triangular                                #Returns the list of triangular numbers

#Finds the minimum number of terms needed to sum to n using given numbers
def decompose_number(n, numbers):
    # initialize dp array with inf nums
    dp = [float('inf')] * (n + 1)
    # initialize prev array with zeros
    prev = [0] * (n + 1)
    # base case
    dp[0] = 0
    # loop through range n
    for i in range(1, n + 1):
        for num in numbers:
            # if best fit
            if num <= i and dp[i - num] + 1 < dp[i]:
                dp[i] = dp[i - num] + 1
                prev[i] = num

    result = []
    current = n
    while current > 0:
        result.append(prev[current])
        current -= prev[current]

    return dp[n], result[::-1]

def solve(n):
    triangular = get_triangular_numbers(n)                  #Gets the triangular numbers up to n
    count1, terms1 = decompose_number(n, triangular)        #Finds the least # of triangular numbers that make up n

    print("The decomposition with triangular numbers:")
    print(f"{count1} terms:")
    print(f"{n} = {'+'.join(map(str, terms1))}")            #Prints and adds + signs between the terms

    squares = [t * t for t in triangular]                   #Squares the triangular numbers up to n
    count2, terms2 = decompose_number(n, squares)           #Finds the least # of squared triangular numbers that make up n

    print("\nThe decomposition with squares of triangular numbers:")
    print(f"{count2} terms:")
    print(f"{n} = {'+'.join(map(str, terms2))}")            #Prints and adds + signs between the terms

if __name__ == "__main__":
    n = int(sys.argv[1])
    solve(n)
