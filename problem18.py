# https://projecteuler.net/problem=18
# dynamic programming solution!

triangle = [ 
	                           [75],
	                         [95, 64],
	                       [17, 47, 82],
	                     [18, 35, 87, 10],
	                    [20, 4, 82, 47, 65],
	                  [19, 1, 23, 75, 3, 34],
	                [88, 2, 77, 73, 7, 63, 67],
	              [99, 65, 4, 28, 6, 16, 70, 92],
	           [41, 41, 26, 56, 83, 40, 80, 70, 33],
	         [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
	       [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
	     [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
	   [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
	  [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
	[04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

# O(n) running time and O(log(n)) space complexity :)
def max_path_sum(triangle):
	''' Find the max sum of a path from the top to the bottom of triangle. '''

	# at iteration i, max_sums[j] is the max sum of any path from (0,0) to (i,j).
	max_sums = [0] * len(triangle)

	# at iteration i, prev is basically max_sums for row (i-1)
	prev = [0] * len(triangle)
	
	prev[0] = triangle[0][0]    # initialize base

	for i in range(1, len(triangle)):

		max_sums[0] = prev[0] + triangle[i][0]    # solve left
		max_sums[i] = prev[i-1] + triangle[i][i]  # solve right
		
		for j in range(1, i):
			greater_parent = max(prev[j-1], prev[j])
			max_sums[j] = triangle[i][j] + greater_parent

		prev[:] = max_sums    # copy max_sums into prev using slice assignment

	return max(max_sums)

# old/alternate solution. O(n) space complexity (uses 2D list to store max sums)
def max_path_sum2(triangle):
	''' Find the max sum of a path from the top to the bottom of triangle. '''
	
	# make a 2D list with the same dimensions as triangle.
	# max_sums[i][j] is the max sum of any path from (0,0) to (i,j)
	max_sums = [[0] * (i + 1) for i in range(len(triangle))]
	
	max_sums[0][0] = triangle[0][0]    # initialize base

	for i in range(1, len(triangle)):
		
		max_sums[i][0] = max_sums[i-1][0] + triangle[i][0]    # leftmost
		max_sums[i][i] = max_sums[i-1][i-1] + triangle[i][i]  # rightmost
		
		for j in range(1, i):
			greater_parent = max(max_sums[i-1][j-1], max_sums[i-1][j])
			max_sums[i][j] = triangle[i][j] + greater_parent

	last_row = max_sums[len(max_sums) - 1]
	return max(last_row)

answer = max_path_sum(triangle)
print(answer)