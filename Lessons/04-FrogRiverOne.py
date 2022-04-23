# Score: 100%

def solution(X, A):

	leaves = set()

	for time, a in enumerate(A):
		leaves.add(a)
		if len(leaves) == X:
			return time

	return -1

print(solution(5, [1,3,1,4,0,3,5,4]))