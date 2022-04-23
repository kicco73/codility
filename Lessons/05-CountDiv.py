def solution(A, B, K):
	a = A // K if A % K else A // K - 1
	b = B // K
	return b - a

print(solution(6, 11, 2))