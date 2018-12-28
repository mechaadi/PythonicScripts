## adds <br/> html tags at every \n

filename = input("Enter file name with directory:  ")

f = open(filename, "r")	


char = ""
i = 0
for a in f:
	for ch in a:
		if(ch=='\n'):
			char += "<br/>"
		else:
			char += ch

print(char)		
