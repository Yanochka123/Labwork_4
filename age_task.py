class respondent:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age


class age_groups:
    def __init__(self, low_limit, upper_limit):
        self.__low_limit = low_limit  # приватный
        self.__upper_limit = upper_limit  # приватный
        self.__respondents = []  # приватный

    def get_low(self):
        return self.__low_limit

    def get_upper(self):
        return self.__upper_limit

    def add_respondent(self, name, age):
        new_respondent = respondent(name, age)
        self.__respondents.append(new_respondent)

    def display_group(self):
        if len(self.__respondents) == 0:
            pass
        else:
            print(self.__low_limit, '-', self.__upper_limit, ':', sep='', end=' ')
            for i in range(len(self.__respondents)-1):
                print(' ', self.__respondents[i].get_name(), '(',
                      self.__respondents[i].get_age(), '),', sep='', end=' ')

            print(' ', self.__respondents[-1].get_name(), '(',
                  self.__respondents[-1].get_age(), ')', sep='')


def binary_search(list1, low, high, n):
    mid = int((low + high)/2)
    if (high - low == 1) or (high == low):
        if list1[high] == n:
            return high
        else:
            return low
    elif list1[mid] < n:
        return binary_search(list1, mid + 1, high, n)
    # Else the search moves to the right sublist1
    else:
        return binary_search(list1, low, mid, n)


if __name__ == "__main__":
    age = input()
    numbers = [int(i) for i in age.split(' ')]
    # создаем массив с экземплярами класса
    age_list_groups = []
    start_year = 0
    for i in range(len(numbers)):
        new_group = age_groups(start_year, numbers[i])
        age_list_groups.append(new_group)
        start_year = numbers[i] + 1
    new_group = age_groups(start_year, 123)
    age_list_groups.append(new_group)
    # получаем первую строку данных
    poll_info = input()
    # ввод всех данных и запись в экземпляры класса
    numbers.insert(0, 0)
    numbers.append(124)
    while (poll_info != "END"):
        current_name, current_age = poll_info.split(", ")
        # group_index = binary_search(
        #    numbers, 0, len(numbers)-1, int(current_age))
        for j in range(len(numbers) - 1):
            if (numbers[j] <= int(current_age)) and (numbers[j+1] > int(current_age)):
                group_index = j
                break
        age_list_groups[group_index].add_respondent(current_name, current_age)
        poll_info = input()

    # c помощью методов класса выводим всю необходимую информацию
    for i in range(len(age_list_groups)-1, -1, -1):
        age_list_groups[i].display_group()
