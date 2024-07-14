#Task 1: Grocery Store Math Calculate the total cost of three items 
# you'd commonly find in a grocery store, given their individual prices. 
# For example, what would be the cost of bread, peanut butter, and jelly be? 
# Prices don't need to be realistic!
from decimal import *
getcontext().prec = 2

print("Grocery Calculator")

item_one =input("First item?")+","
price_one = input("Price?")
item_two = input("Second item?")+","
price_two = input("Price?")
item_three = input("Third item?")
price_three = input("Price?")
total = float(price_one)+float(price_two)+float(price_three)

#Fix cases that the last digit is zero. Changes notation of $12.0 to correct notation of $12.00
total = format(total,".2f")

#prints final answer
print(item_one,item_two,"and,",item_three, "cost: $", total)  # extra_zero)
