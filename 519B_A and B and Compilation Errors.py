n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
 
ans1=sum(a)-sum(b)
ans2=sum(b)-sum(c)
print(ans1)
print(ans2)
