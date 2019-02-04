rank = [1,2,3,4,5,6,7,8,9,10,11,12,13]
suite = ["H","S","D","C"]

cards = list(zip(rank,suite))	#Populate the card list

cards = []
for ranks in rank:
	cards = cards + [(ranks,suite[0]) , (ranks,suite[1]),ranks,suite[2])]

