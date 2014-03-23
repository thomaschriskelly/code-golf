def main():
	names_string = ""
	with open("names.txt", "r") as names_file:
		names_string = names_file.read()
	name_split = names_string.split(",")
	names = [name[1:-1] for name in name_split]
	names.sort()
	for name in names:
		score = name_score(name)

def letter_score(letter):
	lower = letter.lower()
	ascii_val = ord(lower)
	score = ascii_val - 96
	return score

def name_score(name):
	letter_scores = [letter_score(letter) for letter in name]
	return sum(letter_scores)

if __name__ == "__main__":
	main()
