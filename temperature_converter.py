unit = input('Is the temperature in Celsius or in Fahrenheit? C or F: ')
temp = float(input('Enter the temperature: '))

if unit == 'F':
    temp = ((temp - 32)/1.8)
    unit = 'C'
    print(f'The temperature is {round(temp, 1)}{unit}')

elif unit == 'C':
    temp = (temp * 1.8 + 32)
    unit = 'F'
    print(f'The temperature is {round(temp, 1)}{unit}')

else:
    print('Unit is not valid')
