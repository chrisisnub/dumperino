import hashlib


answer = ""
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ".", "-", "?", "!", ":", ";", "(", ")", "[", "]", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "@", "#", "$", "%", "^", "&", "*", "+", "~", "`", "\\", "/", "<", ">", "{", "}", "_", "|", "\n"]

cnt = 1

def hashmaker(word):
	#print word
	#print hashlib.md5(word).hexdigest()
	return hashlib.md5(word).hexdigest() + "\n"

with open("puzzle.txt","r") as f:
    for line in f:
    	print cnt
    	cnt+=1
        #print line
        #print "Testing"
        for letter in alphabet:
        	#print "Comparing... %r" % line 
        	if line == hashmaker(answer + letter):
        		#print "first"
        		print "Y"
        		answer = answer + letter
        		break
        	elif line == hashmaker(answer + letter.upper()):
        		#print "second"
        		print "Y"
        		answer = answer + letter.upper()
        		break
        	#else: #print "Failed."



print "The answer is %r" % answer


print "Writing to part2.txt..."

shafile = open("part2.txt", "w")
shafile.write(answer)
shafile.close()
