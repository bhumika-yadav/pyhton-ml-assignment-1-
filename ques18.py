# if two strings are anagram

a=input('enter a string')
b=input('enter a string')
if sorted(a)==sorted(b):
    print('anagram')

else:
    print(' not anagram')
