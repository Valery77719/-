# TODO Напишите функцию find_common_participants
list_=()
def find_common_participants(participants_first_group, participants_second_group, delimiter=','):
    participants_first_group = set(participants_first_group.split(delimiter))
    participants_second_group = set(participants_second_group.split(delimiter))



    participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
    return participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой
