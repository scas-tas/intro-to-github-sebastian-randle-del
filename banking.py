#banking

class account:
  def ____init___(self, number, balance, owner):
    self.number = number 
    self.balance = balance 
    self.owner = owner 

    #____________________MAINLINE_______________________________
    robert = account("12345", 100000000000000000000000000000000000000000000000000000000000000000, "robert")
    
    #seb = account ("13452", 2, "seb")

    print(robert.owner)
    print(robert.balance)
    print(robert.number)
