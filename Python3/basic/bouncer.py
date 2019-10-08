#ask for age
#age 18-21 wear wrist band
#21+ drink, normal entry
# less than 18 no entry

age = input("How old are you! ")

#while age:
#	input("How old are you! ")

if age:
	age = int(age)	
	if age>=18 and age <=21:
		print("You can enter but need a to wear a wrist band")
	elif age>21:
		print("Enjoy your concert and have a drink!")
	else:
		print(f"Sorry no entry for you! Come back later after {18-age} years")
else:
	print("Please enter a proper age")