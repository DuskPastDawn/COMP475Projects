import sys

def get_triangular_numbers(n):
    #Generate triangular numbers
    triangular = []
    i = 1
    while (i * (i + 1)) // 2 <= n:
        triangular.append((i * (i + 1)) // 2)
        i += 1
    return triangular

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
    triangular = get_triangular_numbers(n)
    count1, terms1 = decompose_number(n, triangular)

    print("The decomposition with triangular numbers:")
    print(f"{count1} terms:")
    print(f"{n} = {'+'.join(map(str, terms1))}")

    squares = [t * t for t in triangular]
    count2, terms2 = decompose_number(n, squares)

    print("\nThe decomposition with squares of triangular numbers:")
    print(f"{count2} terms:")
    print(f"{n} = {'+'.join(map(str, terms2))}")

if __name__ == "__main__":
    n = int(sys.argv[1])
    solve(n)
