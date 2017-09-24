
#Peace Iyiewuare & Rut Merida
#concordance??
#
#4/27/17

import time
import random


def RemovePunctuation(string): #removes sepecial characters 
	for letter in string: #letter in string
		for ch in ".,:;'\"\n-'!":
			if letter == ch:
				string = string.replace(ch,"")
			
	return string.lower()

def SuperRemovePunctuation(string): #removes blank spaces that keep showing up for some reason
	for letter in string: #letter in string
		for ch in ".,:;'\"\n-'! ":
			if letter == ch:
				string = string.replace(ch,"")
			
	return string.lower()

def make_dic(doc):
	lines = doc.readlines()
	concordance = {}
	line_num = 0
	for line in lines:
		if line.strip() != "":
			line_num += 1
			line = RemovePunctuation(line)
			for word in line.split(" "):
				word = SuperRemovePunctuation(word)
				#print("STRING BELOW IS A WORD")
				#print (word)
				if len(word) != 0:
					if word not in concordance:
						concordance[word] = [line_num]
					elif word in concordance:
						concordance[word].append(line_num)
		else:
			pass
	return concordance

def printEntry(word, concordance):
	if word in concordance:
		for line_num in concordance[word]:
			print(line_num, end = " ")
	elif word not in concordance:
		print (word[0].upper(), word[1:]," not found!", sep = "")
	
def main():
	document = input("What text file would you like to input? ") #input text file!
	doc = open(document,"r")

	concordance = make_dic(doc)
	
	findWord = input("What word would you like to try and find? ") #input words you'd like to find
	
	if findWord.isalpha() == True: #checks if string is all letters
		for i in range(4): #personal effecets
			rand_time = random.uniform(0.75,1.5)
			print("looking for word...")
			time.sleep(rand_time)
		time.sleep(2)
		printEntry(findWord, concordance) #prints the line numbers where the word is found
	else:
		for i in range(2): #personal effecets
			rand_time = random.uniform(0.75,1.5)
			print("looking for word...")
			time.sleep(rand_time)
		time.sleep(2)
		print()
		print("Error :(")
		print("Your word doesn't contain only letters.") #error is string isn't just letters
		print ("You must enter a word!")
	
	
if __name__ == '__main__':
	main()