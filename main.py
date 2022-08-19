from random import shuffle, choice
import sys

def main():
	with open('words.txt') as f:
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
	if ans in words:
		print("Hurray! Correct guess")
	else:
		print("Incorrect")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print()
		sys.exit('Bye')
	except EOFError:
		sys.exit('')
