age_of_oldboy = 77
count = 0
while count < 3:
	count += 1
	guess_age = int(input('guess old: '))
	if guess_age == age_of_oldboy:
		print ('You are good job')
		break
	elif guess_age > age_of_oldboy:
		print ('大了')
	else:
		print ('小了')
	if count == 3:
		print("you have tried too  many times...fuck off")
else:
	print ("you have tried too  many times...fuck off")



