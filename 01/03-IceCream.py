import random

randomList = list(random.choice(range(4,28)) for n in [None]*100) 

evensAndOdds = [[n for n in randomList if n%2==0],[n for n in randomList if n%2==1]]

#print randomList[0:100]
#print evensAndOdds[0:100]
#print len(randomList)
#print len(evensAndOdds[0])
#print len(evensAndOdds[1])
