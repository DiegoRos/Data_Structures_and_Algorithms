# A set is like a python dict but without values (aka only keys)
# To make an empty set we can utilize the set() constructor

a = set()
a.add(1)
a.add(2)
a.add(1)# This number will not be saved since sets are equivalente even if they have repeated values.
a.add(15)

print(a)