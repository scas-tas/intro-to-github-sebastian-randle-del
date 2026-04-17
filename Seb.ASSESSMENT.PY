"""coffee shop"""
reg = ["TIM", "TOM", "TAM", "MAOFN", "ZAVONE", "ALICE", "JEDD", "ROBERT"]                         #lists
menu = ["COFFEE","MUFFIN","BANNANA BREAD","PASTRY","TEA","SALTED CARAMEL LATTE","CAPPUCCINO"]
menu = ["COFFEE","MUFFIN","BANANA BREAD","PASTRY","TEA","SALTED CARAMEL LATTE","CAPPUCCINO"]
menu_prices = {"COFFEE":6.50,  "MUFFIN": 3.00,  "BANANA BREAD":6.00,  "PASTRIES":5.00,  "TEA":9.00,  "SALTED CARAMEL LATTES":12.50,  "CAPPUCCINO":5.50}

entire_orde = {}      #dictionaries

parts_orde ={}

price_orde = 0

def too_quiet(yell):       #pretty useful as it is the main feature of the original program, it turned out to be easier than i thought
  if yell.islower():
   print("I DIDN'T HEAR YOUR ORDER!")
   exit()
  elif yell.isupper():
   pass
  else:
   print("I CAN'T UNDERSTAND YOU!")
   exit()

def amount_orde(num):    #amount being ordered : i wanted some fun and interesting responses if you requested strange or pointless things
      if num == 0: 
         return ('WHATS THE POINT OF ORDERING NOTHING?!')   
      elif num < 0: 
         return ("OK WHERE'S MY ORDER THAN?!")
      elif 1 < num < 50:     #the normal response
         return (num)
      else:
         return ('YOU ORDERING FOR AN ENTIRE TOWN OR SOMETHING?!')

def loop_orde(lop):      #loops the code may not be incredibly neccesary but its a little too far in to turn back
   if lop == "NO":
       orde = input('WHAT ELSE WOULD YOU LIKE TO ORDER?! ')
       global price_orde
       loud = too_quiet(orde)
       if orde in menu:
           amount = int(input("HOW MANY WOULD YOU LIKE?! "))
           if 1< amount < 50:
               parts_orde["items"] = orde
               parts_orde["amount"] = amount
               entire_orde[amount] = orde
               total_price = menu_prices[orde] * amount
               price_orde += total_price
               again = input("IS THAT ALL?! ")
               loud = too_quiet(again)
               if again == "NO":
                   repe = loop_orde(again)
               elif again == "YES": 
                pass
           else:
               ting = amount_orde(amount)
               print (ting)
       else: 
         print(f'DID YOU HEAR ME SAY {orde} WAS ON THE MENU?!')
  
#__________________Mainline_______________________________________

#I have added spaces to the menu to make everything line up nicely so its easier to see the entire thing
print("CURRENTLY WE ARE SELLING:\n \n       --COFFEES--\n       --MUFFINS--\n     --BANANA BREAD--\n       --PASTRIES--\n         --TEA--\n--SALTED CARAMEL LATTES--\n     --CAPPUCCINO-- \n")

orde = input('WHAT WOULD YOU LIKE TO ORDER?! ')
loud = too_quiet(orde)

if orde in menu:   #this is another instance of wanting interesting interactions depending on what you ask for
 amount = int(input("HOW MANY WOULD YOU LIKE?! "))
 if 1 <= amount < 50:
   nam = input('NAME?! ')
   loud = too_quiet(nam)        #this is the def  at play if they don't shout their requests it will end the code

   parts_orde["items"] = orde
   parts_orde["amount"] = amount                    #this bit here also feels pointless and unessasary but changeing it could take awhile
  
   entire_orde[amount] = orde

   total_price = menu_prices[orde] * amount        #adds the price of what was ordered together
   price_orde += total_price

   if amount > 1:
      mult = "'s"
   else:                                         #this was so it sounds gramatically correct
      mult = ""
      if nam in reg:
        print("YOU HAVE A 15% DISCOUNT FOR BEING A REGULAR CUSTOMER!")     #actual discount on items
        
        again = input("IS THAT ALL?! ")
        loud = too_quiet(again)
        if again == "NO":
          repe = loop_orde(again)
          print(F'order for {nam}:') 
          for amount, orde in entire_orde.items():
            print(f'{amount} {orde}{mult}')                 #this is a loop so each item in the order is on a different line 
          
          price_orde = price_orde * 0.85                    #this is the 15% discount
          print(f'THAT WILL COST:${price_orde}')

        
        elif again == "YES":
          print(F'order for {nam}:') 
          for amount, orde in entire_orde.items():         #same as before except ordered only one item
            print(f'{amount} {orde}{mult}')

          price_orde = price_orde * 0.85
          print(f'THAT WILL COST: ${price_orde}')

      else:
        again = input("IS THAT ALL?! ")
        loud = too_quiet(again)
        if again == "NO":
          repe = loop_orde(again)
          print(F'order for {nam}:') 
          for amount, orde in entire_orde.items():        # just like the other two but without the discount
            print(f'{amount} {orde}{mult}')
          print(f'THAT WILL COST: ${price_orde}')

        elif again == "YES":
          print(F'order for {nam}:') 
          for amount, orde in entire_orde.items():
            print(f'{amount} {orde}{mult}')
            print(f'THAT WILL COST: ${price_orde}')
 else:
    ting = amount_orde(amount)
    print (ting)
else:                                                        #the interesting resposes i mentioned before
  print(f'DID YOU HEAR ME SAY {orde} WAS ON THE MENU?!')
