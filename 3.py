def validnumber(n):
    validlist=[1,2,5,6,8,9]
    if n-1 < len(validlist) :
        return validlist[n-1]
    n=n-len(validlist)
    str1=9
    while n >1:
        str1=str1+1
        s=str(str1)
        for i in s:
            if int(i) not in validlist:
                break
        else:
            n=n-1
            
    return str1       
n=int(input())
print(validnumber(n))
