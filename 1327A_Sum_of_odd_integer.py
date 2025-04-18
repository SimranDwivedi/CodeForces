n=int(input())
for i in range(n):
    n1,n2=map(int,input().split())
    if n2>n1 or n2*n2>n1:
         print("NO")
    elif (n1%2==0 and n2%2==0 ) or (n1%2==1 and n2%2==1):
        print("YES")
    else:
        print("NO")
