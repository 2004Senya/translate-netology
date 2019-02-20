import requests

ID = '7faae2f7.5c6d5ef7.175a1be3-0-0'
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

        if to_lang == '':
          to_lang = 'ru'

        response = requests.get(URL, params=params)
        json_ = response.json()

        with open(save, 'wb') as f:
            f.write(''.join(json_['text']))
        
        return 'saved'
  
print(translate_it('ES.txt', 'ES-R.txt', '', 'es'))
