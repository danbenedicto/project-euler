def sum_of_squares(n):
	return sum([i*i for i in range(1, n + 1)])

def square_of_sum(n):
	s = sum([i for i in range(1, n + 1)])
	return s * s

diff = square_of_sum(100) - sum_of_squares(100)
print(diff)