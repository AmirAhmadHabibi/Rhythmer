LETTERS = 'ابپتثجچحخدذرزژسشصضطضعغفقکگلمنوهیيئءؤأإةۀ'
LONG_VOWELS = ['ا', 'ی', 'و']
SAKEN = 'ْ'
FATHEH = 'َ'
KASREH = 'ِ'
ZAMMEH = 'ُ'
EROB = [SAKEN, FATHEH, KASREH, ZAMMEH]
SHORT_VOWELS = [FATHEH, KASREH, ZAMMEH]
VOWELS = LONG_VOWELS + SHORT_VOWELS


# be and beh cases
# first letter should have vowel
# kasreh ezafeh

class Wordie:
    def __init__(self, text):
        self.text = text
        self.text = self.text.replace('اً', 'ن')
        self.text = self.text.replace('ي', 'ی')
        self.text = self.text.replace('آ', 'ئا')
        self.text_vowel = set()
        self.hejas = dict()

    def add_pronunciation(self, input_prn, dictionary):
        if dictionary == 'dehkhoda':
            # extract the consonant vowel pairs out of the raw formula
            prn_list = [[]]
            list_index = 0  # in case of seeing / this index would be added
            consonant = None
            input_prn = input_prn.replace('\/', '-')
            input_prn = input_prn.replace('ي', 'ی')
            input_prn = input_prn.replace('ً', 'َ')
            input_prn = input_prn.replace('آ', 'ئا')
            for c in input_prn:
                if c == ' ':
                    continue
                # the case of a regular consonant
                elif consonant is None and c in LETTERS:
                    consonant = c
                # regular vowel
                elif c in VOWELS or c == SAKEN:
                    vowel = c
                    if consonant is None:
                        print('[W] What is this vowel doing here? \tw:' + self.text + '\tp: ' + input_prn + '\tc: ' + c)
                        continue
                    prn_list[list_index].append((consonant, vowel))
                    consonant = None
                # a new group
                elif c == '-':
                    # TODO: partial and complete differences seem to be not distinguishable!! e.g. نخستین - سخی
                    if consonant is not None:
                        prn_list[list_index].append((consonant, ''))
                    consonant = None
                    list_index += 1
                    prn_list.append([])
                # the case of Tashdeed and some other case
                elif c in LETTERS:
                    if c == consonant:  # Thashdeed
                        prn_list[list_index].append((consonant, SAKEN))
                    else:
                        print('[W] This seems weird \tw:' + self.text + '\tp: ' + input_prn + '\tc: ' + c)
                        prn_list[list_index].append((consonant, ''))
                    consonant = c
                # otherwise
                else:
                    raise Exception('What is this char? \tw:' + self.text + '--' + input_prn + '--' + c)
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
                        # the case of semi Tashdeeds on ی
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

                # TODO: maybe check for partials here

                # print(dictionary, ':\t in[', input_prn, ']\tout [', prn_word, ']')

        elif dictionary == 'moein':
            # TODO
            pass
        elif dictionary == 'amid':
            # TODO
            pass

    def build_hejas(self):
        print(self.text)
        for wrd in self.text_vowel:
            try:
                heja_list = []
                hj = ''
                state = 0
                for i in range(len(wrd)):
                    hj += wrd[i]
                    if state == 0:
                        if wrd[i] in LETTERS:
                            state = 1
                        else:
                            raise Exception('[E] Bad word!', wrd)
                    elif state == 1:
                        if wrd[i] in VOWELS:
                            # lookahead
                            if i + 2 < len(wrd) and wrd[i + 1] in LETTERS and wrd[i + 2] in VOWELS:
                                state = 0
                                heja_list.append(hj)
                                hj = ''
                            else:
                                state = 2
                        else:
                            raise Exception('[E] Bad word!', wrd)
                    elif state == 2:
                        if wrd[i] in LETTERS:
                            # lookahead
                            if i + 2 < len(wrd) and wrd[i + 1] in LETTERS and wrd[i + 2] in VOWELS:
                                state = 0
                                heja_list.append(hj)
                                hj = ''
                            else:
                                state = 3
                        else:
                            raise Exception('[E] Bad word!', wrd)
                    elif state == 3:
                        if wrd[i] in LETTERS:
                            # lookahead
                            if i + 2 < len(wrd) and wrd[i + 1] in LETTERS and wrd[i + 2] in VOWELS:
                                state = 0
                                heja_list.append(hj)
                                hj = ''
                            else:
                                state = 3
                        elif wrd[i] == SAKEN:
                            # lookahead
                            if i + 2 < len(wrd) and wrd[i + 1] in LETTERS and wrd[i + 2] in VOWELS:
                                state = 0
                                heja_list.append(hj)
                                hj = ''
                            else:
                                state = 4
                        else:
                            raise Exception('[E] Bad word!', wrd)
                    elif state == 4:
                        if wrd[i] in LETTERS:
                            # lookahead
                            if i + 2 < len(wrd) and wrd[i + 1] in LETTERS and wrd[i + 2] in VOWELS:
                                state = 0
                                heja_list.append(hj)
                                hj = ''
                            else:
                                state = 3
                        else:
                            raise Exception('[E] Bad word!', wrd)
                if hj != '':
                    heja_list.append(hj)

                print(wrd, heja_list)
                self.hejas[wrd] = heja_list
            except Exception as e:
                print(e)
        print('------')

    


class Heja:
    pass
