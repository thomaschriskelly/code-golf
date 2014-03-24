#!/usr/bin/env python

'''
This is a solution to the Euler Project problem #22. The problem can be found at: https://projecteuler.net/problem=22

A string is given a score based on the sum of the position of each of its letters in the alphabet.
A file of names is read, and each name is given a score based on the product of its string score and its position in the list of sorted names.
The main function prints the sum of all scores
'''

def main():
	names_string = file_to_string("names.txt")
	name_split = names_string.split(",")
	names = [name[1:-1] for name in name_split]
	names.sort()

	total_scores = 0
	alpha_position = 1
	for name in names:
		score = name_value(name) * alpha_position
		total_scores += score
		alpha_position += 1
	print total_scores

def file_to_string(filename):
	"""reads a file, returns the contents as a string"""
	with open(filename, "r") as names_file:
		return names_file.read()

def letter_value(letter):
	"""returns the score value of a single letter (string)"""
	lower = letter.lower()
	ascii_val = ord(lower)
	value = ascii_val - 96 # lowercase 'a' is ASCII 97
	return value

def name_value(name):
	"""returns the score value of a name (string)"""
	letter_scores = [letter_value(letter) for letter in name]
	return sum(letter_scores)

if __name__ == "__main__":
	main()
