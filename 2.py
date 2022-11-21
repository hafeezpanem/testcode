def stringc(str1,str2):
    t=str2[-1]
    count=0
    for i in str1:
        if i==t:
            count+=1
    return count
str1=input()
str2=input()
print(stringc(str1,str2))
