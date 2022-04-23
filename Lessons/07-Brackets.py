# Score: 100%

def solution(S):
	stack = []
	brackets = {'{': '}', '[': ']', '(': ')'}
	for s in S:
		if s in brackets:
			stack.append(brackets[s])
		else:
			if not stack:
				return 0
			expected = stack.pop() 
			if s != expected:
				return 0

	return 0 if stack else 1

print(solution('[]'))

