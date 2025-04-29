week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
hour = ['8 a.m', '9 a.m', '10 a.m', '11 a.m', '12 a.m', '2 p.m', '3 p.m', '4 p.m', '5 p.m']

name = input('Thank you for interesting for our Barber Shop!. Please type your name: ')
while name.isalpha() == False:
    name = input('Incorrect name, please try again: ')
surname = input('Type your surname: ')
while surname.isalpha() == False:
    surname = input('Incorrect surname, please try again: ')

phone = input('Type your phone number. (Example: 988652006): +992 ')
while phone.isdigit() == False or len(phone) != 9:
    phone = input('Incorrect phone number, please try again: +992 ')
print()
for i in range(6):
    print(f'{i+1}. {week[i]}', sep='\n')
date = input('Please pick a day (in numbers): ')
while int(date) > 6 or 0 >= int(date):
    date = input('Incorrect day. Please try again!: ')
print()

for j in range(9):
    print(f'{j+1}. {hour[j]}', sep='\n')
clock = input('Please pick the hour (in numbers): ')
while int(clock) > 9 or 0 >= int(clock):
    clock = input('Incorrect day. Please try again!: ')

print(f'{name} {surname} appointed for {week[int(date)-1]} at {hour[int(clock)-1]}. Please come 15 minutes earlier. Thank you!')




