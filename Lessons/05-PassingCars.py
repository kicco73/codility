# Score: 100%

def solution(A):

	tot = 0
	pairs = 0

	for a in A:
		if tot > 1000000000:
			return -1
		if a:
			tot += pairs
		else:
			pairs += 1

	return tot


print(solution([0,1,0,1]))