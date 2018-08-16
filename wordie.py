LETTERS = 'آابپتثجچحخدذرزژسشصضطضعغفقکگلمنوهیيئءؤأإةۀ'
LONG_VOWELS = 'ایو'
SAKEN = 'ْ'
FATHEH = 'َ'
KASREH = 'ِ'
ZAMMEH = 'ُ'
SHORT_VOWELS = [SAKEN, FATHEH, KASREH, ZAMMEH]


# be and beh cases
# first letter should have vowel
# kasreh ezafeh

class Wordie:
    def __init__(self, text):
        self.text = text
        self.text = self.text.replace('اً', 'ن')
        self.text = self.text.replace('ي', 'ی')
        self.text_vowel = set()

    def add_pronunciation(self, prn, dictionary):
        if dictionary == 'dehkhoda':
            # extract the consonant vowel pairs out of the raw formula
            prn_list = [[]]
            list_index = 0  # in case of seeng / this index would be added
            consonant = None
            prn = prn.replace('\/', '-')
            prn = prn.replace('ي', 'ی')
            prn = prn.replace('ً', 'َ')
            for c in prn:
                if c == ' ':
                    continue
                # the case of a regular consonant
                elif consonant is None and c in LETTERS:
                    consonant = c
                # regular vowel
                elif c in SHORT_VOWELS or c in LONG_VOWELS:
                    vowel = c
                    if consonant is None:
                        print('[W] What is this vowel doing here? \tw:' + self.text + '\tp: ' + prn + '\tc: ' + c)
                        continue
                    prn_list[list_index].append((consonant, vowel))
                    consonant = None
                # a new group
                elif c == '-':
                    # TODO: partial and complete differences seem to be not distinguishable!! e.g. کرک - سخی
                    if consonant is not None:
                        prn_list[list_index].append((consonant, ''))
                    consonant = None
                    list_index += 1
                    prn_list.append([])
                # the case of Tashdeed and some other case
                elif c in LETTERS:
                    if c == consonant: # Thashdeed
                        prn_list[list_index].append((consonant, SAKEN))
                    else:
                        print('[W] This seems weird', prn)
                        prn_list[list_index].append((consonant, ''))
                    consonant = c
                # otherwise
                else:
                    raise Exception('What is this char? \tw:' + self.text + '--' + prn + '--' + c)
            if consonant is not None:
                prn_list[list_index].append((consonant, ''))

            # print(prn_list)
            # create text with vowels out of the extracted pairs of consonant vowels
            for pair_list in prn_list:
                prn_word = ''
                pair_index = 0
                text_index = 0
                while text_index < len(self.text):
                    curr_pair = pair_list[pair_index] if pair_index < len(pair_list) else None
                    next_pair = pair_list[pair_index + 1] if pair_index + 1 < len(pair_list) else None

                    # if there is a cons-vow pair for this character
                    if curr_pair is not None and self.text[text_index] == curr_pair[0]:
                        # the case of semi tashdeeds on ی
                        if next_pair is not None and curr_pair[1] == 'ی' and next_pair[0] == 'ی':
                            prn_word += curr_pair[0] + curr_pair[1]
                        # the case of Tashdeed I hope
                        elif curr_pair[1] == SAKEN and next_pair is not None and curr_pair[0] == next_pair[0]:
                            # add the consonant with Saken
                            prn_word += curr_pair[0] + curr_pair[1]
                            # remain on the same char in the base text
                            text_index -= 1
                        # the case of having long vowels in phonetics
                        elif curr_pair[1] in LONG_VOWELS:
                            prn_word += curr_pair[0]
                        # other normal cases
                        else:
                            prn_word += curr_pair[0] + curr_pair[1]
                        pair_index += 1

                    # if there are no cons-vow pairs for this character
                    else:
                        prn_word += self.text[text_index]
                    text_index += 1

                # remove the Sakens
                # prn_word = prn_word.replace(SAKEN, '')
                # add the voweled word to the set of all pronunciations
                self.text_vowel.add(prn_word)

                print(dictionary, ':\t in[', prn, ']\tout [', prn_word, ']')

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
