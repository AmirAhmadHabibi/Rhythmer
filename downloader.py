import os
import pickle
import requests

# MY_TOKEN = "26950.t3scZdG7Xpw4dpeUhQVIifShsP2rCwS5AlizyYHw"
MY_TOKEN = '61378.IrcnbCjqvwdGdoAmklUJGUbmBpY5jdI1EUoQwIh2'


def send_request(word, dictionaries='dehkhoda,moein,amid'):
    try:
        print(':::', word, ':::')
        response = requests.get(
            url="http://api.vajehyab.com/v3/search",
            params={
                "token": MY_TOKEN,
                "q": word,
                "type": "exact",
                "filter": dictionaries,
                "rows": "50",
            },
        )
        resp = str(response.content, encoding='utf-8')
        resp = resp.replace('true', 'True')
        resp = resp.replace('false', 'False')
        resp = resp.replace('null', 'None')
        resp = eval(resp)
        if not resp['response']['status']:
            print(resp)
            raise Exception('[E] Come back later! Vajehyab doesn\'t feel like doing it.')
        return resp['data']['results']
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    return []


def add_to_dictionary(new_words):
    # open the dictionary
    if os.path.isfile('./res/dictionary.pkl'):
        with open('./res/dictionary.pkl', 'rb') as infile:
            dictionary = pickle.load(infile)
    else:
        dictionary = dict()

    # add the new words
    for word in new_words:
        if word in dictionary:
            print('[W]', word, 'is already in the dictionary!')
            continue
        # making separate requests for dehkhoda and the others due to the limit of max 12 entries in the response
        meanings = send_request(word, dictionaries='dehkhoda,moein,amid')
        # meanings = send_request(word, dictionaries='dehkhoda')
        # meanings += send_request(word, dictionaries='moein,amid')
        if not meanings:
            print('[W] both responses for', word, 'were empty!')
            continue
        dictionary[word] = meanings

    # save the dictionary
    with open('./res/dictionary.pkl', 'wb') as outfile:
        pickle.dump(dictionary, outfile)
    print('new words added.')


input_words = ['کتف', 'دروازه بان', 'قطعاً', 'کرک', 'ابر', 'الاکلنگ', 'فعالیت', 'نیت', 'تهنیت', 'اهمیت', 'کش',
               'جبار', 'به', 'سخی', 'شدت', 'ضدیت', 'قرآن', 'فناوری', 'سرآمد', 'پیام', 'دولت']
add_to_dictionary(input_words)
