flag = "112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 98 56 100 55 50 55 49 102 125"
flag_new  = flag.split(' ')
decoded_txt = ""
for i in flag_new:
#	print(type(i))
	decoded_txt += chr(int(i))
	#print(decoded_txt)
print(decoded_txt)
