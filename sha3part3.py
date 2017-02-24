from Crypto.Hash import SHA256


answer = ""
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ".", "-", "?", "!", ":", ";", "(", ")", "[", "]", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "@", "#", "$", "%", "^", "&", "*", "+", "~", "`", "\\", "/", "<", ">", "{", "}", "_", "|", "\n"]

cnt = 1

def hashmaker(word):
	print word
	sha= SHA256.new()
	sha.update(word)
	sha.digest()
	print sha.hexdigest()
	return sha

with open("test.txt","r") as f:
    for line in f:
    	print cnt
    	cnt+=1
        print line
        print "Testing"
        for letter in alphabet:
        	print "Comparing... %r" % line 
        	mash = answer + letter
        	mashUP = answer + letter.upper()
        	if line == hashmaker(mash):
        		#print "first"
        		print "Y"
        		answer = answer + letter
        		break
        	elif line == hashmaker(mashUP):
        		#print "second"
        		print "Y"
        		answer = answer + letter.upper()
        		break
        	#else: #print "Failed."



print "The answer is %r" % answer


#print "Writing to part2.txt..."

#shafile = open("part2.txt", "w")
#shafile.write(answer)
#shafile.close()
