def function_with_uncommon_error(data):
    try:
        result = data['key'] * 2 # KeyError if 'key' is missing
        return result
except KeyError:
    return 0

data = {}
result = function_with_uncommon_error(data)
print(result)  # Output: 0