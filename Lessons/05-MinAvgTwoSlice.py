# Score: 50%

def value(prefix_sum, k, j):
	return prefix_sum[j] - prefix_sum[k-1] if k else prefix_sum[j]

def solution(A):
	min_avg = None

	prefix_sum = []
	for i, a in enumerate(A):
		sum = prefix_sum[i-1] + a if i else a
		prefix_sum.append(sum)

	min_avg = None
	min_pos = None

	for k in range(len(A)):
		for j in range(k+1, len(A)):
			avg = value(prefix_sum, k,j) / (j-k+1)
			if min_avg is None or min_avg > avg:
				min_pos = k
				min_avg = avg

	return min_pos

print(solution([4,2,2,5,1,5,8]))	
