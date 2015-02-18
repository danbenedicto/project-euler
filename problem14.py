# memoization!

lengths = {1: 1}

def start_of_longest_collatz_sequence(bound):

	def fill_lengths(lengths, start):
		if start in lengths:
			return
		elif start % 2 == 0:
			next = start / 2
		else:
			next = start * 3 + 1

		fill_lengths(lengths, next)
		lengths[start] = 1 + lengths[next]
		

	for start in range(2, bound):
		fill_lengths(lengths, start)

	return max(range(1, bound), key=lambda n: lengths[n])


answer = start_of_longest_collatz_sequence(1000000)
print(answer)