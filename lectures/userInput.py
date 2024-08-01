a = input("Enter a number ")
print(type(a))

#Whenver we take inputy from user by default it is in string format
a=int(input('no1'))
b=int(input('no2'))
print(a+b)

a=int(input('no1'))
b=int(input('no2'))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#write a program which will take 5 subj marks from students and dispklay final percentage
a=int(input('subject1 '))
b=int(input('subject2 '))
c=int(input('subject3 '))
d=int(input('subject4 '))
e=int(input('subject5 '))
totalMarks = a+b+c+d+e
perc = totalMarks/5
print('Final percentage is : ',perc)