all_user_input = []
user_input = None
print("Enter Random String to Capitalize (blank enter to stop) :")
while user_input != "":
    user_input = raw_input()
    all_user_input.append(user_input)

all_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for user_input in all_user_input:
    final_result = ""
    for ui in user_input:
        final_char = ui
        if ui in all_char and all_char.index(ui) <= 25:
            final_char = all_char[all_char.index(ui)+26]
        final_result += final_char
    print(final_result)
