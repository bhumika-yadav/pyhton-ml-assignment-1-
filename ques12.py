a=int(input('enter a no'))
sum=0
while(a!=0):
    r=a%10
    sum=sum+r
    a=a//10

print('the sum of ', a ,'is ',sum )
