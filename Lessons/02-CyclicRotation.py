# Score: 100%

def rotate(A):
	return [A[-1]] + A[:-1] if A else []

def solution(A, K):
	for k in range(K):
		A = rotate(A)
	return A

print(solution([3, 8, 9, 7, 6], 5))
print(solution([], 5))
print(solution([3, 8, 9, 7, 6], -1))