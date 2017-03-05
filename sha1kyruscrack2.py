import hashlib


answer = ""
# Alphabet for testing each letter against puzzle
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ".", "-", "?", "!", ":", ";", "(", ")", "[", "]", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "@", "#", "$", "%", "^", "&", "*", "+", "~", "`", "\\", "/", "<", ">", "{", "}", "_", "|", "\n"]

cnt = 1

def hashmaker(word):
	return hashlib.sha1(word).hexdigest() + "\n"

# Grabs line from puzzle
with open("part2.txt","r") as f:
    for line in f:
    	print cnt
    	cnt+=1
	# Compares generated hash for each alphabet letter to the hash in the puzzle
        for letter in alphabet:
        	print "Comparing... %r" % line 
        	if line == hashmaker(answer + letter):
        		#print "first"
        		print "Y"
        		answer = answer + letter
        		break
		# Compares uppercase letters
        	elif line == hashmaker(answer + letter.upper()):
        		#print "second"
        		print "Y"
        		answer = answer + letter.upper()
        		break
        	#else: #print "Failed."



print "The answer is %r" % answer

# Writes answer to text file
print "Writing to part3.txt..."

shafile2 = open("test.txt", "w")
shafile2.write(answer)
shafile2.close()
