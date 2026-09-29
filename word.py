st=input().strip()

freq={}
for ch in st:
    freq[ch]=freq.get(ch,0)+1
s=-1

for ch in st:
    if freq[ch]==1:
        s=ch
        break

print(s) 