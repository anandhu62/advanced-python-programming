n=int(input())
a=list(map(int,input().split()))
freq={}
for x in a:
    freq[x]=freq.get(x,0)+1
answer=-1
for x in a:
    if freq[x]==1:
        answer=x
        break   
print(answer)