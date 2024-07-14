#Task 2: Bank Interest If you have a savings account with a particular 
# initial amount and a fixed yearly interest rate, 
# calculate the total amount in your account after a year.
#  So if you had $10,000 at a 7% interest write code that would tell us the 
# amount at the end of the year. For the example the expected outcome would be $10,700.

bank_account = input("How much money are you starting with? (Do not include commas)")
interest_amount = input("What is your yearly interest rate persentage?")
bank_account = float(bank_account)
interest_amount = float(interest_amount)/100
bank_account+=bank_account*(interest_amount)
bank_account = format(bank_account,".2f")
print("At the end of the year you will have $", bank_account)

