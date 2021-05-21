#Letter Counter App

# A welcome message!
name =input('What is your name: ').title().strip()
print('Hello '+ name + "!\n I will count the number of times that a specific letter occurs in a message.")


# Message & Letter
message = input('Please enter your message:')
counter = input('Which letter would you like to count the occurences of:')


# Standardizing the MEssage Text & The LEtter to be counted
counted_letters = message.lower().count(counter.lower())


# Message to be printed for counting the letters
print("{}, your message has {} {}\'s in it.".format(name, counted_letters, counter))