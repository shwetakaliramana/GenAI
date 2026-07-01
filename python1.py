n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    isprime=True
    if i<2:
        isprime=False
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            isprime=False
            break
    if isprime:
        sum+=i
        print(i,"+",end=" ")
print("=", sum)

