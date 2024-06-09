my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num1 = 0
while num1 < len(my_list):
    if my_list[num1] < 0:
        break
    elif my_list[num1] == 0:
        num1 += 1
        continue
    else:
        print(my_list[num1])
        num1 += 1
