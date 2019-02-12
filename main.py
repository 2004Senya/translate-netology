import requests

ID = 'c9c38233.5c630b8d.1254d45a-0-0'
URL = 'https://translate.yandex.net/api/v1/tr.json/translate'

def translate_it(file, save, to_lang, from_lang):

    with open(file, 'r') as f:
        text = f.read()
        params = {
            'id': ID,
            'srv': 'tr-text',
            'text': text,
            'reason': 'auto',
            'lang': f'{from_lang}-{to_lang}'
        }

        response = requests.get(URL, params=params)
        json_ = response.json()

        with open(save, 'wb') as f:
            f.write(''.join(json_['text']))
        
        return 'saved'
  
print(translate_it('ES.txt', 'ES-R.txt', 'ru', 'es'))
