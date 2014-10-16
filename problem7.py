# this could be better

def nth_prime(n):
	if n == 1:
		return 2
	
	primes = [2]	# store primes here
	candidate = 3	# next number to test for prime-ness
	
	while (n > 1):
		if is_prime(candidate, primes):
			primes.append(candidate)
			n -= 1

		candidate += 1

	return candidate - 1	# because we just incremented the last prime

def is_prime(candidate, smaller_primes):
	for i in smaller_primes:
		if (candidate % i == 0):
			return False
	return True

answer = nth_prime(10001)
print(answer)