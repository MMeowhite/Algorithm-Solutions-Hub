def max_path_sum(triangle):
    """
    Calculate the maximum path sum from top to bottom of the triangle.
    """
    # Convert the triangle into a list of lists
    triangle = [list(map(int, row.split())) for row in triangle.split('\n') if row.strip()]
    
    # Create a DP table to store the maximum path sums
    dp = [[0 for _ in range(len(row))] for row in triangle]
    
    # Initialize the DP table with the bottom row of the triangle
    dp[-1] = triangle[-1]
    
    # Iterate from the second last row up to the top
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # Update the DP table with the maximum path sum
            dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])
    
    # The top element of the DP table contains the maximum path sum
    return dp[0][0]

if __name__ == "__main__":
    triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
    print(max_path_sum(triangle))
