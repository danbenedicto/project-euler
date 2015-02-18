# 2^1000 (mod 10^x) == (2^500 * 2^500) (mod 10^x) .. is this helpful?
# part of me wants to figure out an efficient solution, but another part
# just wants to accept the straightforward solution and move on


# super easy way with strings: 
answer = sum([int(c) for c in str(2 ** 1000)])
print(answer)