a=list(map(int,input().split()))
a.sort
l=0
r=len(a)-1
target=int(input("Enter the target sum:"))
answer=False

while l<r:
    current=a[l]+a[r]
    if current==target:
        answer=True
        break  
    elif current<target:
        l+=1
    else:
        r-=1
