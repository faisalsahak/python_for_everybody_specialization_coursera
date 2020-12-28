 # Write a program that repeatedly prompts a user for 
 # integer numbers until the user enters 'done'. 
 # Once 'done' is entered, print out the largest and smallest of the numbers. 
 # If the user enters anything other than a valid number catch it with a try/except 
 # and put out an appropriate message and ignore the number. 
 # Enter 7, 2, bob, 10, and 4 and match the output below.

smallest = None
largest = None

while True:
	userInput = input("enter number")
	try:

		if userInput == 'done':
			break
		else:
			intNum = int(userInput)
			if smallest == None and largest == None:
				smallest = intNum
				largest = intNum
			else:
				if intNum > largest:
					largest = intNum
				elif intNum < smallest:
					smallest = intNum
	except:
		print("Invalid input")

print("Maximum is ", largest)
print("Minimum is ", smallest)
