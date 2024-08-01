age = int(input("enter age "))
if age >= 16 and age <= 18:
    print('u can do parttime job')
elif age > 18 and age <= 65:
    print('u can do fulltime job')
else:
    print('berojgar')


s1 = int(input('enter sub1 marks : '))
s2 = int(input('enter sub2 marks : '))
s3 = int(input('enter sub3 marks : '))
s4 = int(input('enter sub4 marks : '))
s5 = int(input('enter sub5 marks : '))

per = (s1+s2+s3+s4+s5)/500*100
print(per)

if per < 0:
    print('wrong no of marks')
elif per <= 35:
    print('Fail')
elif per <= 40:
    print('pass class')
elif per <= 60:
    print('second class')
elif per <= 75:
    print('first class')
elif per <=100:
    print('distinction')
else:
    print('vrom vrom!!')