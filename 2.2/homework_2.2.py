class Animal:
    food = 'fodder'


class Eggs:
    utility = 'Собирать яйца'


class Milk:
    utility = 'Доить'


class Goose(Animal, Eggs):
    sound = 'Ga-ga-ga'

    def __init__(self, name='Серый', weight=3):
        self.name = name
        self.weight = weight


class Cow(Animal, Milk):
    sound = 'Moooo'

    def __init__(self):
        self.name = 'Манька'
        self.weight = 450  # kg


class Sheep(Animal):
    utility = 'Стричь'
    sound = 'Mee'

    def __init__(self, name='Барашек', weight=120):
        self.name = name
        self.weight = weight


class Hen(Animal, Eggs):
    sound = 'Buc'

    def __init__(self, name='Ко-ко', weight=0.8):
        self.name = name
        self.weight = weight


class Goat(Animal, Milk):
    sound = 'Naa'

    def __init__(self, name='Рога', weight=100):
        self.name = name
        self.weight = weight


class Duck(Animal, Eggs):
    sound = 'Quack'

    def __init__(self):
        self.name = 'Кряква'
        self.weight = 1.1  # kg


goose1 = Goose()
goose2 = Goose('Белый', 2.5)

cow1 = Cow()

sheep1 = Sheep()
sheep2 = Sheep('Кудрявый', 105)

hen1 = Hen()
hen2 = Hen('Кукареку', 1)

goat1 = Goat()
goat2 = Goat('Копыта', 110)

duck1 = Duck()

animals = [goose1, goose2, cow1, sheep1, sheep2, hen1, hen2, goat1, goat2, duck1]

weight = 0
top_weight = 0
top_weight_name = ''

for each in animals:
    weight += each.weight
    if each.weight > top_weight:
        top_weight = each.weight
        top_weight_name = each.name

print(f"Общий вес животных составляет {weight} кг.")
print(f"Самое тяжелое животное - {top_weight_name}, весит {top_weight} кг.")
