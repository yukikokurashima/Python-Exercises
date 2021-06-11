#Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3=[i+j for j in list1 for i in list2]
for i in list1:
	for j in list2:
		print(i+j)






#list3=[i+j for j in list1 for i in list2]
#for i in list1:
#	for j in list2:
#		print(i+j)
