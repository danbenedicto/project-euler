from math import sqrt

def pythagorean_triplet(total):
	for a in range(total):
		for b in range(a):
			c = sqrt(a * a + b * b)		# floating point makes this error-prone?

			if (c % 1 == 0):
				# {a, b, c} is a pythagorean triple
				c = int(c)
				if (a + b + c == total):
					return a * b * c
	
	return -1 	# definitely no triple whose sum is @total

answer = pythagorean_triplet(1000)
print(answer)