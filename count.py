def get_json_key_count(arr):
    json = {}
    for val in arr:
        if json.has_key(val):
            json[val] += 1
        else:
            json[val] = 1
    return json

arr = ['python', 'pyhton3', 'user1', 'assignment', 'user', 'user1', 'python', 'User1']
print get_json_key_count(arr)
