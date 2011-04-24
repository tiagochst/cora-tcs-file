from numpy import*

x0 = []
rate=[]
oldCount=-1
oldRate=0
for line in file('data.txt'):
	copy = line	
	line = line.split()
	if(line):
		if(line[0]=='T' or line[0]=='Ttp' or line[0]=='T p'):
			print line[7]
			print line[0]
			if(oldCount!=line[10] or oldRate!=line[1]):
				oldCount= line[10]
				oldRate= line[1]
	 			x0.append(copy)
	 			rate.append(line[1])


f = open('teste', 'w')
fCora = open('minstrelPlot', 'w')
for i in range(len(x0)):
	f.write(x0[i])
	fCora.write(str(i)+" "+ rate[i] +"\n")
