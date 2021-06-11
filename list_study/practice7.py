#Given a Python list of numbers. Turn every item of a list into its square


def square(square):
	for i in range (len(square)):
		square[i]=square[i]*square[i]
		i+=1
	return i
aList = [1, 2, 3, 4, 5, 6, 7]
square(aList)
print(aList)

