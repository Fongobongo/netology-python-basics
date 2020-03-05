import requests
import glob


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


def upload_to_yadisk(token, filename):
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    params = {
        'path': filename,
        'overwrite': 'true'
    }

    headers = {
        'Authorization': f'OAuth {token}'
    }

    response = requests.get(url, params=params, headers=headers)
    response_json = response.json()
    upload_url = response_json['href']

    with open(filename, 'rb') as file_to_upload:
        requests.put(upload_url, file_to_upload)

    return


if __name__ == '__main__':
    for original_file in glob.glob('*.txt'):
        file_lang = original_file[:-4].lower()
        translated_file = f'translated_from_{file_lang}.txt'
        translate_it(original_file, translated_file, file_lang)
        upload_to_yadisk('AgAAAAAMkE0HAADLW1UZrj8lmEctpzTITFE2Rg8', translated_file)
