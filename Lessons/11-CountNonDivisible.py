import math
from functools import lru_cache

@lru_cache(maxsize=50000)
def first_primes(N):
	limit = int(math.sqrt(N))
	F = {x: True for x in range(2, N+1)}

	for f in F.keys():
		if f > limit: break
		if not F[f]: continue
		for i in range(2, N // f + 1):
			F[f*i] = False
	return [f for f, d in F.items() if d]

@lru_cache(maxsize=50000)
def factorisation(N):
	limit = int(math.sqrt(N))

	primes = first_primes(100000)
	result = {1, N}

	for prime in primes:
		if prime > limit: break
		if (N / prime) % 1 == 0: 
			result.add(prime)
			result.add(N // prime)
	return result

def solution(A: list):

	result = []

	for a in A:	
		factors = factorisation(a)

		count = len(A)
		for aa in A:
			count -= 1 if aa in factors else 0			
		result.append(count)
	return result

print(solution([3,1,2,3,6]))