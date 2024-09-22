main = []
main1 = []
anarr = []
def check(aa,ab,ac,ad):
    arr1, arr2 = [0,0,0,0], [0,0,0,0]
    if aa>ac: arr1[0]=1 
    else: arr2[0]=1 
    if aa>ad: arr1[1]=1
    else: arr2[1]=1 
    if ab>ac: arr1[2]=1 
    else: arr2[2]=1 
    if ab>ad: arr1[3]=1 
    else: arr2[3]=1 
    #sn, sl = arr1[0], arr2[0]
    #print(arr1, arr2)
    res = 0
    ans = 0
    sn, sl = 0, 0
    #1,1,0,1 
    #0,0,1,0
    for i in range(0,len(arr1)):
        #if sn!=sl and arr1[i]>arr2[i]: res+=1
        sn+=arr1[i]
        sl+=arr2[i]
        if sn!=sl and arr1[i]==1 and arr2[i]==0: ans+=1
        #print(sn, sl)
    if ans>=2:return 1 
    else: return 0

for _ in range(int(input())):
    a1, a2, b1, b2 = map(int, input().split())
    res = 0
    res+= check(a1,a2,b1,b2)
    res+= check(a2,a1,b1,b2)
    res+= check(a1,a2,b2,b1)
    res+= check(a2,a2,b2,b1)
    anarr.append(res)
print(anarr)
