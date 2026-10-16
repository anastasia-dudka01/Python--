class Media:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value < 0 or value > 10:
            raise ValueError("Рейтинг должен быть от 0 до 10")
        self._rating = value

    def show_info(self):
        return self.title + " (" + str(self.year) + ")"


class Movie(Media):
    def __init__(self, title, year, rating, duration):
        super().__init__(title, year, rating)
        self.duration = duration

    def size(self):
        return self.duration

    def show_info(self):
        return "Фильм: " + self.title + " (" + str(self.year) + "), " + \
               str(self.duration) + " мин, рейтинг " + str(self.rating)


class Series(Media):
    def __init__(self, title, year, rating, seasons):
        super().__init__(title, year, rating)
        self.seasons = seasons

    def size(self):
        return self.seasons * 10

    def show_info(self):
        return "Сериал: " + self.title + " (" + str(self.year) + "), " + \
               str(self.seasons) + " сезон(ов), рейтинг " + str(self.rating)


class MediaLibrary:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show_all(self):
        print("Библиотека: " + self.name)
        for item in self.items:
            print("  " + item.show_info())

    def total_size(self):
        total = 0
        for item in self.items:
            total = total + item.size()
        return total

    def best(self):
        best = self.items[0]
        for item in self.items:
            if item.rating > best.rating:
                best = item
        return best

    def average(self):
        total = 0
        for item in self.items:
            total = total + item.rating
        return total / len(self.items)


movies = []
movies.append(Movie("Начало", 2010, 9.0, 148))
movies.append(Movie("Матрица", 1999, 8.7, 136))
movies.append(Series("Игра престолов", 2011, 9.5, 8))
movies.append(Series("Друзья", 1994, 8.9, 10))
movies.append(Movie("Интерстеллар", 2014, 8.6, 169))

library = MediaLibrary("Моя фильмотека")

for m in movies:
    library.add(m)

library.show_all()

print()
print("Общая продолжительность: " + str(library.total_size()) + " мин")

best = library.best()
print("Лучший по рейтингу: " + best.title)

print("Средний рейтинг: " + str(round(library.average(), 2)))

print()
print("Проверка инкапсуляции:")

try:
    movies[0].rating = 15
except ValueError as e:
    print("Ошибка: " + str(e))

print()
print("Полиморфизм - общий метод show_info() для разных классов:")
for m in movies:
    print("  " + m.show_info())