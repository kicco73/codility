# given an infinite checkboard, move a knight from the coordinates (x0, y0) to (xn, yn)
# using the mininum number of moves.

possible_moves = lambda x, y: [
		(x, y),
		(x-1, y-2),
		(x-1, y+2),
		(x+1, y-2),
		(x+1, y+2),
		(x-2, y-1),
		(x-2, y+1),
		(x+2, y-1),
		(x+2, y+1),
	]

def solution(x0, y0, xn, yn):

	queue = []
	already_been = set()

	queue.append((x0, y0, 0))
	already_been = set((x0, y0))

	while queue:
		x0, y0, moves = queue[0]
		queue = queue[1:]
	
		if (x0, y0) == (xn, yn):
			return moves

		for (xi, yi) in possible_moves(x0, y0):

			if (xi, yi) not in already_been:
				already_been.add((xi, yi))
				queue.append((xi, yi, moves + 1))

print(solution(0,0, 3,0))