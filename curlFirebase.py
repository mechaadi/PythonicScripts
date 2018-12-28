## adds newline, tab and " ", for curl operations on FIREBASE

filename = input("Enter file name with directory:  ")

f = open(filename, "r")	


char = ""
i = 0
for a in f:
	for ch in a:
		if(ch=='\n'):
			char += "\\"+"\\"+"n"
		elif(ch=='\t'):
			char += "\\"+"\\"+"t"
		elif(ch=="\""):
			char += ""+"\\"+"\\"+'\"'
		else:
			char += ch

print(char)		
