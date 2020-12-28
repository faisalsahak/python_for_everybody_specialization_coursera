# Write a program to read through the mbox-short.txt and figure out who has 
# sent the greatest number of mail messages. The program looks for 'From '
# lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address 
# to a count of the number of times they appear in the file. After the dictionary is 
# produced, the program reads through the dictionary using a maximum loop to find 
# the most prolific committer.

def printContent(dic):
	k = ''
	v = 0
	for key, value in dic.items():
		if value > v:
			k = key
			v = value
		# print(key, value)
	return (k,v)

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()

for line in handle:
	if line.startswith("From "):
		lineArr = line.split()
		sec = lineArr[1]
		# dic.append(sec)
		# dic.get(sec,0) + 1
		if sec in dic:
			dic[sec] = dic[sec] + 1
		else:
			dic[sec] = 1
		# print(line)

# print(len(dic.values()))
key, value = printContent(dic)
print(key,value)
