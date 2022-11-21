n=int(input('enter the number of rows: '))
m=int(input('enter the number of columns : '))

l=[]
for i in range(n):
    t=[]
    for j in range(m):
        t.append(int(input()))
    l.append(t)

topp=0

bottomm=len(l)-1

righ=len(l[0])-1
lef=0


for i in range(len(l)//2):
    if 0 not in l[i]:
        topp=topp+1
    if 0 not in l[len(l)-1-i]:
        bottomm=bottomm-1
        
for i in range(len(l)//2):
    k=[]
    m=[]
    for j in range(len(l)//2):
         k.append(l[j][i])
         m.append(l[len(l)-1-j][i])
    if 0 not  in k:
        lef=lef+1
    if 0 not in m:
        righ=righ-1
        
        
print((top,left),(top,right),(bottom,left),(bottom,right),sep=',')
