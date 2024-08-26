# Challenge 1: Basic Set Operations
fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')
fruits.add('apple')
fruits.remove('banana')
print(fruits)
print()
# Challenge 2: Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a-set_b)
print()
# Challenge 3: Symmetric Difference
set_c = {1, 2, 3, 4, 5}
set_d = {4, 5, 6, 7, 8, }
print(set_c.symmetric_difference(set_d))
# Challenge 4: Subset and Superset
set_e = {1, 2, 3}
set_f = {1, 2, 3, 4, 5}
if set_e.issubset(set_f) is True:
    print("e is subset of f")
else:
    print('e is not a subset of f')
if set_f.issuperset(set_e) is True:
    print("f is a superset of e")
else:
    print("f is not  a superset of e")
# Challenge 5: Practical Application
completed_assignment_1 = {'Alice', "Bob", 'Charles'}
completed_assignment_2 = {'Bob', 'Charles', 'David'}
print(f"At least one:{completed_assignment_1.union(completed_assignment_2)}")
print(f"Both:{completed_assignment_1.intersection(completed_assignment_2)}")
