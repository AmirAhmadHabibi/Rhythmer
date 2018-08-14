import requests

letters = 'آابپتثجچحخدذرزژسشصضطضعغفقکگلمنوهیيئءؤأإةۀ'
short_vowels = 'َُِْ'
long_vowels = 'ایيو'


# TODO check tanveens


def send_request(word='سلام'):
    try:
        response = requests.get(
            url="http://api.vajehyab.com/v3/search",
            params={
                "token": "26950.1yq8LLtXqUIfJj070qK6qQtWVe50ioikWIsItVFU",
                "q": word,
                "type": "exact",
                "filter": "dehkhoda,moein,amid",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(content=response.content))
        resp = str(response.content, encoding='utf-8')
        resp = resp.replace('true', 'True')
        resp = resp.replace('null', 'None')
        resp = eval(resp)
        for res in resp['data']['results']:
            if res['id'].startswith('dehkhoda'):
                phon = res['text'].partition('[')[2].partition(']')[0]
                phon = ''.join(phon.split())
                # TODO
            elif res['id'].startswith('moein'):
                phon = res['text'].partition('(')[2].partition(')')[0]
                # TODO
                pass
            elif res['id'].startswith('amid'):
                phon=res['pron']
                # TODO
                pass
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


send_request()
