def find(combi):
	powerset={}#generates entire powerset
	ps={}#powerset excluding (repeated/null/single_letter) words
	noe=pow(2,len(combi))
	print('Total number of combination',noe)
	print('Total number of characters in the word',len(combi))
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
