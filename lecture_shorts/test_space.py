print ("Please enter a value where x < y")

while True:
	print ("beginning of loop")
    
	try:
		print ("X and Y must both be integers")
		x, y = (input("Please enter X/Y ").split("/"))
		x = int(x)
		y = int(y)
		if x < 0:
					print ("iffy")

	except ValueError:
		print("Bad Value")
		# x = int(x) removed, exception should restate then restart loop
		# y = int(y) this setup would cause a retry of the error causing function

	except NameError:
		print("No cats allowed")
		continue
	
	else:
		print ("else/break")
		break	