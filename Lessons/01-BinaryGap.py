# Score: 100%

def solution(N):

	n = N
	state = 'init'
	max_gap = 0
	current_gap = 0

	while n:
		is_one = n & 1

		if state == 'init':
			state = 'sentinel_1' if is_one else 'init'
		elif state == 'sentinel_1':
			if not is_one:
				current_gap = 1
				state = 'sentinel_2'
		elif state == 'sentinel_2':
			if is_one:
				max_gap = max(current_gap, max_gap)
				state = 'sentinel_1'
			else:
				current_gap += 1

		n = n >> 1

	return max_gap

for N in [0b1000111111000000100000000]:
	print(solution(N))

