from math import factorial

# could easily optimize this (by memoizing factorial)
def num_routes(m, n):
	return int(factorial(m + n)/(factorial(m) * (factorial(n))))

answer = num_routes(20, 20)
print(answer)