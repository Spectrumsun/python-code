import re
total = 0
love = open("regex_sum_177615.txt")
lost = love.read()
hate = re.findall('[0-9]+' ,lost)
for line in hate:
	will = int(line)
	total = total + will
print total


#hand = open("mbox-short.txt")
#for line in hand:
#	line = line.rstrip()
##		print line



#hand = open("mbox-short")
##	if line.find("From:") >=0:
#		print line



#y = re.findall ("[AEIOU]+",x)
#print y


#ff = open(mbox-short.txt) 
#w = re.findall("\S+@\S+",x)
#x = re.findall ("^From  (\S+@\S+)",x)
#z = re.findall ("@([^ ]*) ", lin)
#print x, w, z