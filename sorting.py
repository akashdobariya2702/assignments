user_input = raw_input("Enter Random String With Space to Sort :")
ui_arr = user_input.split(" ")
uniqe_arr = []
for val in ui_arr:
    if val not in uniqe_arr:
        uniqe_arr.append(val)
for i in range(len(uniqe_arr)-1):
    for j in range(len(uniqe_arr)-1):
        if uniqe_arr[j] > uniqe_arr[j+1]:
            temp = uniqe_arr[j+1]
            uniqe_arr[j+1] = uniqe_arr[j]
            uniqe_arr[j] = temp

print " ".join(uniqe_arr)
