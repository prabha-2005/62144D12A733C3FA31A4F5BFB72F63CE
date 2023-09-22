class bankAccount :_

  

 def  __ int__ (self , account_number , account_holder_name, initial_blance=0.0):

  self.account_number= account_number

  self.__account_holder_name= account_holder_name
 
 self.__account_balance=initial_balance

 
  def deposit(self, amount):
    if amount > 0:

    self.__account_balance += amount
 
   print( "Deposited${}. NEW balance: ${}". format(amount,self.__account_balance))

else:

 print("Invaleid deposeit amount.please depose a positive amount.")


  def withdraw(self, amount):

 if amount > 0 and amount <=self.__account_balance:

      self.__account_balance _= amount
 
    print("withdrew ${}. New balance: ${}".format(amount,self.__account_balance))

else:

 print("Invalid withdrawal amount or insufficient balance.")


  def display_balance(self):
 
    print("Account balance for {}")