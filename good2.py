a = []
with open('C:/Users/Also_Lenovo/Desktop/reviews.txt', 'r') as txt:
	for t in txt:
		a.append(t.strip())

good = []
for good2 in a: 
	if 'good' in good2:
		good.append(good2)
print("It have", len(good), "message with good!")

bad = [good2 for good2 in a if 'bad' in good2]

print("It have", len(bad), "message with bad!")