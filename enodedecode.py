def encode(strs):
    encoded=[]
    for word in strs:
        encoded.append(str(len(word))+"#"+word)
    return ''.join(encoded)

def decode(s):
    result=[]
    i=0
    while i<len(s):
        j=i
        while s[j].isdigit():
            j+=1

        length=int(s[i:j])
        start=j+1
        word=s[start:start+length]
        result.append(word)
        i=start+length
    return result
strs = ["neet", "code", "love", "you"]
cd=encode(strs)
print("Encoded:",cd)

dc=decode(cd)
print("Decoded:",dc)
