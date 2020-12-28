# Open the file romeo.txt and read it line by line. For each line, split the 
# line into a list of words using the split() method. The program should build 
# a list of words. For each word on each line check to see if the word is already 
# in the list and if not append it to the list. When the program completes, sort 
# and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

def checkWord(word, lst):
	for i in range(len(lst)):
		if lst[i] == word:
			return True

	return False

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	#split the line
	words = line.split()
	for word in words:
		#check to see if the word is in the list
		if checkWord(word, lst) :
			continue
		else:
			#if it is ignore otherwise add it to the list
			lst.append(word)

#sort the list and print
lst.sort()
print(lst)
# print(line.rstrip())