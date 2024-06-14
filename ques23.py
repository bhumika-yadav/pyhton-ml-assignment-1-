# conversion of temperature

choice=input('enter ur choice')
if choice =='1':
    temp=int (input('enter your temperature in celcius'))
    f=((9/5)*temp)+32
    print ("the temperature is ",f)


if choice =='2':
    temp=int (input('enter your temperature in celcius'))
    c=((f-32)*5)/9
    print ("the temperature is ",c)
