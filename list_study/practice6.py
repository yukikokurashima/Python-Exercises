#Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3= [i+j for i,j in zip(list1, list2)]
print(list3)


for i, j in zip(list1, list2):
	print(i + j)

list4 = []
for i,j in zip(list1, list2):
	list4.append(i + j)
print(list4)

def my_zip(a, b):
	if len(a) != len(b):
		raise ValueError("lists have to be of the same size")

	c = []
	for i in range(len(a)):
		c.append(a[i] + b[i])

	return c

print(my_zip(list1, list2))

inp = ['axx,bxx,cxx']

res = []

spl = inp[0].split(',') 
for x in spl:
	res.append([x])

print(res)