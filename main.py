first = 123
second = 456
third = 789
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

first_a = 42
second_a = 69
third_a = 42
if first_a == second_a == third_a:
    print(3)
elif first_a == second_a or first_a == third_a or second_a == third_a:
    print(2)
else:
    print(0)