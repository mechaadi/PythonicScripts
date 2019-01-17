import urllib.request
import time
import sys
import subprocess
import shlex
import pycurl, json


title = ''
desc = ''
counter = 0
sendTitle = ''
sendDesc = ''
link = ''
ti, de = '', ''
titlelist, desclist = [""], [""]
tiC, deC = 0, 0
newTitle = ''
counting = 1
videoList = open("/home/mechaadi/Desktop/Desktop/dataStructs.txt", 'r')

for x in videoList:
	f = open("youtube.txt", 'w')	
	link = x
	with urllib.request.urlopen(x) as url:
	    s = url.read()
	    
	  
	strr = s.decode() 
	#link = strr
	newstrr=''
	li, lit = [""], [""]
	liWord = [""]
	chh=''
	f.write(strr)
	count = 0
	found = 0
	index = 0
	i,i1,i2 = 0,0,0
	s = ''
	count1 = 0
	found1 = 0
	countLit = 0
	c=0
	c1=0

	count1, found1 = 0, 0
	reading = open("youtube.txt", 'r')

	for words in reading:
		for ch in words:
			newstrr = ch
			li.append(newstrr)		

	while i < 8000:
		lit.append(li[i])
		i+=1		


	for x in lit:
		s = s + x


	for s in lit:
		c = c+1
		if(s=='<'):
			if(lit[c]=='t'):
				break
		

	c = c+5		

	while i1 < 12000 :
		title = title + lit[c]
		c = c+1
		if(lit[c]=='>'):
			c = c+1
			title = title + lit[c]
			break

	c = 0

	for s in lit:
		c = c+1
		if (s=='d'):
			if (lit[c]=='e'):
				if (lit[c+1]=='s'):
					break

	c = c+21
	while i2 < 12000:
		desc = desc + lit[c]
		c = c + 1
		if (lit[c]=='>'):
			break

	#print("title is ", title, '\n')
	#print("desc is ", desc, '\n\n\n')


	for t in title:
		if(t=='<'):
			t = ''
			if (t=='t'):
				t = ''
		elif(t=='>'):
			t = ''
		elif(t=='/'):
			t = ''
		else:
			ti = ti + t

	for t in desc:
		if(t=='"'):
			t = ''
			if (t=='t'):
				t = ''
		elif(t=='>'):
			t = ''
		else:
			de = de + t	

	for x in ti:
		titlelist.append(x)

	for x in de:
		desclist.append(x)



	#print("size of titleLitst" ,len(titlelist))

	size = len(titlelist)
	while(counter<size):
		if (titlelist[counter]=='t'):
			if(titlelist[counter+1]=='i'):
				if (titlelist[counter+2]=='t'):
					if (titlelist[counter+3]=='l'):
						titlelist[counter]=''
						titlelist[counter+1]=''
						titlelist[counter+2]=''
						titlelist[counter+3]=''
						titlelist[counter+4]=''

		counter = counter + 1

	
	for x in titlelist:
		newTitle = newTitle + x
	
	print("newTitle is ", newTitle)

	uri = 'https://path/'+str(counting)+'.json?auth=youtAuthKey'

	postmark_url = uri

	data = json.dumps({"title": str(counting)+". "+newTitle, "key": str(counting), "desc": de, "link":link, "duration":"less than 10 mins", "thumb":"https://firebasestorage.googleapis.com/v0/b/fir-2-83e2c.appspot.com/o/codey.png?alt=media&token=0c19d553-a996-4dd8-99f6-ac9dabcd53f2"})

	c = pycurl.Curl()       
	c.setopt(pycurl.URL, postmark_url)
	c.setopt(pycurl.CUSTOMREQUEST, "PUT")
	c.setopt(pycurl.POSTFIELDS,data)        
	c.perform()
	c.close()

	outfile = open("outfile.txt", 'a')
	outfile.write(title)
	outfile.write('\n')
	outfile.write(desc)
	outfile.write('\n')
	counting = counting + 1

	title = ''
	desc = ''
	ti = ''
	de = ''
	newTitle = ''
	titlelist.clear()
	counter = 0

	#titlelist.remove()
