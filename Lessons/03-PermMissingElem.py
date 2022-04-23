# Score: 100%

def solution(A):
	s = set(range(1, len(A)+2))
	for a in A:
		s.remove(a)
	return s.pop()

print(solution([]))