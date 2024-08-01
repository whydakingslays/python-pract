i = int(input('enter ur number '))
if i > 10:
    i = int(input('enter a num less than 10'))
else:
    a = 0
    while a < 10:
     a = a+1
     print(i, 'x', a, '=', i*a)

a = int(input("enter no : #"))
for i in range(1, 11):
   print(a, "x", i, "=", a*i)
i = 0
while i < 11:
   print(a, "x", i, "=", a*i)
   i=i+1
  

user = int(input("enter a no : "))
if(user <= 10 and user >= 0):
   for i in range (1,11):
    print(user,"x",i,"=",user*i)
  
else:
  print("enter nu again bten 1-10")    