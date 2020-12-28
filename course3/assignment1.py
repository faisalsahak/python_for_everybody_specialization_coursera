import re

inp = input("enter file name")
if len(inp) == 0:
	inp = "sample.txt"

file = open(inp)

def sumList(lst):
	count = 0
	if len(lst)> 0:

		for i in lst:
			count = count + int(i)
	return count

finalCount = 0

for line in file:
	# print(line)
	nums = re.findall("[0-9]+", line)
	# if len(nums)>= 0:

	finalCount = finalCount + sumList(nums)
	# print(type(nums))

print(finalCount)


# finput = input("Enter the file name: ")
# fhand = open(finput, "r")
# totalsum = 0

# for line in fhand:
# 	numlist = re.findall('[0-9]+', line)
# 	if len(numlist) > 0:
# 		for item in numlist:
# 			totalsum = totalsum + int(item)
	
# print(totalsum)
