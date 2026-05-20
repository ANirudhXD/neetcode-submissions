from typing import List

def read_integers() -> List[int]:
    input_string = input()
    string_list = input_string.split(",")
    int_list = []
    for num in string_list:
        int_list.append(int(num))
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
