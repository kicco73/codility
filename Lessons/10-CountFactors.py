# Score: 100%

import math

def solution(N):
	count = 0
	m = int(math.sqrt(N))
	if math.sqrt(N) == m:
		count = 1
	else:
		m += 1

	for n in range(1, m):
		count += 2 if N % n == 0 else 0
	return count

print(solution(8))
