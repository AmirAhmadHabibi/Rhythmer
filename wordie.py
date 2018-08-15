letters = 'آابپتثجچحخدذرزژسشصضطضعغفقکگلمنوهیيئءؤأإةۀ'
long_vowels = 'ایيو'
short_vowels = 'َ ُ ِ ْ'


# َ ُ ِ ْ
# tanveens
# tashdeed
# be and beh cases
# first letter should have vowel

class Wordie:
    def __init__(self, text):
        self.text = text
        self.pronunciations = set()

    def add_pronunciation(self, prn, dictionary):
        if dictionary == 'dehkhoda' or dictionary == 'moein':
            # extract the consonent vowel pairs out of the raw formula
            prn_list = [[]]
            list_index = 0  # in case of seeng / this index would be added
            consonent = None
            prn = prn.replace('\/', '-')
            for c in prn:
                if c == ' ':
                    continue
                elif c in letters:
                    consonent = c
                elif c in short_vowels:
                    vowel = c
                    if consonent is None:
                        raise Exception('What is this vowel doing here? ' + self.text + '--' + prn + '--' + c)
                    if vowel != 'ْ':
                        prn_list[list_index].append((consonent, vowel))
                    consonent = None
                elif c == '-':
                    list_index += 1
                    prn_list.append([])
                    consonent = None
                else:
                    raise Exception('What is this char? ' + self.text + '--' + prn + '--' + c)

            # create pronunciations out of the extracted pairs
            for pair_list in prn_list:
                prn_word = ''
                pair_index = 0
                for i in range(len(self.text)):
                    if pair_index < len(pair_list) and self.text[i] == pair_list[pair_index][0]:
                        prn_word += pair_list[pair_index][0] + pair_list[pair_index][1]
                        pair_index += 1
                    else:
                        prn_word += self.text[i]
                self.pronunciations.add(prn_word)
                print(dictionary, ':\t', prn, '|', prn_word, '|')
        elif dictionary == 'amid':
            # TODO
            pass


class Heja:
    pass
