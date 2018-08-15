import requests
from wordie import Wordie


def send_request(word='سلام', dictionaries='dehkhoda'):
    try:
        # TODO: verbs and compounds
        print('-------')
        print(word)
        response = requests.get(
            url="http://api.vajehyab.com/v3/search",
            params={
                "token": "26950.1yq8LLtXqUIfJj070qK6qQtWVe50ioikWIsItVFU",
                "q": word,
                "type": "exact",
                "filter": dictionaries,
            },
        )

        # "filter": "dehkhoda,moein,amid",
        # print('Response HTTP Status Code: {status_code}'.format(status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(content=response.content))
        resp = str(response.content, encoding='utf-8')
        resp = resp.replace('true', 'True')
        resp = resp.replace('null', 'None')
        resp = eval(resp)
        wordie = Wordie(word)
        for res in resp['data']['results']:
            if res['id'].startswith('dehkhoda'):
                pron = res['text'].partition('[')[2].partition(']')[0]
                pron = ''.join(pron.split())
                try:
                    wordie.add_pronunciation(pron, 'dehkhoda')
                except Exception as e:
                    print(e)
            elif res['id'].startswith('moein'):
                pron = res['text'].partition('(')[2].partition(')')[0]
                try:
                    wordie.add_pronunciation(pron, 'moein')
                except Exception as e:
                    print(e)
            elif res['id'].startswith('amid'):
                try:
                    wordie.add_pronunciation(res['pron'], 'amid')
                except Exception as e:
                    print(e)
        return wordie
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# send_request(word='کتف', dictionaries='moein,amid')
# send_request(word='کتف', dictionaries='dehkhoda')
# # send_request(word='دروازه بان', dictionaries='moein,amid')
# send_request(word='دروازه بان', dictionaries='dehkhoda')
# # send_request(word='قطعاً', dictionaries='moein,amid')
# send_request(word='قطعاً', dictionaries='dehkhoda')
# # send_request(word='کرک', dictionaries='moein,amid')
# send_request(word='کرک', dictionaries='dehkhoda')
# # send_request(word='ابر', dictionaries='moein,amid')
send_request(word='ابر', dictionaries='dehkhoda')
# # send_request(word='الاکلنگ', dictionaries='moein,amid')
# send_request(word='الاکلنگ', dictionaries='dehkhoda')
# # send_request(word='فعالیت', dictionaries='moein,amid')
# send_request(word='فعالیت', dictionaries='dehkhoda')
# send_request(word='نیت', dictionaries='dehkhoda')
# send_request(word='تهنیت', dictionaries='dehkhoda')
