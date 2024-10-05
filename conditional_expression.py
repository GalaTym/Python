# (X if condition else Y)

num = 9
a = 9
b = 7
age = 16
temperature = 5
user_role = 'guest'


print('Positive' if num > 0 else 'Negative')

result = 'Even' if num % 2 == 0 else 'Odd'
print(result)

max_num = b if a > b else b
print(max_num)

min_num = a if a < b else b
print(min_num)

status = 'Adult' if age >= 18 else 'Child'
print(status)

weather = 'Hot' if temperature > 29 else 'Good'
print(weather)

access_level = 'Full axxess' if user_role == 'Admin' else 'Limited access'
print(access_level)
