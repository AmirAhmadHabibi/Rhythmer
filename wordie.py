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
            # extract the consonant vowel pairs out of the raw formula
            prn_list = [[]]
            list_index = 0  # in case of seeng / this index would be added
            consonant = None
            prn = prn.replace('\/', '-')
            prn = prn.replace('ً', 'َ')
            for c in prn:
                if c == ' ':
                    continue
                elif consonant is None and c in letters:
                    consonant = c
                elif c in short_vowels or c in long_vowels:
                    vowel = c
                    if consonant is None:
                        raise Exception('What is this vowel doing here? ' + self.text + '--' + prn + '--' + c)
                    prn_list[list_index].append((consonant, vowel))
                    consonant = None
                elif c == '-':
                    list_index += 1
                    prn_list.append([])
                    consonant = None
                elif c in letters:
                    prn_list[list_index].append((consonant, 'ْ'))
                    consonant = c
                else:
                    raise Exception('What is this char? ' + self.text + '--' + prn + '--' + c)
            if consonant is not None:
                prn_list[list_index].append((consonant, 'ْ'))

            # create text with vowels out of the extracted pairs of consonant vowels
            for pair_list in prn_list:
                prn_word = ''
                pair_index = 0
                for i in range(len(self.text)):
                    # if there is a cons-vow pair for this character
                    if pair_index < len(pair_list) and self.text[i] == pair_list[pair_index][0]:
                        # the case of semi tashdeeds on ی
                        if pair_index + 1 < len(pair_list) and \
                                pair_list[pair_index][1] == 'ی' and pair_list[pair_index + 1][0] == 'ی':
                            prn_word += pair_list[pair_index][0] + pair_list[pair_index][1]
                        # the case of Tashdeed I hope
                        elif pair_list[pair_index][1] == 'ْ' and pair_index + 1 < len(pair_list) and \
                                pair_list[pair_index][0] == pair_list[pair_index + 1][0]:
                            # add the consonant with Saken first
                            prn_word += pair_list[pair_index][0] + pair_list[pair_index][1]
                            # then add the second consonant with vowel
                            if pair_list[pair_index + 1][1] in long_vowels:
                                prn_word += pair_list[pair_index + 1][0]
                            else:
                                prn_word += pair_list[pair_index + 1][0] + pair_list[pair_index + 1][1]
                            pair_index += 1
                        # the case of having long vowels in phonetics
                        elif pair_list[pair_index][1] in long_vowels:
                            prn_word += pair_list[pair_index][0]
                        # other normal cases
                        else:
                            prn_word += pair_list[pair_index][0] + pair_list[pair_index][1]
                        pair_index += 1
                    # if there are no cons-vow pairs for this character
                    else:
                        prn_word += self.text[i]

                prn_word = prn_word.replace('ْ', '')
                # add the voweled word to the set of all pronunciations
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
