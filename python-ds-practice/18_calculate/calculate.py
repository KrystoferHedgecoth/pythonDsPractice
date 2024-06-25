def calculate(operation, a, b, make_int=False, message='The result is'):
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y!= 0 else 'Cannot divide by zero',
    }

    if operation not in operations:
        return None

    result = operations[operation](a, b)

    if make_int:
        result = int(result)

    return f"{message} {result}"