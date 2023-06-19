def Sumofelements(n,nos):
    s=0
    for i in nos:
        if i%2==0:
            s+=i
    print(s)

n=int(input())
nos=list(map(int,input().split()))
Sumofelements(n,nos)
