size = [10, 20, 30]

newsize = size.copy()
newSize1 = size
size.append(40)

print(size)
print(newsize)
print(newSize1)

print(id(size))
print(id(newsize))
