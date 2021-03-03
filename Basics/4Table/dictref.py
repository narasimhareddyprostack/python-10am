emp = {'name': 'raj'}
new_Emp = emp

emp['name'] = 'Raj Kumar'

print(id(emp))
print(id(new_Emp))
print(emp)
print(new_Emp)