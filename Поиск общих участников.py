# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(str1_, str2_, n=","):
    first_group = set(str1_.split(n))
    second_group = set(str2_.split(n))
    common_list = first_group.intersection(second_group)
    common_list = list(common_list)
    common_list.sort()
    return (common_list)

print(find_common_participants(participants_first_group, participants_second_group, n="|"))


# TODO Провеьте работу функции с разделителем отличным от запятой

