#Count the number of spaces in a string 

teststring = 'Find all of the words in a string that are less than 4 letters'
count=0
for i in teststring:
	if i==' ':
		count+=1
print(count)