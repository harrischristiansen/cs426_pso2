'''
	@ Harris Christiansen (Code@HarrisChristiansen.com)
	File Created: February 2018
	Purdue CS426 Computer Security - PSO 2 - https://github.com/harrischristiansen/cs426_pso2
	Problem 8 - Frequency Analysis
'''

from collections import Counter
import re, string

TEXT_DENY_PATTERN = re.compile('[^a-zA-Z]+')
NUM_TOP_FREQS = 10

################# Getting Text #################

def getPlaintext():
	with open("file.txt","r") as f:
		return f.read()

def getCiphertext():
	with open("ciphertext.txt","r") as f:
		return f.read()

def formatText(text): # Return only [A-Z] in uppercase text
	justLetters = TEXT_DENY_PATTERN.sub('', text)
	return justLetters.upper()

################# Single Character Frequency Analysis #################

def getSinglesFrequencies(text):
	return Counter(text)

################# Double Character Frequency Analysis #################

def getDoubles(text):
	for i, v in enumerate(text):
		try:
			yield v, text[i + 1]
		except IndexError:
			return

def getDoublesFrequencies(text):
	doubles = getDoubles(text)
	return Counter(doubles)

################# Triple Character Frequency Analysis #################

def getTriples(text):
	for i, v in enumerate(text):
		try:
			yield v, text[i + 1], text[i + 2]
		except IndexError:
			return

def getTriplesFrequencies(text):
	triples = getTriples(text)
	return Counter(triples)

################# Complete Frequency Analysis #################

def getDictFromFreqs(freqs):
	result = {}
	for freq in freqs:
		text = ''.join(freq[0])
		result[text] = freq[1]
	return result

def getTopFrequencies(text, count=NUM_TOP_FREQS):
	singles = getSinglesFrequencies(text).most_common(count)
	doubles = getDoublesFrequencies(text).most_common(count)
	triples = getTriplesFrequencies(text).most_common(count)

	return {
		'singles': getDictFromFreqs(singles),
		'doubles': getDictFromFreqs(doubles),
		'triples': getDictFromFreqs(triples),
	}

def printTopFrequencies(text="", freqs=None):
	if freqs == None:
		freqs = getTopFrequencies(text)

	print("Singles: %s" % freqs["singles"])
	print("Doubles: %s" % freqs["doubles"])
	print("Triples: %s" % freqs["triples"])

################# Main #################

if __name__ == '__main__':
	plaintext = formatText(getPlaintext())
	printTopFrequencies(plaintext)

	ciphertext = getCiphertext()
	printTopFrequencies(ciphertext)
