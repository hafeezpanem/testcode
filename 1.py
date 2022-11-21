def based3(n):
    l=[]
    while(n!=0):
        r=n%3
        n=n//3
        l.append(r)
    return ("".join(map(str,l)))
n=int(input())
t=based3(n)
print(t)
    
    
