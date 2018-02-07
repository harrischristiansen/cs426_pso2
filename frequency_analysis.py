'''
	@ Harris Christiansen (Code@HarrisChristiansen.com)
	File Created: January 2018
	Purdue CS426 Computer Security - PSO 1 - https://github.com/harrischristiansen/cs426_pso1
	Problem 5 - Estimated Time to Brute-Force Passwords
'''

PASSWORDS_PER_SECOND = pow(2,48)
DAYS_PER_MONTH = 30.45

def secondsToHuman(total):
	years = total // (60*60*24*365)
	months = total % (60*60*24*365) // (60*60*24*DAYS_PER_MONTH)
	days = total % (60*60*24*DAYS_PER_MONTH) // (60*60*24)
	hours = total % (60*60*24) // (60*60)
	minutes = total % (60*60) // (60)
	seconds = total % 60
	return "%d Years, %d Months, %d Days, %d Hours, %d Minutes, %d Seconds" % (years, months, days, hours, minutes, seconds)

# Part a: [8,14] chars length, containing [a-z]
a_chars = 26
a_possibilities = pow(a_chars,8) + pow(a_chars,9) + pow(a_chars,10) + pow(a_chars,11) + pow(a_chars,12) + pow(a_chars,13) + pow(a_chars,14)
a_seconds = a_possibilities/PASSWORDS_PER_SECOND
print("Part a: %s" % secondsToHuman(a_seconds))

# Part b: [8,14] chars length, containing [a-zA-Z]
b_chars = 26 + 26
b_possibilities = pow(b_chars,8) + pow(b_chars,9) + pow(b_chars,10) + pow(b_chars,11) + pow(b_chars,12) + pow(b_chars,13) + pow(b_chars,14)
b_seconds = b_possibilities/PASSWORDS_PER_SECOND
print("Part b: %s" % secondsToHuman(b_seconds))

# Part c: [8,14] chars length, containing [a-zA-Z0-9]
c_chars = 26 + 26 + 10
c_possibilities = pow(c_chars,8) + pow(c_chars,9) + pow(c_chars,10) + pow(c_chars,11) + pow(c_chars,12) + pow(c_chars,13) + pow(c_chars,14)
c_seconds = c_possibilities/PASSWORDS_PER_SECOND
print("Part c: %s" % secondsToHuman(c_seconds))

# Part d: [8,14] chars length, containing [a-zA-Z0-9], starting with a birth-year XXXX (E.G. 1990)
def numpos_year(passlen): # Starts with XXXX = [(19)(20)][0-9][0-9]
	d_chars = 26 + 26 + 10
	return 2 * 10 * 10 * pow(d_chars, passlen-4)
d_possibilities = numpos_year(8) + numpos_year(9) + numpos_year(10) + numpos_year(11) + numpos_year(12) + numpos_year(13) + numpos_year(14)
d_seconds = d_possibilities/PASSWORDS_PER_SECOND
print("Part d: %s" % secondsToHuman(d_seconds))
