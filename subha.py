list1=[5]
list2=[]
list3=[]
list4=[]
for x in list1:
	if x%2==0:
		list2.append(x)
	elif x%2!=0:
		list3.append(x)
	else:
		list4.append(x)
print('the odd numbers are',list3)
print('the even numbers are',list2)		
print('the invalid numbers are',list4)
