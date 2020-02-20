class Animal():
    animals = []
    food = 'fodder'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.animals.append(self)

    @classmethod
    def top_weight(cls):
        weight = 0
        top_weight = 0
        top_weight_name = ''

        for each in cls.animals:
            weight += each.weight
            if each.weight > top_weight:
                top_weight = each.weight
                top_weight_name = each.name

        print(f"Общий вес животных составляет {weight} кг.")
        print(f"Самое тяжелое животное - {top_weight_name}, весит {top_weight} кг.")


class Eggs:
    utility = 'Собирать яйца'


class Milk:
    utility = 'Доить'


class Goose(Animal, Eggs):
    sound = 'Ga-ga-ga'


class Cow(Animal, Milk):
    sound = 'Moooo'


class Sheep(Animal):
    utility = 'Стричь'
    sound = 'Mee'


class Hen(Animal, Eggs):
    sound = 'Buc'


class Goat(Animal, Milk):
    sound = 'Naa'


class Duck(Animal, Eggs):
    sound = 'Quack'

goose1 = Goose('Серый', 3)
goose2 = Goose('Белый', 2.5)

cow1 = Cow('Манька', 450)

sheep1 = Sheep('Барашек', 120)
sheep2 = Sheep('Кудрявый', 105)

hen1 = Hen('Ко-ко', 0.8)
hen2 = Hen('Кукареку', 1)

goat1 = Goat('Рога', 100)
goat2 = Goat('Копыта', 110)

duck1 = Duck('Кряква', 1.1)

Animal.top_weight()
