# Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and 
# then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, 
# sorted by hour as shown below.

def printDic(dic):
	lst = list()
	for k, v in dic.items():
		lst.append((v,k))
		
	lst = sorted(lst, reverse=True)
	# print(lst)
	# lst.sort(key = lambda x: x[1]) 
	# print(lst)
	for v, k in lst[:]:
		print(k, v)
	# for k, v in dic.items():
	# 	print(k,v)

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()

for line in handle:
	if line.startswith('From '):
		splt = line.split()
		time = splt[5]
		timeArr = time.split(":")
		hour = timeArr[0]
		if hour in dic:
			dic[hour] = dic[hour] + 1
		else:
			dic[hour] = 1
		# print(hour)

printDic(dic)
