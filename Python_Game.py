'''
Python command line scenario game
Command line game of life

'''
print "Welcome to command line life"
print "To get started, press 'Enter'"
enter = raw_input(">>> ")

print "Choose a career"
print "Teacher(1):"
print "Doctor(2):"
print "Lawyer(3):"
print "Engineer(4)"

# Begin Teacher
scenario = raw_input(">>> ")


if scenario == "1":
	print "You are now a teacher, educating and mentoring future generations, what will you do next? "
	print "1: Continue your education with a Phd"
	print "2: Continue your schooling and achieve a doctorate degree"
	print "3: Pursue another career"
	print "4: Work until retirement"
	scenario1 = raw_input(">>> ")

	if scenario1 <= "2":
		print "Congratulations, you have now received your degree!"
	elif scenario1 == "3":
		print "All that time and money invested in school to just quit! What's wrong with you!?"
	elif scenario1 == "4":
		print "Sounds like a plan, at what age will you retire?"
	else:
		exit()
		

#End Teacher

#Begin Doctor
if scenario == "2":
	print "A very prestigous choice, we ensure a healthy, lively population,what will be your next step?"
	print "1: Become your own boss"
	print "2: Go on vacation"
	print "3: Party"
	print "4: Start thinking about how much debt your in"

	print "Enter to Continue"

	doctor = raw_input(">>> ")
	if doctor == "1":
		print "Congratulations you no longer have 10+ years of schooling and you don't have to take crap from anyone"
	elif doctor == "2":
		print "Go on vacation, you've earned it"
	elif doctor == "3":
		print "Bad choice, you ended up trying to drive home drunk. You were arrested, convicted and had your degree revoked"
	elif doctor == "4":
		print "You have $415,000 dollars of debt accumulated, better start paying on it now!"
	else:
		print "Not a valid operation, please retry"


# End Doctor

#Begin lawyer


if scenario == "3":
	print "Congratulations you are now a professional liar and can get anyone out of even the most stickiest of situations"
	print "What's your next move?"
	print "1: Become a judge"
	print "2: Get to work in the courthouse"
	print "3: Figure out what to do next"
	print "4: Have fun"

	lawyer = raw_input(">>> ")

	if lawyer == "1":
		print "Being a judge is more sressful than you think"
	elif lawyer == "2":
		print "Who knew getting paid to lie is so much fun"
	elif lawyer == "3":
		print "You are still figuring..."
	elif lawyer == "4":
		print "You have too much fun and end up dying!"

#End lawyer
 
 #Begin Engineer

if scenario == "4":
	print "Indeed a great choice, we are revered as the backbone of a growing economy"
 	print "1: Build stuff"
 	print "2: Destroy stuff"
 	#print "3:"
 	#print "4:"

 	engineer = raw_input(">>> ")

 	if engineer == "1":
 		print "Great job you built a revolutionary medical device and won the noble prize!"
 	elif engineer == "2":
 		print "BOOM!"

#End Engineer
