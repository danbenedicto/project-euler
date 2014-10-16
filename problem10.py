def primes_below(n):
	"""Uses the sieve of eratosthenes to generate a list of all prime
	numbers less than n."""
	nums = range(2, n)	# 
	primes = []
	for i in range(len(nums)):
		if nums[i]:
			# n has not been 'sieved' by smaller numbers, must be prime
			primes.append(nums[i])
			for j in range(i, len(nums), nums[i]):
				nums[j] = None	# mark all multiples of nums[i] as composite (None)
	return primes

answer = sum(primes_below(2000000))
print(answer)