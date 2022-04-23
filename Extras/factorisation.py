# Using siege of Erathostenes

import math

def first_primes(N):
	limit = int(math.sqrt(N))
	F = {x: True for x in range(2, N+1)}

	for f in F.keys():
		if f > limit: break
		if not F[f]: continue
		for i in range(2, N // f + 1):
			F[f*i] = False
	return [f for f, d in F.items() if d]

def factorisation(N):
	limit = int(math.sqrt(N))
	F = {x: 0 for x in range(2, N+1)}

	for f in F.keys():
		if f > limit: break
		if F[f] is None: continue
		F[f] = N // f if (N/f) % 1 == 0 else None
		for i in range(2, N // f + 1):
			F[f*i] = 0
	return {f: d for f, d in F.items() if d} or {N: 1}

print(factorisation(22))