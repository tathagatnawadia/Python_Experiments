#This is a program which can generate all sensible words from a combination of letters ... 
#THe input which has to be provided in this code are ====== 

#
#1.A sorted dictionary .txt file ... comes from the rooot folder

#
#2.A group of letters no matter where they are placed we would find all the combination(OOPS!! have to figures out alogorithm)
import subprocess #Mainly used in the case of doing command prompt or a terminal behaviour
import sys
import re
global guess
guess=[]
def find(combi):
	powerset={}#generates entire powerset
	ps={}#powerset excluding (repeated/null/single_letter) words
	noe=pow(2,len(combi))
	i=0
	k=0
	for i in range(noe):
		j=0
		s=''
		for j in range(len(combi)+1):
			if (i&(1<<j)):
				s=s+combi[j]
		powerset[k]=s
		k=k+1
	#The powerset is generated  now !!
	i=0
	j=0
	for i in range(len(powerset)):
		if len(powerset[i]) == 0:
			del(powerset[i])#This deletes the 0 length elements e.g.''
			continue
		if len(powerset[i]) == 1:
			del(powerset[i])#This deletes the 1 length elements e.g.'a','l','m'
		else:
			if powerset[i] in ps.values():#Removes duplicate entries in case of repeated letter e.g.'cool'
				continue
			ps[j]=powerset[i]#This edits the list and makes it free from 0 and 1 length elements
			j=j+1
	#The ps is generated now !!
	print(sorted(ps.values(),key=len))
	print('The total number of smart permutations',len(ps),':: Accuracy =',(len(ps)/noe))
	print('The process has stopped now and has returned an "unordered" list')
	return ps
	#This is the best possible code which works
#______________________________________________________________________________________________________________________________________________________________
def convertlist(str):#This funtion seperates the strings entered into an ordered list e.g. b=['h','e','l','l','o']
    k=0
    b=[]
    for k in range(len(str)):
        b.append(str[k])
    return b
#______________________________________________________________________________________________________________________________________________________________

def getmatches(filename,combi):
    f=open(filename, 'r')
    i=0
    j=0
    conf=0 #This is a confirmation flag : 1-The permutation has a succesfull combination in the dictionry // 0-No combination present
    for s in f:#This sends the a "single word" from the dictionary and sends it for processing
        combi=combi.lower()#changes the available words to lowercase for the purpose of matching
        s=s.lower()#changes dictionary to lowercase for the purpose of matching
        if len(s)==(len(combi)+1):#Compares the length of available words with that of the dictionary
            temp=convertlist(s)#converts the string into a list
            j=0
            conf=0
            temp.pop(-1)#removes \n character
            for j in range(len(combi)):#runs a comparity test on the "single word" from the dictionary
                if combi[j] in temp:#if the comparity test of the letter in the "single word" from the dictionary is true POP that letter from the "single word"
                    conf=1
                    k=0
                    for k in range(len(temp)):
                        if combi[j] == temp[k]:
                            temp.pop(k)#Pops the letter from the "single word"
                            break
                else:
                    conf=0
                    break  #if the letter is not present in the "single word" from the dictionary .. it breaks out of the loop
        if conf == 1:#if the permutation satisfies all conditions
            if s in guess:
                continue
            guess.append(s)#Put the "single word" in the solution list guess
            print(s)
            print(guess)
            conf=0
#________________________________________________________________________________________________________________________________________________________________
            
def main():
    matches=find(sys.argv[2])
    print(len(matches))
    k=0
    for k in range(len(matches)):
        print('For the combination',matches[k],'sensible words are ')
        getmatches(sys.argv[1],matches[k])
    print('Your combinations are : ')
    print(sorted(guess,key=len,reverse=True))
    

if __name__ == '__main__':
    main()
    