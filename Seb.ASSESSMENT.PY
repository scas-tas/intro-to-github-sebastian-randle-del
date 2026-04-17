"""coffee shop"""
reg = ["TIM", "TOM", "TAM", "MAOFN", "ZAVONE", "ALICE", "JEDD", "ROBERT"]
menu = ["COFFEE","MUFFIN","BANNANA BREAD","PASTRY","TEA","SALTED CARAMEL LATTE","CAPPUCCINO"]
menu = ["COFFEE","MUFFIN","BANANA BREAD","PASTRY","TEA","SALTED CARAMEL LATTE","CAPPUCCINO"]
menu_prices = {"COFFEE":6.50,  "MUFFIN": 3.00,  "BANANA BREAD":6.00,  "PASTRIES":5.00,  "TEA":9.00,  "SALTED CARAMEL LATTES":12.50,  "CAPPUCCINO":5.50}

entire_orde = {}      #dictionarie

parts_orde ={}

price_orde = 0

def too_quiet(yell):
  if yell.islower():
   print("I DIDN'T HEAR YOUR ORDER!")
   exit()
  elif yell.isupper():
   pass
  else:
   print("I CAN'T UNDERSTAND YOU!")
   exit()

def amount_orde(num):    #amount being ordered
      if num == 0: 
         return ('WHATS THE POINT OF ORDERING NOTHING?!')
      elif num < 0: 
         return ("OK WHERE'S MY ORDER THAN?!")
      elif 1 < num < 50:     #the normal response
         return (num)
      else:
         return ('YOU ORDERING FOR AN ENTIRE TOWN OR SOMETHING?!')

def loop_orde(lop):      #loops the code 
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

print("CURRENTLY WE ARE SELLING:\n \n       --COFFEES--\n       --MUFFINS--\n     --BANANA BREAD--\n       --PASTRIES--\n         --TEA--\n--SALTED CARAMEL LATTES--\n     --CAPPUCCINO-- \n")

orde = input('WHAT WOULD YOU LIKE TO ORDER?! ')
loud = too_quiet(orde)

if orde in menu:
 amount = int(input("HOW MANY WOULD YOU LIKE?! "))
 if 1 <= amount < 50:
   nam = input('NAME?! ')
   loud = too_quiet(nam)

   parts_orde["items"] = orde
   parts_orde["amount"] = amount

   entire_orde[amount] = orde

   total_price = menu_prices[orde] * amount
   price_orde += total_price

   if amount > 1:
      mult = "'s"
   else:
      mult = ""
      if nam in reg:
        print("YOU HAVE A 15% DISCOUNT FOR BEING A REGULAR CUSTOMER!")
        
        again = input("IS THAT ALL?! ")
        loud = too_quiet(again)
        if again == "NO":
          repe = loop_orde(again)
          print(F'order for {nam}:') 
          for amount, orde in entire_orde.items():
            print(f'{amount} {orde}{mult}')
          
          price_orde = price_orde * 0.85
          print(f'THAT WILL COST:${price_orde}')

        
        elif again == "YES":
          print(F'order for {nam}:') 
          for amount, orde in entire_orde.items():
            print(f'{amount} {orde}{mult}')

          price_orde = price_orde * 0.85
          print(f'THAT WILL COST: ${price_orde}')

      else:
        again = input("IS THAT ALL?! ")
        loud = too_quiet(again)
        if again == "NO":
          repe = loop_orde(again)
          print(F'order for {nam}:') 
          for amount, orde in entire_orde.items():
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
else: 
  print(f'DID YOU HEAR ME SAY {orde} WAS ON THE MENU?!')
