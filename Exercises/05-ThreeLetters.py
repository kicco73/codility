# Score: 53%
# Failing: timeouts

def solution(A, B):
	
	automaton = {
		'init': {'a': 'A', 'b': 'B'},
		'A': {'a': 'AA', 'b': 'B'},
		'B': {'a': 'A', 'b': 'BB'},
		'AA': {'b': 'B'},
		'BB': {'a': 'A'},
	}
	
	queue = [('init', A, B, '')]

	while queue:
		state, A, B, output = queue[0]
		queue = queue[1:]
		
		if not A and not B:
			return output

		if A and 'a' in automaton[state]:
			queue.append((automaton[state]['a'], A-1, B, output+'a'))
		if B and 'b' in automaton[state]:
			queue.append((automaton[state]['b'], A, B-1, output+'b'))

	return ''

print(solution(4, 1))