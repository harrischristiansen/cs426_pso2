'''
	@ Harris Christiansen (Code@HarrisChristiansen.com)
	File Created: February 2018
	Purdue CS426 Computer Security - PSO 2 - https://github.com/harrischristiansen/cs426_pso2
	Problem 8 - Frequency Analysis
'''

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

def getFrequencies(items):
	counts = {}
	for item in items:
		value = ''.join(item)
		if value in counts:
			counts[value] += 1
		else:
			counts[value] = 1
	return dict(sorted(counts.items(), key=lambda k: counts[k[0]], reverse=True))

def getSinglesFrequencies(text):
	return getFrequencies(list(text))

################# Double Character Frequency Analysis #################

def getDoubles(text):
	doubles = []
	for i, v in enumerate(text):
		try:
			double = (v, text[i + 1])
			doubles.append(double)
		except IndexError:
			return doubles
	return doubles

def getDoublesFrequencies(text):
	doubles = getDoubles(text)
	return getFrequencies(doubles)

################# Triple Character Frequency Analysis #################

def getTriples(text):
	triples = []
	for i, v in enumerate(text):
		try:
			triple = v, text[i + 1], text[i + 2]
			triples.append(triple)
		except IndexError:
			return triples
	return triples

def getTriplesFrequencies(text):
	triples = getTriples(text)
	return getFrequencies(triples)

################# Complete Frequency Analysis #################

def getTopFrequencies(text, count=NUM_TOP_FREQS):
	singles = dict(list(getSinglesFrequencies(text).items())[:count])
	doubles = dict(list(getDoublesFrequencies(text).items())[:count])
	triples = dict(list(getTriplesFrequencies(text).items())[:count])

	return {
		'singles': (singles),
		'doubles': (doubles),
		'triples': (triples),
	}

def printTopFrequencies(text="", freqs=None):
	if freqs == None:
		freqs = getTopFrequencies(text)

	print("Singles: %s" % freqs["singles"])
	print("Doubles: %s" % freqs["doubles"])
	print("Triples: %s" % freqs["triples"])

################# Decipher #################

def getListSingleFreqs(text):
	freqs = getSinglesFrequencies(text)
	return list(freqs.keys())

def createFreqReplacementMap(source_freqs, target_freqs):
	replacements = {}
	for i, freq in enumerate(source_freqs):
		replacements[freq] = target_freqs[i]
	return replacements

def replaceBySingleFreq(text, target_freqs):
	freqs = getListSingleFreqs(text)
	replacements = createFreqReplacementMap(freqs, target_freqs)
	#print(replacements)

	result = ""
	for c in text:
		result += replacements[c]

	return result

################# Main #################

if __name__ == '__main__':
	plaintext = formatText(getPlaintext())
	#printTopFrequencies(plaintext)

	ciphertext = getCiphertext()
	#printTopFrequencies(ciphertext)

	#target_freqs = getListSingleFreqs(plaintext) # ['E', 'T', 'O', 'A', 'I', 'S', 'N', 'R', 'H', 'L', 'D', 'U', 'M', 'Y', 'C', 'W', 'F', 'G', 'B', 'P', 'K', 'V', 'X', 'J', 'Q', 'Z']
	target_freqs = ['E', 'T', 'A', 'O', 'H', 'R', 'N', 'D', 'I', 'L', 'S', 'W', 'C', 'V', 'F', 'U', 'G', 'B', 'M', 'P', 'Y', 'K']
	deciphered_text = replaceBySingleFreq(ciphertext, target_freqs)
	print(deciphered_text)
