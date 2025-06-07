"""
Project: Shopping List App
Author: Ryan Younger
Environment: Coded in Ed 1.14 on Amiga Workbench 1.3
Year: 2025
"""

import os
import random

shoppinglist = []
randomlist = ['marzipan', 'tuna', 'ciabatta', 'yoghurt', 'weetabix', 'tea', 'floppy disks']


def clear():
   os.system('cls' if os.name == 'nt' else 'clear')


def main():
   clear()
   print('------Shopper 1.0.1------')
   input('Press Enter to start your list')
   shopper()


def shopper():

   while True:
      clear()
      userinput = input('Commands: add , del , list, quit:  ').strip().lower()

      if userinput == 'add':
         addfunction()

      elif userinput == 'list':
         listfunction()

      elif userinput == 'del':
         delfunction()

      elif userinput == 'quit':
         break

      else:
         print('Command not recognised')


def delfunction():

   if not shoppinglist:
      print('No items in list!')
      input('Press Enter to continue')
      return
   
   else:
      print(shoppinglist)
      delitem = input('Delete which item?')

      try:
         shoppinglist.remove(delitem)
         print(delitem + ' removed!')
         print(shoppinglist)
         input('Press Enter to continue')

      except ValueError:
         print('Item not found')
         input('Press Enter to continue')


def addfunction():

   while True:
      print('Choose an item to add:')
      print('1.milk \n2.butter \n3.cheese \n4.custom \n5.random \n6.mainmenu')
      addchoice=input().strip().lower()

      if addchoice == '1':
         shoppinglist.append('milk')
         clear()
         print(shoppinglist)

      elif addchoice == '2':
         shoppinglist.append('butter')
         clear()
         print(shoppinglist)

      elif addchoice == '3':
         shoppinglist.append('cheese')
         clear()
         print(shoppinglist)

      elif addchoice == '4':
         customitem = input('Enter your custom item: ').strip().lower()
         shoppinglist.append(customitem)
         clear()
         print(shoppinglist)

      elif addchoice == '5':
         randomitem = random.choice(randomlist)
         shoppinglist.append(randomitem)
         clear()
         print('Random shopping item added!')
         print(shoppinglist)

      elif addchoice == '6':
         break

      else:
         clear()
         print('Please choose an option between 1 and 6!')


def listfunction():

   clear()

   if not shoppinglist:
      print('No items in list!')
      input('Press Enter to continue')
      return

   for listitem in shoppinglist:
      print ('[ ] ' + listitem)

   markcompleted = input('mark an item as purchased? (y/n): ').strip().lower()
      
   if markcompleted == 'n':

      return

   else:

      item_to_complete = input('Which item?').strip().lower()

      if item_to_complete in shoppinglist:
            print (item_to_complete + ' Has been purchased!')
            shoppinglist.remove(item_to_complete)
            input('Press Enter to continue')


      else:

         print ('Could not find item in list, please check spelling')
         input('Press Enter to continue')

main()

      

   
