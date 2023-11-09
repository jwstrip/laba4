
n=int(input())
while(n<100000 or n>999999):

    n=int(input())

m=int(input())
while(m>999999 or m<n):

    m=int(input())
cnt=0
for i in range(n,m+1):
    a=int(i/1000)
    b=i%1000
    s1=0
    s2=0
    for g in range(1,3):
        s1+=a%10
        a=int(a/10)
    for g in range(1,3):
        s2+=a%10
        b=int(b/10)
    if(s1==s2):
        cnt+=1
print(f"{cnt}")
