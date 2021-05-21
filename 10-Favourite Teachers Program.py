print('Welcome to the Favorite Teachers Program\n')

teachers = []
teacher = input('Who is your first favorite teacher:').title()
teachers.append(teacher)
teacher = input('Who is your second favorite teacher:').title()
teachers.append(teacher)
teacher = input('Who is your third favorite teacher:').title()
teachers.append(teacher)
teacher = input('Who is your fourth favorite teacher:').title()
teachers.append(teacher)

print(f'Your favorite teachers ranked are: {teachers}')
sort_teachers = sorted(teachers)
print(f'Your favorite teachers alphabetically are: {sort_teachers}')
rev_teachers = sorted(teachers, reverse = True)
print(f'Your favorite teachers in reverse alphabetical order are: {rev_teachers}\n')

print(f'Your top two teachers are: {teachers[0]} and {teachers[1]}.')
print(f'Your next two favorite teachers are: {teachers[2]} and {teachers[3]}.')
print(f'Your last favorite teacher is: {teachers[-1]}.')
print(f'You have total of {len(teachers)} favorite teachers.\n')

teacher = input(f'Oops, {teachers[0]} is no longer first favorite teacher. Who is your new FAVORITE teacher: ').title()
teachers.insert(0, teacher)

print(f'Your favorite teachers ranked are: {teachers}')
sort_teachers = sorted(teachers)
print(f'Your favorite teachers alphabetically are: {sort_teachers}')
rev_teachers = sorted(teachers, reverse = True)
print(f'Your favorite teachers in reverse alphabetical order are: {rev_teachers}\n')

print(f'Your top two teachers are: {teachers[0]} and {teachers[1]}.')
print(f'Your next two favorite teachers are: {teachers[2]} and {teachers[3]}.')
print(f'Your last favorite teacher is: {teachers[-1]}.')
print(f'You have total of {len(teachers)} favorite teachers.\n')

removed_teacher = input('You\'ve decided you no longer like a teacher. Which teacher would you like to remove from your list:').title()
teachers.remove(removed_teacher)

print(f'Your favorite teachers ranked are: {teachers}')
sort_teachers = sorted(teachers)
print(f'Your favorite teachers alphabetically are: {sort_teachers}')
rev_teachers = sorted(teachers, reverse = True)
print(f'Your favorite teachers in reverse alphabetical order are: {rev_teachers}\n')

print(f'\nYour top two teachers are: {teachers[0]} and {teachers[1]}.')
print(f'Your next two favorite teachers are: {teachers[2]} and {teachers[3]}.')
print(f'Your last favorite teacher is: {teachers[-1]}.')
print(f'You have total of {len(teachers)} favorite teachers.\n')

