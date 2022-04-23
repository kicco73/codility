# Score: 100%

def solution(N, A):
	R = [0] * N
	max_val = 0
	pending_max = False
	for a in A:
		if a > N:
			pending_max = True
		else:
			if pending_max: 
				R = [max_val] * N
				pending_max = False
			R[a-1] += 1
			max_val = max(R[a-1], max_val)
	if pending_max: 
		R = [max_val] * N
	return R

print(solution(5, [3,4,4,6,1,4,4]))
print(solution(1, [1]))