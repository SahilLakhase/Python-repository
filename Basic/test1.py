n=int(input("Enter any NO:"))
sum=0
while n>0:
    b=n%10
    print(b)
    n=n//10
    sum=sum+b
    print("addition is",sum)