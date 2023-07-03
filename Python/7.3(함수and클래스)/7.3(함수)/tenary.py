numbers = [1, 2, 3, 4, 5]
result = ['even' if num % 2 == 0 else 'odd' for num in numbers]
result = [num for num in numbers if num % 2 == 0]
print(result)
