def solution(message, K):
	if K >= len(message):
		return message

	k = min(len(message), K)
	k = max(k, 0)

	if message[k] == ' ':
		return message[:k]

	while k and message[k] != ' ':
		k -= 1
		
	return message[:k]


print ('-' + solution('Codility We test coders', 14) + '-')

for x in range(10):
	print ('-' + solution('Why not', x) + '-')

print ('-' + solution('The quick brown fox jumps over the lazy dog', 39) + '-')
print ('-' + solution('To crop or not to crop', 21) + '-')


