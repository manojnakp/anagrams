import sys

def main():
	loc = 'words.txt'
	if len(sys.argv) == 2:
		loc = sys.argv[1]
	try:
		f = open(loc)
	except FileNotFoundError:
		sys.exit(f'Reuested file "{loc}" is not found')
	else:
		with f:
			lines = f.read().split('\n')

	if '' in lines:
		lines.remove('')

	visited = {}

	for line in lines:
		if line.find(' ') == -1:
			sys.exit(f'Single word in line:\n{line}')
		words = map(lambda x: ''.join(sorted(x)), line.split())
		wset = set(words)
		if len(wset) != 1:
			sys.exit(f'Invalid line! Words are not anagrams of each other:\n{line}')
		word = wset.pop()
		if word in visited:
			sys.exit(f'Two lines of identical anagrams:\n{line}\n{visited[word]}')
		visited[word] = line
	print("Valid words file")

if __name__ == '__main__':
	main()
