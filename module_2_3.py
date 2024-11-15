my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    numbder = my_list[index]
    if numbder < 0:
        break
    elif numbder > 0:
        print(numbder)
    index += 1