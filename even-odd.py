a=int(input("Enter a number: "))
sum=0
multiply=1
for i in range(1,a+1):
    if i%2!=0:
        sum+=i
        print(i,"+",end=" ")
        print("=",sum)
    else:
        multiply*=i
        print(i,"*",end=" ")
        print("=",multiply)