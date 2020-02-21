cook_book = {}


def add_dish(dish_name):
    number_of_ingredients = file.readline()

    ingredients_list = []

    for i in range(int(number_of_ingredients)):
        ingredient_dict = {}
        ingredient = file.readline().split("|")
        ingredient_dict["ingredient_name"] = ingredient[0].strip()
        ingredient_dict["quantity"] = ingredient[1].strip()
        ingredient_dict["measure"] = ingredient[2].strip()
        ingredients_list.append(ingredient_dict)

    file.readline()

    return ingredients_list


with open("recipes.txt") as file:
    while True:
        new_dish = file.readline()

        if not new_dish:
            break

        cook_book[new_dish.strip()] = add_dish(new_dish)

print(f"Получился следующий словарь блюд: {cook_book}.")


def get_shop_list_by_dishes(dishes, person_count):
    all_ingredients = {}

    for dish in dishes:
        for ingredient in cook_book.get(dish):
            new_ingredient = ingredient.pop('ingredient_name')
            if all_ingredients.get(new_ingredient) is None:
                all_ingredients[new_ingredient] = ingredient
            else:
                all_ingredients[new_ingredient]['quantity'] = int(all_ingredients[new_ingredient]['quantity']) + int(ingredient['quantity'])
            all_ingredients[new_ingredient]['quantity'] = int(all_ingredients[new_ingredient]['quantity']) * person_count

    return all_ingredients


print("Словарь с названием ингредиентов и его количества для блюда:", get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
