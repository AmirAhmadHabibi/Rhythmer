letters = 'آابپتثجچحخدذرزژسشصضطضعغفقکگلمنوهیيئءؤأإةۀ'
long_vowels = 'ایيو'
short_vowels = 'َ ُ ِ ْ'


# َ ُ ِ ْ
# tanveens
# tashdeed
# be and beh cases
# first letter should have vowel
# kasreh ezafeh

class Wordie:
    def __init__(self, text):
        self.text = text
        self.text = self.text.replace('اً', 'ن')
        self.text_vowel = set()

    def add_pronunciation(self, prn, dictionary):
        if dictionary == 'dehkhoda':
            # extract the consonent vowel pairs out of the raw formula
            prn_list = [[]]
            list_index = 0  # in case of seeng / this index would be added
            consonent = None
            prn = prn.replace('\/', '-')
            prn = prn.replace('ً', 'َ')
            for c in prn:
                if c == ' ':
                    continue
                elif consonent is None and c in letters:
                    consonent = c
                elif c in short_vowels or c in long_vowels:
                    vowel = c
                    if consonent is None:
                        raise Exception('What is this vowel doing here? ' + self.text + '--' + prn + '--' + c)
                    prn_list[list_index].append((consonent, vowel))
                    consonent = None
                elif c == '-':
                    list_index += 1
                    prn_list.append([])
                    consonent = None
                elif c in letters:
                    prn_list[list_index].append((consonent, 'ْ'))
                    consonent = c
                else:
                    raise Exception('What is this char? ' + self.text + '--' + prn + '--' + c)
            if consonent is not None:
                prn_list[list_index].append((consonent, 'ْ'))

            # create text with vowels out of the extracted pairs of consonent vowels
            for pair_list in prn_list:
                prn_word = ''
                pair_index = 0
                for i in range(len(self.text)):
                    if pair_index < len(pair_list) and self.text[i] == pair_list[pair_index][0]:
                        if pair_index + 1 < len(pair_list) and \
                                pair_list[pair_index][1] == 'ی' and pair_list[pair_index + 1][0] == 'ی':
                            prn_word += pair_list[pair_index][0] + pair_list[pair_index][1]
                        elif pair_list[pair_index][1] != 'ْ':
                            if pair_list[pair_index][1] not in long_vowels:
                                prn_word += pair_list[pair_index][0] + pair_list[pair_index][1]
                            else:
                                prn_word += pair_list[pair_index][0]
                        elif pair_index + 1 < len(pair_list) and \
                                pair_list[pair_index][0] == pair_list[pair_index + 1][0]:  # the case of Tashdeed I hope
                            prn_word += pair_list[pair_index][0]
                            if pair_list[pair_index + 1][1] not in long_vowels:
                                prn_word += pair_list[pair_index + 1][0] + pair_list[pair_index + 1][1]
                            else:
                                prn_word += pair_list[pair_index + 1][0]
                            pair_index += 1
                        else:
                            prn_word += pair_list[pair_index][0]
                        pair_index += 1
                    else:
                        prn_word += self.text[i]
                prn_word = prn_word.replace('ْ', '')
                self.text_vowel.add(prn_word)
                print(dictionary, ':\t', prn, '|', prn_word, '|')
        elif dictionary == 'moein':
            # TODO
            pass
        elif dictionary == 'amid':
            # TODO
            pass

    def build_hejas(self):
        pass


class Heja:
    pass
