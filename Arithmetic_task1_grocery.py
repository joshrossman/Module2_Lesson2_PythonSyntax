#Task 1: Grocery Store Math Calculate the total cost of three items 
# you'd commonly find in a grocery store, given their individual prices. 
# For example, what would be the cost of bread, peanut butter, and jelly be? 
# Prices don't need to be realistic!

print("Grocery Calculator")

item_one =input("First item?")+","
price_one = input("Price?")
item_two = input("Second item?")+","
price_two = input("Price?")
item_three = input("Third item?")
price_three = input("Price?")
print(item_one,item_two,"and,",item_three, "cost:", float(price_one)+float(price_two)+float(price_three))
