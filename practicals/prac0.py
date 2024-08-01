import cmath

a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
c = int(input('Enter c value: '))


discriminant = b**2 - 4*a*c

eqn1 = (-b + cmath.sqrt(discriminant)) / (2*a)
eqn2 = (-b - cmath.sqrt(discriminant)) / (2*a)

print('First equation is {0} and Second equation {1} : '.format(eqn1,eqn2))
