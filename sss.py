list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
list3=[]
for x in list1:
if x%2==0:
list2.append(x)
else:
list3.append(x)
print('the odd numbers are',list3)
print('the even numbers are',list2)
