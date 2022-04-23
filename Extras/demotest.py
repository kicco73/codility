def solution(A):
	found = set(range(1, 100001))
	for a in A:
		if a in found:
			found.remove(a)
	return min(found)

print(solution([1, 3, 6, 4, 1, 2]))