'''
	@ Harris Christiansen (Code@HarrisChristiansen.com)
	File Created: February 2018
	Purdue CS426 Computer Security - PSO 2 - https://github.com/harrischristiansen/cs426_pso2
	Problem 8 - Frequency Analysis
'''

import re, string

TEXT_ACCEPT_PATTERN = re.compile('[^a-zA-Z]+')

def getPlaintext():
	f = open("file.txt","r")
	return f.read()

def getCiphertext():
	f = open("ciphertext.txt","r")
	return f.read()

def formatText(text): # Transform [a-z] to [A-Z], and then only accept [A-Z]
	justLetters = TEXT_ACCEPT_PATTERN.sub('', text)
	return justLetters.upper()

plaintext = getPlaintext()
formatted = formatText(plaintext)

print(formatted)