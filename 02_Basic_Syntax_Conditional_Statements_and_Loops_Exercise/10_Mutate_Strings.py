string_one = input()
string_two = input()

last_printed_string = string_one
for character_index in range(len(string_one)):
    left_part = string_two[:character_index + 1]
    right_part = string_one[character_index + 1:]
    new_string = left_part + right_part
    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string

# Slicing
# print(my_string[start:end:step])
# print(my_string[start:end])
# print(my_string[start:])
# print(my_string[:end])
# print(my_string[::step])
