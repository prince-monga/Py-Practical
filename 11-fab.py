n=int(input("Enter Number of terms: "))

a,b=0,1
if n<=0:
    for i in range(n):
        print(a,end=" ")
        nth=a-b
        a=b
        b=nth    
elif n==1:
    print(" ",a," ")    
else:
    for i in range(n):
        print(a,end=" ")
        nth=a+b
        a=b
        b=nth