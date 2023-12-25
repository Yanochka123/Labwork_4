class viewers:
    def __init__(self):
        self.__viewed_films = set()

    def add_film(self, film_list):
        for number in film_list:
            self.__viewed_films.add(number)

    def get_films(self) -> set:
        return self.__viewed_films


class films:
    def __init__(self, int):
        self.__viewers = set()
        self.__rate = 0
        self.__name = int

    def add_viewer(self, viewer):
        self.__viewers.add(viewer)

    def get_viewers(self) -> set:
        return self.__viewers

    def get_name(self):
        return self.__name

    def rating(self):
        self.__rate += 1

    def __lt__(self, other):
        if (self.__rate < other.__rate):
            return True
        else:
            return False


def film_sortion(films) -> list:
    for i in range(len(films)-1):
        for j in range(i+1, len(films)):
            if (films[i] < films[j]):
                films[i], films[j] = films[j], films[i]

    return films



if __name__ == "__main__":
    # input from file
    # get all films from file in set
    with open("films.txt") as file:
        lines = [line.rstrip() for line in file]

    with open("data.txt") as file:
        viewers_data = [line.rstrip() for line in file]

    # получаем список фильмов
    all_films = set()
    for i in lines:
        if i != '':
            all_films.add(int(i[0]))

    films_rating = []
    for i in range(len(all_films)+1):
        new_film = films(i)
        films_rating.append(new_film)

    # парсинг данных пользователей и измнение рейтинга фильмов
    users_list = []
    for v in viewers_data:
        new_user = viewers()
        users_films = [int(i) for i in v.split(',')]
        new_user.add_film(users_films)
        users_list.append(new_user)
        for i in users_films:
            films_rating[i].rating()
            films_rating[i].add_viewer(new_user)

    # sort by rating all films
    films_ = film_sortion(films_rating)

    # обработка пользователя в зависимости от его списка просмотров с помощью множеств
    # и обработки рэйтинга фильмов
    request = input()
    new_user = viewers()
    user_films = [int(i) for i in request.split(',')]
    new_user.add_film(user_films)

    recommendation = set()
    user_rating_films = []
    unseen_rating_films = []
    for i in range(len(films_)):
        if films_[i].get_name() in user_films:
            user_rating_films.append(films_[i])
        else:
            unseen_rating_films.append(films_[i])

    recommendation = user_rating_films[0].get_viewers()
    for i in range(1, int(len(user_rating_films)/2)):
        recommendation = recommendation.intersection(
            user_rating_films[i].get_viewers)

    recommended_films = set()
    if len(recommendation) == 0:
        print(unseen_rating_films[0].get_name())
    else:
        for i in recommendation:
            recommended_films.update(i.get_films())
        recommended_films = recommended_films - new_user.get_films()
        recommended_list = list(recommended_films)
        recommended_list = film_sortion(recommended_list)
        print(recommended_list[0])
