emp = {'name': "naraimha", 'age': 38, 'loc': 'Bangalore'}

print(emp.keys())
print(emp.values())

print(emp['name'])
print(emp.get('name'))

emp.pop('loc')

print(emp)
