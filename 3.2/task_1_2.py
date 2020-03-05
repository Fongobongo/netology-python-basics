import requests


def translate_it(from_file, to_file, from_lang, to_lang='ru'):
    api_key = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

    with open(from_file, encoding='utf-8') as file_text:
        text = file_text.read()

    params = {
        'key': api_key,
        'text': text,
        'lang': f'{from_lang}-{to_lang}',
        'format': 'plain'
    }

    response = requests.get(url, params=params)
    response_json = response.json()
    answer = ''.join(response_json['text'])

    with open(to_file, 'w', encoding='utf-8') as file_result:
        file_result.write(answer)

    return


def upload_to_yadisk(token):
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    params = {
        'path': 'translated.txt',
        'overwrite': 'true'
    }

    headers = {
        'Authorization': f'OAuth {token}'
    }

    response = requests.get(url, params=params, headers=headers)
    response_json = response.json()
    upload_url = response_json['href']

    with open('result.txt', 'rb') as result:
        requests.put(upload_url, result)

    return


if __name__ == '__main__':
    translate_it('de.txt', 'result.txt', 'de')
    upload_to_yadisk('INSERT YOUR TOKEN HERE')
