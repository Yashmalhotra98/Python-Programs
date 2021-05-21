import datetime

print('Welcome to the Grocery List App.')

# Create date time object & put current date & time.
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

print(f'Current Date and Time: {month}/{day}\t {hour}:{minute}')

grocery_list = ['Meat', 'Cheese']
print(f'You currently have {grocery_list[0]} and {grocery_list[1]} in your list.\n')
item = input('Type of food to add to the grocery list: ').title() # If we put the title() method inside the input() function then it would capitalize all the first letters of the prompt statement inside the input() function
grocery_list.append(item) # But if we put it outside, (like here) then it will capitalize the first letters of the input that  we give as users.
item = input('Type of food to add to the grocery list: ').title()
grocery_list.append(item)
item = input('Type of food to add to the grocery list: ').title()
grocery_list.append(item)

print(f'\nHere is your grocery list:\n', grocery_list)
print(f'Here is your grocery list sorted:')
grocery_list.sort()
print(grocery_list)

print(f'\nSimulating grocery shopping...\n')

print(f'Current grocery list: {len(grocery_list)} items\n', grocery_list)

item = input('What food did you just buy:').title()
grocery_list.remove(item)
print(f'Removing {item} from list...\n')

print(f'Current grocery list: {len(grocery_list)} items\n', grocery_list)
item = input('What food did you just buy:').title()
grocery_list.remove(item)
print(f'Removing {item} from list...\n')

print(f'Current grocery list: {len(grocery_list)} items\n', grocery_list)
item = input('What food did you just buy:').title()
grocery_list.remove(item)
print(f'Removing {item} from list...\n')

print(f'Sorry, the store is out of {grocery_list[-1]}')
grocery_list.pop()
item = input('What food would you like instead:').title()
grocery_list.insert(0, item)
print(grocery_list)