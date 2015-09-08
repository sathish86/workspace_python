N = input()
list_with_spaces = raw_input()

list_of_ap = list_with_spaces.split(" ")

start_pos = 0
next_pos = 0
main_diff = 0
first_element = False
counter = 0

import pdb; pdb.set_trace()


for index , i in enumerate(list_of_ap):
    i = int(i)
    first_element = False

    if start_pos == 0:
        start_pos = i
        first_element = True
        continue

    next_pos = i

    temp_start_pos = start_pos
    start_pos = next_pos

    loop_res = abs(temp_start_pos - next_pos)

    if main_diff == 0:
        main_diff = abs(temp_start_pos - next_pos)
        last_val = abs(int(list_of_ap[-1]) - int(list_of_ap[-2]))
        check_diff = abs(main_diff - last_val)
        if check_diff != 0:
            print int(list_of_ap[(index-1)]) + last_val
            break

    if first_element is False:
        check_diff = abs(main_diff - loop_res)

        if check_diff != 0:
            print int(list_of_ap[(index-1)]) + main_diff
            break



