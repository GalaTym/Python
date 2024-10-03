age = int(input('Enter your age: '))

if age > 100:
    print('You are too old')
elif age >= 18:
    print('You are now signed up!')
elif age < 0:
    print('You havent been born yet!')

else:
    print('You must be 18+ to sign up!')

response = input('Whould you like some food? (Y/N): ')
# == два дорівнює тому що якби було одне, значить responce is(=) Y
if response == 'Y':
    print('Enjoy your food')
else:
    print('No food for you')

name = input('Enter your name')

if name == '':
    print('You havent entered your name!')
else:
    print(f'You have a beautiful name, {name}!')
