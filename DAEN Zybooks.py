
# coding: utf-8

# In[ ]:


initial_value = float(input())
r = 2 ** (1/12)
n = 1
higher_key = initial_value * (r ** n)
print('%0.2f' % (initial_value), end=' ')
print('%0.2f' % (higher_key), end=' ')
n = n + 1
higher_key = initial_value * (r ** n)
print('%0.2f' % (higher_key), end=' ')
n = n + 1
higher_key = initial_value * (r ** n)
print('%0.2f' % (higher_key), end=' ')
n = n + 1
higher_key = initial_value * (r ** n)
print('%0.2f' % (higher_key))

user_int = int(input('Enter integer (32 - 126):\n'))
user_float = float(input('Enter float:\n'))
user_character = input('Enter character:\n')
user_string = input('Enter string:\n')

print(user_int , user_float , user_character , user_string)
print(user_string , user_character , user_float , user_int)
print(user_int , 'converted to a charcter is' , chr(user_int))



# In[ ]:


food_item = input('Enter food item name:\n')
item_price = float(input('Enter item price:\n'))
item_quantity = int(input('Enter item quantity:\n'))
total = 0
item_total = item_price * item_quantity
print()
print('RECEIPT')
print(item_quantity , food_item , '@ $%0.2f = $%0.2f' % ( item_price, item_total))
total = total + item_total
print('Total cost: $%0.2f\n' % (total))
print()
sec_food_item = input('Enter second food item name:\n')
sec_item_price = float(input('Enter item price:\n'))
sec_item_quantity = int(input('Enter item quantity:\n'))
sec_item_total = sec_item_price * sec_item_quantity
print()
print('RECEIPT')
print(item_quantity , food_item , '@ $%0.2f = $%0.2f' % ( item_price, item_total))
print(sec_item_quantity , sec_food_item , '@ $%0.2f = $%0.2f' % ( sec_item_price, sec_item_total))
total = total + sec_item_total
print('Total cost: $%0.2f\n' % (total))
gratuity = .15 * total
total_withtip = total + gratuity
print('15%% gratuity: $%0.2f' % (gratuity))
print('Total with tip: $%0.2f' % (total_withtip))


# In[ ]:


lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
print()
print('Lemonade ingredients - yields %0.2f servings' % servings)
print('%0.2f cup(s) lemon juice' % lemon_juice_cups)
print('%0.2f cup(s) water' % water_cups)
print('%0.2f cup(s) agave nectar' % agave_nectar_cups)
print()
desired_servings = float(input('How many servings would you like to make?\n'))
print()
adj_lemon_juice_cups = (desired_servings / servings) * lemon_juice_cups
adj_water_cups = (desired_servings / servings) * water_cups 
adj_agave_nectar_cups =  (desired_servings / servings) * agave_nectar_cups
adj_lemon_juice_gal = adj_lemon_juice_cups / 16
adj_water_gal = adj_water_cups / 16 
adj_agave_nectar_gal = adj_agave_nectar_cups / 16
print('Lemonade ingredients - yields %0.2f servings' % desired_servings)
print('%0.2f cup(s) lemon juice' % adj_lemon_juice_cups)
print('%0.2f cup(s) water' % adj_water_cups)
print('%0.2f cup(s) agave nectar' % adj_agave_nectar_cups)
print()
print('Lemonade ingredients - yields %0.2f servings' % desired_servings)
print('%0.2f gallon(s) lemon juice' % adj_lemon_juice_gal)
print('%0.2f gallon(s) water' % adj_water_gal)
print('%0.2f gallon(s) agave nectar' % adj_agave_nectar_gal)

