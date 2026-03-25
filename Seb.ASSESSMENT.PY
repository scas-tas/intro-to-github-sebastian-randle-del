"""coffee shop"""

reg = ["TIM", "TOM", "TAM", "MAOFN", "ZAVONE", "ALICE", "JEDD", "ROBERT"]
menu = ["COFFEE","MUFFIN","BANNANA BREAD","PASTRY","TEA","SALTED CARAMEL LATTE","CAPPUCCINO"]

entire_orde = {}

def amount_orde(num):
      if num == 0: 
         return ('WHATS THE POINT OF ORDERING NOTHING?!')
      elif num < 0: 
         return ("OK WHERE'S MY ORDER THAN?!")
      elif 1 < num < 50:     #the normal response
         return (num)
      else:
         return ('YOU ORDERING FOR AN ENTIRE TOWN OR SOMETHING?!')

def loop_orde(lop):
 if lop == "NO":
  orde = input('WHAT ELSE YOU LIKE TO ORDER?! ')


  if orde in menu:
   amount = int(input("HOW MANY WOULD YOU LIKE?! "))

   if 1< amount < 50:
      again = input("IS THAT ALL?!")
      repe = loop_orde(again)
      

    entire_orde[orde]
  
  
  else:
    ting = amount_orde(amount)
    print (ting)

 elif lop == "NO":
   """t"""
  

amount = int(input("you know what to do "))
ting = amount_orde(amount)
print (ting)
 
 
 #Mainline
"""while True:
    response = input("Enter your response: ")
    if not response.isupper():
        print("Please respond in upper case.")
    else:
        print("Your response: ", response)
        break"""

"""while volum.islower():
     print("WHAT WAS THAT!?")
     input("SPEAK UP! ")"""





"""nam = input('NAME?! ')
while nam.islower():            #THIS needs to be swapped with the one up somewhere
  print("WHAT WAS THAT!?")
  input("SPEAK UP! ")"""


print("CURRENTLY WE ARE SELLING:----COFFEE'S----MUFFINS----BANNANA BREAD----PASTRY'S----TEA----SALTED CARAMEL LATTES---AND---CAPPUCCINO")
orde = input('WHAT WOULD YOU LIKE TO ORDER?! ')


if orde in menu:
 amount = int(input("HOW MANY WOULD YOU LIKE?! "))
 if 1< amount < 50:
   nam = input('NAME?!')
   if nam in reg:
     print("YOU HAVE A 15% DISCOUNT FOR BEING A REGULAR CUSTOMER!")
     again = input("IS THAT ALL?!")
     repe = loop_orde(again)
     
     """print(F'IF THATS ALL {}')"""

   else:
    again = input("IS THAT ALL?!")
    if again == "YES":
      print('tes')



 else:
    ting = amount_orde(amount)
    print (ting)
else: 
  print(f'DID YOU HEAR ME SAY {orde} WAS ON THE MENU?!')









if orde.islower():

  print("I DIDN'T HEAR YOUR ORDER!")

elif orde.isupper():
  num = input("HOW MANY WOULD YOU LIKE?! ") 
  print(num, orde + "S COMING RIGHT UP!")
else:
  print("I CAN'T UNDERSTAND YOU!")