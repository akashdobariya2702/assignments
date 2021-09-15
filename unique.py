def get_unique_list(arr):
    final_arr = []
    for val in arr:
        if val not in final_arr:
            final_arr.append(val)
    return final_arr

arr = [1,2,55,1,3,2,34,55]
print get_unique_list(arr)
