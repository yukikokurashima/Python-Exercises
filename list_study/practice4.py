#Find all of the words in a string that are less than 4 letters
teststring = 'Find all of the words in a string that are less than 4 letters'
list_teststring=teststring.split()
list=list(map(list, list_teststring))
for i in list:
	if len(i) <4:
		print(''.join(i))