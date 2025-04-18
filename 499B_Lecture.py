n,m=map(int,input().split())
arr=[]
for i in range(m):
    n1,n2=input().split() 
    arr.append(n1)
    arr.append(n2)
 
ans_s=input().split()
d={}
for i in range(0,len(arr)-1):
    d[arr[i]]=arr[i+1]
ans=[]
for i in ans_s:
    p=d[i]
    q=len(i)
    if len(p)<q:
        ans.append(d[i])
    else:
        ans.append(i)
print(' '.join(ans))
