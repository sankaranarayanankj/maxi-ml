x=list(input())
l=[]
for i in x:
    if(i not in l):
        l.append(i)
print(len(l))