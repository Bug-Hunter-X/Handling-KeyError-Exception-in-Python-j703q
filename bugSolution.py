def function_with_uncommon_error(data):
    try:
        result = data.get('key', 0) * 2  # Use get() method with default value
        return result
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    return 0

data = {}
result = function_with_uncommon_error(data)
print(result)  # Output: 0

data = {'key': 5}
result = function_with_uncommon_error(data)
print(result)  # Output: 10