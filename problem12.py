def num_divisors(n):
	"""Returns the number of divisors of n."""
	if n < 2:
		return 1 	# not really correct
	
	divisors = 1
	i = 2

	while n > 1:
		p = 0 	# p will be the maximum x such that i^x evenly divides n

		# repeatedly divide n by i, and store the number of times into p
		while (n % i == 0):
			n = n / i
			p += 1

		divisors = divisors * (p + 1)
		i += 1

	return divisors

def first_triangle_number(divisors):
	"""Returns the first triangle number with the given number of divisors."""
	if divisors < 1:
		return 0
	elif divisors == 1:
		return 1

	# approach: the nth triangle number is n * (n + 1) / 2
	# the number of divisors 

	n = 1 					# index of current triangle number
	n_divisors = 1			# number of divisors of n
	n_plus_1_divisors = 2 	# number of divisors of n + 1
	
	while(n_divisors * n_plus_1_divisors < divisors):
		n += 1
		n_divisors = n_plus_1_divisors
		n_plus_1_divisors = num_divisors((n + 1) if n % 2 == 0 else (n + 1) / 2)

	return (n * (n + 1)) / 2

answer = first_triangle_number(500)
print(answer)