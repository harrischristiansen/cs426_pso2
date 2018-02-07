For this problem you will conduct frequency analysis on ciphertext to determine the original plain text.  Here is some background information to help you:  

The plaintext is written in English. It only contains capital letters (A-Z). All punctuation, spaces, line-breaks, numbers, and any other character outside of the range of A-Z have been removed. (You do not need to double-check this input, although you can if you wish.)  

The cipher used to encrypt the plain text simply substitutes all instances of a letter from the plaintext with another letter in the alphabet. For instance, the cipher could replace all instances of A with Z, all instances of B with X, etc. (a monoaphabetic cipher)  

In a cipher like this, one can use frequency analysis of normal text as a reference in guessing the mapping the cipher has used. For instance, one should see that if E is the most common letter in the English language, whatever letter that appears in the ciphertext the most often has high probability of being an E.  

Code Requirements:  

You will find the following files attached:  

- `file.text` Some training data you can use (Note Per Piazza Discussion Letters Here Should be made Uppercase as Input Stream is processed - Edit 10/5/18)
- `ciphertext.txt` The ciphertext to be decrypted
You can use either any programming language, but it should be your own code, commented and structured as per the class policies  

You should write a program with a source file named: `frequency_analysis.py`. This program when compiled/interpreted should do the following:  

- It should take its input from standard input
- The program should scan the input, ignore any characters not in the range of A-Z, and ignore any whitespace when processing the text.
- The program should keep track of the following frequencies:
	- The number of times each letter appears.
	- The number of times each adjacent pairs of letters appears. For example in: ABFT- {AB: 1}, {BF: 1}, {FT: 1}
	- The number of times each adjacent triplet of letters appears. For example in: ABFTVYU - {ABF: 1}, {BFT: 1}, {FTV: 1}, {TVY: 1}, {VYU: 1}
- The program should count the frequencies of each letter and your program should output to standard output the frequencies for each letter in sorted order with - the most frequent first. The format should be {A: 100}
- The program should count the frequencies of each pair and the program should output the frequencies for each pair in sorted order with most frequent first. The format should be like: {AB:100}
- The  program should count the frequencies of each triple and the program should output the frequencies for each triple in sorted order with most frequent first.- The format should be like: {ACF: 100}
- Test your code on the provided `file.txt`.  Include in your write up the top 10 each of the  most frequent letters, pairs, and triples along with the counts.
- Run your code on the `ciphertext.txt`. Include in your write up the top 10 most frequent letters, pairs, and triples along with the counts.

Include the plaintext of the ciphertext.  

(Hint: It may be helpful to write a separate program that iteratively substitutes letters with your guess in the ciphertext and leaves any characters you have not guessed as the one in the ciphertext.)  

Include your full code in the write up, with line numbers, and comments. Explain how your code works as part of the write up. If this part is missing then, no points will be awarded. You should use only the code you wrote to conduct the frequency analysis and not other services -- you will get ZERO credit if the code you turned in is not your own and does not do the above.  

Summary: you will turn in your code, the output of your code when run with the sample text, the output of your code run against the ciphertext, and the plaintext you discover from this  exercise.  