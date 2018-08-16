import pickle

from wordie import Wordie


def make_wordies(words):
    with open('./res/dictionary.pkl', 'rb') as infile:
        dictionary = pickle.load(infile)
    if words is None:
        words = dictionary.keys()

    for word in words:
        try:
            meanings = dictionary[word]
        except KeyError as ke:
            print(ke)
            continue
        wordie = Wordie(word)
        for res in meanings:
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


make_wordies(['سخی','شدت','ضدیت'])
# TODO: verbs and compounds
