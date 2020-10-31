list= list(map(int,input().split()))
numbers=[]
for i in list:
    if i >=0:
        numbers.append(i)
numbers.sort()
print(*numbers,end=' ')