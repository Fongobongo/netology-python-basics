import requests
import json
import time

TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'


class PrivateUserException(Exception):
    def __init__(self):
        return


class NotANumberException(Exception):
    def __init__(self):
        return


class UserDeletedException(Exception):
    def __init__(self):
        return


class ServerErrorException(Exception):
    def __init__(self):
        return


def ask_for_username():
    user_input = input('Введите имя пользователя или его id в ВК: ')
    vk_id = None
    n = None

    if user_input.isdigit() and int(user_input) > 0:
        vk_id = user_input
    elif user_input.isalpha():
        vk_id = get_vk_id(user_input)
    elif user_input[2:].isdigit():
        vk_id = user_input[2:]
    else:
        print(f'Введённое значение "{user_input}" не является корректным')

    if vk_id:
        n = input('Введите максимальное количество человек, у которых могут быть общие с пользователем группы: ')

        if not n.isdigit():
            raise NotANumberException
        else:
            n = int(n)
    return vk_id, n

def get_response_without_error6(url, params):
    repeat = True
    response = None
    retry = 5

    while repeat:

        try:
            response = requests.get(url, params=params).json()

            if 'error' in response and 'error_code' in response['error'] and response['error']['error_code'] == 6:
                print('Эта кобыла не может гнать так быстро, дадим ей передохнуть хотя бы пару секунд')
                time.sleep(2)
            else:
                repeat = False
        except requests.exceptions.ReadTimeout:
            if retry > 0:
                print(f'Сервер не отправил данные. Попробуем снова через 10 секунд. Осталось попыток: {retry}')
                retry -= 1
                time.sleep(10)
            else:
                raise ServerErrorException

    return response

def get_vk_id(username):
    url = f'https://api.vk.com/method/users.get?PARAMETERS'

    params = {
        'access_token': TOKEN,
        'user_ids': username,
        'v': '5.89'
    }
    print(f'Запрашиваем VK ID у пользователя {username}')
    response = get_response_without_error6(url, params)

    if 'error' in response and 'error_code' in response['error'] and response['error']['error_code'] == 113:
        print(f'Пользователь {username} не найден среди пользователей VK')
        return
    elif 'error' in response:
        print(f'При запросе VK ID {username} что-то пошло не так')
        return

    vk_id = response.get('response')[0].get('id')
    print(f'VK ID у пользователя {username} получен: {vk_id}')
    return vk_id


class User:

    def __init__(self, vk_id):
        self.vk_id = vk_id

    def get_friends_list(self):
        url = f'https://api.vk.com/method/friends.get?PARAMETERS'

        params = {
            'access_token': TOKEN,
            'user_id': self.vk_id,
            'v': '5.8'
        }

        print(f'Получаем список друзей у пользователя с VK ID {self.vk_id}')
        response = get_response_without_error6(url, params=params)
        if 'error' in response and 'error_code' in response['error'] and response['error']['error_code'] == 15:
            raise PrivateUserException
        if 'error' in response and 'error_code' in response['error'] and response['error']['error_code'] == 18:
            raise UserDeletedException

        friends_list = response.get('response').get('items')
        return friends_list

    def get_groups(self):
        url = f'https://api.vk.com/method/groups.get?PARAMETERS'

        params = {
            'access_token': TOKEN,
            'user_id': self.vk_id,
            'count': 1000,
            'extended': 1,
            'fields': 'members_count',
            'v': '5.103'
        }

        response = get_response_without_error6(url, params)

        if 'error' in response and 'error_code' in response['error'] and response['error']['error_code'] == 7:
            print(f'Нет доступа к группам пользователя с VK ID {self.vk_id}')
            return
        elif 'error' in response and 'error_code' in response['error'] and response['error']['error_code'] == 18:
            print(f'Пользователь с VK ID {self.vk_id} удалён или заблокирован')
            return
        elif 'error' in response and 'error_code' in response['error'] and response['error']['error_code'] == 30:
            print(f'Профиль c VK ID {self.vk_id} является приватным')
            return
        elif 'error' in response:
            print(f'C пользователем {self.vk_id} что-то пошло не так')
            return

        groups = response.get('response').get('items')
        groups_json = []

        for group in groups:
            if group.get('members_count') is None:
                continue
            group_dict = dict()
            group_dict['name'] = group['name']
            group_dict['gid'] = group['id']
            group_dict['members_count'] = group['members_count']
            groups_json.append(group_dict)
        return groups_json

    def create_users_list(self):
        friends = self.get_friends_list()
        users_class_list = [self]
        if friends:
            for friend in friends:
                users_class_list.append(User(friend))
        return users_class_list


def create_groups_dict(victim_user):
    all_groups = dict()
    all_users = victim_user.create_users_list()
    total_users = len(all_users)
    left_users = total_users
    for each_user in all_users:
        progress = (total_users - left_users) / total_users * 100
        print(f'Осталось обработать пользователей: {left_users}. Общий прогресс: {progress:.2f}%')
        print(f'Получаем группы у пользователя с VK ID {each_user.vk_id}')
        user_groups = each_user.get_groups()
        if user_groups:
            for group in user_groups:
                if each_user == victim_user:
                    group['victim_in_group'] = True
                else:
                    group['victim_in_group'] = False
                gid = group.pop('gid')
                if gid not in all_groups:
                    group['users_in_group'] = [each_user.vk_id]
                    group['users_count'] = 1
                    all_groups[gid] = group
                else:
                    all_groups[gid]['users_in_group'].append(each_user.vk_id)
                    all_groups[gid]['users_count'] += 1
        left_users -= 1
    return all_groups

def create_json(all_info, n=0):
    groups_json = []
    for key, value in all_info.items():
        if value['victim_in_group'] and value['users_count'] <= n + 1:
            group_dict = dict()
            group_dict['name'] = value['name']
            group_dict['gid'] = key
            group_dict['members_count'] = value['members_count']
            groups_json.append(group_dict)
    if groups_json:
        with open('groups.json', 'w', encoding='utf-8') as f:
            json.dump(groups_json, f, ensure_ascii=False, indent=2)
            print("Выполнено. Файл groups.json сформирован")
    else:
        print("Выполнено. Подходящих групп не найдено. Файл groups.json не был сформирован")
    return groups_json

if __name__ == '__main__':
    try:
        user_id, max_amount = ask_for_username()
        if user_id and max_amount is not None:
            victim = User(user_id)
            groups_info = create_groups_dict(victim)
            create_json(groups_info, max_amount)
    except ServerErrorException:
        print('Не удалось получить ответ. Сервер недоступен')
    except NotANumberException:
        print('Введено неверное количество человек')
    except PrivateUserException:
        print('Нет доступа к профилю этого пользователя')
    except UserDeletedException:
        print('Такого пользователя не существует, либо он был забанен')
