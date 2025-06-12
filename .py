vetor= []
vetor1=[]
for a in range (-1,1001):
    vetor.append(a)
for b in vetor:
    if b % 5==0:
        vetor1.append(b)
for c in vetor1:
    total=total+c
print(total)
