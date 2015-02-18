# https://projecteuler.net/problem=67
# input file: https://projecteuler.net/project/resources/p067_triangle.txt

import fileinput

def preprocess(text):
	''' Make a 2D list of integers (representing a triangle) from text '''
	return [[int(num) for num in line.split()] for line in text]

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

triangle = preprocess(fileinput.input())
answer = max_path_sum(triangle)
print(answer)