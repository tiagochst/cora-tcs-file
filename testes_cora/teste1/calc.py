from numpy import*

x0 = []
rate=[]
oldCount=-1
oldRate=0
for line in file('data.txt'):
	copy = line	
	line = line.split()
	if(line):
		if(line[0]=='T'):
			print line[11]
			print line[1]
			if(oldCount!=line[11] or oldRate!=line[1]):
				oldCount= line[11]
				oldRate= line[1]
	 			x0.append(copy)
	 			rate.append(line[11])


f = open('teste', 'w')
fCora = open('coraPlot', 'w')
for i in range(len(x0)):
	f.write(x0[i])
	fCora.write(str(i)+" "+ rate[i] +"\n")
