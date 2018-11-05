n=1
d=0
while n!=0:
    n=int(input())
    sum=n
    while sum>=10:
        d+=(sum%10)
        sum//=10
    d+=sum
    while d>=10:
        d=d(d//10)+(d%10)
    if d!=0:
        print(d)
    d=0
            
    
