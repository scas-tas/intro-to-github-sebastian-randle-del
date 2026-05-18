#banking

class Account:
  def __init__(self, number, balance, owner):
    self.number = number 
    self.balance = balance 
    self.owner = owner 

  def deposit(self, amount):
    self.balance = self.balance + amount
  
  def withdrawl(self, amount):
    self.balance = self.balance - amount

#____________________MAINLINE_______________________________

robertAccount = Account("12345", 100, "robert")

sebAccount = Account("13452", 2, "seb")

zavoneAccount = Account("14523", 100000, "zavone")

robertAccount.deposit(100)

made_account = [sebAccount, robertAccount, zavoneAccount]

valid = False

print(robertAccount.owner)
print(robertAccount.balance)
print(robertAccount.number)

#interaction_start

valid = False

# Keep looping until a valid account number is entered
while valid == False:

    # Ask user for an account number
    access_account = input("Bank account number: ")

    # Check every account in the list
    for account in made_account:

        # Compare the entered number with the account's number
        if access_account == account.number:

            print("Account found")
            print("Owner:", account.owner)
            print("Balance:", account.balance)

            # Stop the loop
            valid = True

            # Exit the for-loop immediately
            break

    # If no account matched
    if valid == False:
        print("Invalid account number")





"""while valid == False:

  access_account = input("bank account number: ")

  for account in made_account:

      if access_account == account.number:        #checks if thats a real account number
       print("check")   
       print ("account owner's name:  " account.owner)


       valid = True
valid = True"""



