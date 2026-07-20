#banking

class Account:

  def __init__(self, number, balance, owner):
    self.number = number 
    self.balance = balance 
    self.owner = owner 

  def deposit(self, amount):
    self.balance = self.balance + amount
  
  def withdrawl(self,amount):
    self.balance = self.balance - amount

class interest:
#____________________MAINLINE_______________________________

robertAccount = Account("12345", 100, "robert")

sebAccount = Account("13452", 2, "seb")

zavoneAccount = Account("14523", 100000, "zavone")

robertAccount.deposit(100)

made_account = [sebAccount, robertAccount, zavoneAccount]


print(robertAccount.owner)
print(robertAccount.balance)
print(robertAccount.number)

#interaction_start

select = "unselected"

valid = False

# Keep looping until a valid account number is entered
while valid == False:

    # Ask user for an account number
    access_account = input("Bank account number: ")

    # Check every account in the list
    for account in made_account:

        # Compare the entered number with the account's number
        if access_account == account.number:

            print("valid Account number")
            print("Owner:", account.owner)
            print("Balance:", account.balance)

            opened_account = account

            # Stop the loop
            valid = True

            # Exit the for-loop immediately
            break

    # If no account matched
    if valid == False:
        print("Invalid account number")

print("to select an option please write what you would like to do")

while select == "unselected":
   moving_money = input("would you like to -DEPOSIT- or -WITHDRAW- money :")
   moving_money = moving_money.upper()

   if moving_money == "DEPOSIT":                                   # checks if you would like to deposit money
     money = int(input("how much would you like to deposit?: "))
     opened_account.deposit(money)
     print ("new account balance: ", opened_account.balance)
     select = "selected"

   elif moving_money == "WITHDRAW":                                # checks if you would like to withdraw money
     money = int(input("how much would you like to withdraw?: "))
     opened_account.withdrawl(money)
     if account.balance <= -1:
        print("insufficient funds")

     else:
      print ("new account balance: ", opened_account.balance)
     select = "selected"

   else:
     print("that is an invalid response please try again.")
   