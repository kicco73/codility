def solution(A):
	count = {}
	best_index = -1
	best_count = 0
	for index, a in enumerate(A):
		if a in count:
			count[a] += 1
		else:
			count[a] = 1
		if count[a] > best_count:
			best_index = index
			best_count = count[a]
	return best_index if best_count > len(A)/2 else -1

print(solution([3,4,3,2,3,-1,3,3]))