chr=input()
if((chr>='a' and chr<='z') or (chr>='A' and chr<='Z')):
	if(chr=='a' or chr=='e' or chr=='i' or chr=='o' or chr=='u' or chr=='A' or chr=='E' or chr=='I' or chr=='O' or chr=='U'):
		print("Vowel")
	else:	 
		print("Consonant")
else:
	print('invalid')
