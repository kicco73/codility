import heapq

def solution(F):

	target = sum(F) / 2
	F = [-f for f in F]
	heapq.heapify(F)
	print(target)

	result = 0
	while target > 0:
		max = -heapq.heappop(F)
		print(F)
		heapq.heappush(F, -max/2)
		target -= max/2
		result += 1

	return result
