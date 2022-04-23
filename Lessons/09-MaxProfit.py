# Score: 100%

def solution(A):
	max_profit = 0
	max_value = 0

	for index, a in enumerate(A[1:]):
		profit = a - A[index]
		max_value = max(profit, max_value + profit)
		max_profit = max(max_profit, max_value)

	return max_profit

print(solution([23171, 21011, 21123, 21366, 21367]))