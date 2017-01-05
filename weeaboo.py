print """
Hello there, you don't know who I am.
However, I want to play a game with you.

Please tell me your name.
"""
name = raw_input("> ")

print "Hello, %s. If you can tell me who best girl is, you can continue on. If not, there are consequences." % name

print "If you can tell me who best girl is, you win."

print "1. Nico nico niii~   2. Eli oneesabitch    3. Honk"

best_girl = raw_input("Choose wisely ~ >")

if best_girl == "1":
	print """
	Congratulations! You have chosen the first test correctly, %s-san. 
	I am happy to say you have won this round. Nico Nico Nii~ forever, brother!
	""" % name

	print """
	Now, it's time for question 2, oniichan. 'knee highs' or 'thigh highs'?
	"""
	socks = raw_input("> ")

	if socks == "knee highs":
		print "You fool. You may have gotten the first question right, but you have now lost my favor. Get out of my sight."
	elif socks == "thigh highs":
		print "Congratulations, 10 chicken tendies for you. I'm now getting bored. Game over. You win."
	else:
		print """You think you're funny, don't you, %s? die. - 100 HP.


					GAME OVER
				""" % name

elif best_girl == "2":
	print """
	You have chosen half correctly. Partial credit, ya monkey.
	Think better on the next game, baka. 
	"""
else:
	print """
	You fool. You absolute fucking FOOL.
	REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
	EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
	EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
	EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
	EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
	EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
	EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
	EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
	EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
	EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
	"""
	print """
	This is the end of the game for you. If you can't even get the first 
	question partially correct, you must end here. 
	Good night, young pepperoni pastarino san.
	"""