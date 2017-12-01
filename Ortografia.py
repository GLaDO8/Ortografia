import collections #for finding the count of each item in the list.
import re #for using multiple delimeters in the split function.
import string #for using delimeters which can't be used in the split function.

#Dictionary based implementation

print("\033[1;37;40m   \n")
print("\n\t\t\tWelcome to Ortografia.")
print("  Our program will suggest you correct spellings for your mistakes")

d={}
word=open("words.txt", "r+")

for i in word.readlines():
	x=i[0].lower()
	# if will first check for the existence of a key and then append.
	if x in d.keys():
		d[x].append(i.strip("\r\n"))
		
	# else will add it directly.
	else:
		d[x]=[i.strip(" \r\n")]
word.close()
#creation of a list with all the words from the text given by the user.

filename=raw_input("\nEnter the complete file path (drag the text file into the terminal) : ")
spelfile=open(filename, "r")
x=spelfile.readlines()
s=''
for i in x:
	i.strip("\n")
	s+=i

#replacing some delimeters which can't be recognized by the re library.
#TOKENIZATION
new_str=string.replace(s,'?',':')
new_str1=string.replace(new_str,'? ',':')
new_str2=string.replace(new_str1,'.',':')
new_str3=string.replace(new_str2,'. ',':')
new_str4=string.replace(new_str3,': ',':')
s
wordlist=re.split(":|, |,|!|! |; | |: |;",new_str4)
print wordlist

for i in range(len(wordlist)):
	wordlist[i]=wordlist[i].strip()
	wordlist[i]=wordlist[i].lower()

#creation of a list of all wrong words

wrongwords=[]
correct=[]

#creates list of correct words

for i in wordlist:
	if i[0] in d.keys():
		j=i[0]
		for k in range(len(d[j])):
			if d[j][k]==i:	
				correct.append(i)

#counter checks and creates list of wrong words

for i in wordlist:
	if i not in correct:
		wrongwords.append(i)
print("The wrong words in the given file input are  ")

#Code to remove wrong spellings repeated more than 5 times.

count=collections.Counter(wrongwords)
for i in wrongwords: 
	if count[i]>=5:
		while (i in wrongwords): 
			wrongwords.remove(i)


def spellcheckcode():
	count2=0
	tt=[]
	qq=[]
	for i in wrongwords:
			
			#this code will insert every alphabet between every letter of the word and check it with the dictionary.
			w=0
			print ("\n\nCorrect spelling for "+i+" is/are: "),
			for l in range(len(i)+1):
				x=97
				while (x<123):
					a=list(i)
					a.insert(w,chr(x))
					sample="".join(a)
					for r in range(len(d[sample[0]])):
						if sample==d[sample[0]][r]:
							tt.append(sample)
							count2+=1
					x+=1
				w+=1
							
			#This code will replace every letter of the word and then check it with dictionary.
			pos=0
			for l in range(len(i)):
				x=97
				while(x<123):				
					qwerty = i[:pos] + chr(x)+ i[(pos+1):]
					for r in range(len(d[qwerty[0]])):
						if qwerty==d[qwerty[0]][r]:
							tt.append(qwerty)
							count2+=1
					x+=1
				pos+=1
            
            #This code will swap every pair of adjacent letters and then check it with the dictionary.
			for j in range(len(i)-1):
				k=list(i)
				k[j],k[j+1]=k[j+1],k[j]
				sad="".join(k)
				for r in range(len(d[sad[0]])):
					if sad==d[sad[0]][r]:
						tt.append(sad)
						count2+=1
			sad=''	

			#This code will remove every letter of the word and check it with the dictionary.
			k=0
			for j in i:
				q=i[:k] +i[(k+1):]
				k+=1
				for r in range(len(d[q[0]])):
					if q==d[q[0]][r]:
						tt.append(q)
						count2+=1
			print
			
			if count2==0:
				print(":( |NO SUGGESTIONS AVAILABLE| :( ")	
			
			else:
				for i in tt:
					if i not in qq:
						qq.append(i)
				for i in qq:
					print i+",",
			tt=[]
			qq=[]
			count2=0

spellcheckcode()
print("\n\n\t\t\tThank you for using ortografia !!\n")			

				


		
