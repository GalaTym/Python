
# at least one of the conditions is True - you can consider the entire statement is True
# temp = 20
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print('The event is canceled')
# else:
#     print('The event is going to happen')


temp = 20
is_sunny = False

if temp < 35 and temp > 12 and is_sunny:
    print('it is warm')
    print('It is sunny')
elif temp >= 36 and is_sunny:
    print('it is hot')
    print('It is sunny')
elif temp < 5 and is_sunny:
    print('it is cold')
    print('It is sunny')
elif temp < 35 and temp > 12 and not is_sunny:
    print('it is warm')
    print('It is cloudy')
elif temp >= 36 and not is_sunny:
    print('it is hot')
    print('It is cloudy')
elif temp < 5 and not is_sunny:
    print('it is cold')
    print('It is cloudy')
