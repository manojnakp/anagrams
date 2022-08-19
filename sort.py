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
	lines = map(lambda x: ' '.join(sorted(x.split())), lines)
	lines = sorted(lines, key = lambda x: ''.join(sorted(x[:x.index(' ')])))
	print('\n'.join(lines))
	print('\n')

if __name__ == '__main__':
	main()