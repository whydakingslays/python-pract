num = float (input('enter a num = '))
if num >= 0:
    if num == 0:
        print('Zero')
    else:
        print('positive num')
else:
    print('neg')
    
choice = int(input('Enter your choice: '))

if choice == 1:
    budget = int(input('Enter your budget amount: '))

    if budget >= 20000 and budget <= 30000:
        print('You can buy Vivo, Xiaomi, Oppo')
    elif budget >= 30001 and budget <= 50000:
        print('You can buy OnePlus, iQOO')
    elif budget >= 50001 and budget <= 70000:
        print('You can buy Samsung')
    elif budget >= 70001 and budget <= 100000:
        print('You can buy iPhone')
    else:
        print('No phones in your budget')
elif choice == 2:
    budget = int(input('enter your budget amount: '))
    if budget >= 25000 and budget <= 30000:
     print('You can buy Chromebook')
    elif budget >= 30001 and budget <= 50000:
        print('You can buy Acer,Lenovo')
    elif budget >= 50001 and budget <= 70000:
        print('You can buy Dell, Asus,Hp')
    elif budget >= 70001 and budget <= 100000:
        print('You can buy MacBook')
    else :
        print('No laptops in your budget')
else:
    print('Not a valid choice between 1 and 2')
    
choice = input('Chose between b,l,d : ')
if choice == 'B' or choice == 'b':
   bChoice = input('N.I or S.I : ')
   if bChoice == 'N.I':
      menu = input('Idli or Dosa : ')
      if menu == 'Idli' or menu =='idli':
         print('You ordered Idli!')
      elif menu == 'Dosa' or menu == 'dosa':
         print('You ordered Dosa!')
      else:
         print('Not in menu!!!')
   elif bChoice == 'S.I':
        menu = input('Vada or Puri : ')
        if menu == 'Vada' or menu == 'vada':
           print('You ordered Vada!')
        elif menu == 'Puri' or menu == 'puri':
           print('You ordered Puri!')
        else:
           print('Not in menu!!!')
   else:
      print(bChoice,'is not in menu!!!')
elif choice == 'L' or choice == 'l':
   lMenu = input('chose between Pizza or Burger : ')
   if lMenu == 'Pizza' or lMenu == 'pizza':
    Pmenu = input('Choose between Cheese or Pepperoni : ')
    if Pmenu == 'Cheese' or Pmenu == 'cheese':
       print('You ordered Cheese Pizza!')
    elif Pmenu == 'Pepperoni' or Pmenu == 'pepperoni':
       print('You ordered Pepperoni pizza!')
    else:
       print(Pmenu,'is not in menu!!!')
   elif lMenu == 'Burger' or lMenu == 'burger':
    Bmenu = input('Choose between Chicken or Beef : ')
    if Bmenu == 'Chicken' or Bmenu == 'chicken':
      print('You ordered Chicken Burger!')
    elif Bmenu == 'Beef' or Bmenu == 'beef':
       print('You ordered Beef Burger!')
    else:
       print(Bmenu,'is not in menu!!!')
   else:
      print(lMenu,'is not in menu!!!')
elif choice == 'd' or choice == 'D':
   dMenu = input('Chooze between Veg or Non-Veg : ')
   if dMenu == 'Veg' or dMenu == 'veg':
      print('RAAAHHHH!!!🦅🦅🇦🇺')
      print('no vegans allowed!!!')
   elif dMenu == 'Non-veg' or dMenu == 'non-veg':
      nonvgMenu = input('Choosr between Steak or Pork: ')
      if nonvgMenu == 'Steak' or nonvgMenu == 'steak':
         print('You ordered Steak!')
      elif nonvgMenu == 'Pork' or nonvgMenu == 'pork':
         print('You ordered Pork!')
      else:
         print(nonvgMenu,'is not in menu!!!')
   else:
      print(dMenu,'is not in menu!!!')
else:
   print(choice,'is not a valid choice!!!')    