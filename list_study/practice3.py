#Remove all of the vowels in a string
teststring = 'Find all of the words in a string that are less than 4 letters'
vowels = ['a','e','i','o','u',' ']
for i in teststring:
	if i in vowels:
		pass
	else:
		print(i, end='')
