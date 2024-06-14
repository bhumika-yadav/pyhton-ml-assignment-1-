#calculator

choice=input('enter ur choice betwwn 1,2,3,4')
if choice =='1':
    a=int(input('enter a no'))
    b=int(input('enter a no'))
    print('the sum is: ',a+b)

if choice =='2':
    a=int(input('enter a no'))
    b=int(input('enter a no'))
    print('the difference is: ',a-b)

if choice =='3':
    a=int(input('enter a no'))
    b=int(input('enter a no'))
    print('the multiplication is: ',a*b)

if choice =='4':
    a=int(input('enter a no'))
    b=int(input('enter a no'))
    print('the division is: ',a/b)

else:
    print('invalid choice')
