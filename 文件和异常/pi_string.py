filename = 'pi_million_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()

print (pi_string[:52] + "...")
print (len(pi_string))
birthdday = input("Enter you birthday, in the form nmdddyy: ")
if birthdday in pi_string:
	print("You birthday appears in the first million digits of pi!")
else:
	print("You birthday does not appear in the first million digits of pi!")