# fibbonacci series

n=int(input('how long u want the series'))
n1=0
n2=1
print(n1,n2 ,end =" ")

for i in range(n):
    n3=(n1+n2)
    print(n3,end =" ")
    n1=n2
    n2=n3
