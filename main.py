from random import shuffle, choice
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

	words = choice(lines).split(' ')
	word = choice(words)
	wlist = list(word)
	shuffle(wlist)
	jumbled = ''.join(wlist)

	print("Anagram:", jumbled)
	ans = input("Guess: ").strip()
	while ans not in words:
		print('Incorrect! Try again')
		ans = input("Guess: ").strip()
	print("Hurray! Correct guess")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print()
		sys.exit('Bye')
	except EOFError:
		sys.exit('')
