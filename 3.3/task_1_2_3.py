import requests
from pprint import pprint as pp

token = 'eaa1603beaa1603beaa1603b7eead17a9beeaa1eaa1603bb4c1907d35f3c7f4b5d3cbcc'


class User:

    def __init__(self, vk_id):
        self.vk_id = vk_id

    def __str__(self):
        link = f'https://vk.com/id{self.vk_id}'
        return link

    # Не совсем понял задание № 2. Может сразу ссылки на профили нужно было выдавать? Тогда пригодится код ниже.
    # def __repr__(self):
    #     link = f'https://vk.com/id{self.vk_id}'
    #     return link

    def __and__(self, other):
        common_friends = list(self.get_friends_list() & other.get_friends_list())
        friends_class_list = []
        for friends_count, friend in enumerate(common_friends, 1):
            friends_class_list.append(User(friend))
        print(f'Общих друзей: {friends_count}. Список общих друзей с экземплярами классов:')
        pp(friends_class_list)
        print(f'Ссылки на профили общих друзей:')
        for friend in friends_class_list:
            print(friend)
        return friends_class_list

    def get_friends_list(self):
        url = f'https://api.vk.com/method/friends.get?PARAMETERS'

        params = {
            'access_token': token,
            'user_id': self.vk_id,
            'v': '5.8'
        }

        response = requests.get(url, params=params)
        friends_list = set(response.json().get('response').get('items'))
        return friends_list


user1 = User(12683387)
user2 = User(15447726)

user1 & user2

print(f"Ссылка на профиль первого пользователя: {user1}")
print(f"Ссылка на профиль второго пользователя: {user2}")
