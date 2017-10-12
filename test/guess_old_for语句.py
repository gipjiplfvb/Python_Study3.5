age_of_oldboy = 77
for i in range(3):
	guess_age = int(input('guess old: '))
	if guess_age == age_of_oldboy:
		print ('You are good job')
		break
	elif guess_age > age_of_oldboy:
		print ('大了')
	else:
		print ('小了')
else:
	print ("you have tried too  many times...fuck off")



