import numpy as np


class Model(object):
    """class model"""

    def __init__(self, n, ngrams):
        self.n = n
        self.ngrams = ngrams


    def fit(self, text):
        """makes a dictionary of n-grams"""

        for i in range(len(text) - self.n):
            key = ' '.join(text[i:i + self.n])

            if key not in self.ngrams.keys():
                self.ngrams[key] = []

            self.ngrams[key].append(text[i + self.n])


    def generate(self, pref, length):
        """generates a text starting with the prefix"""

        cur_seq = pref
        list_seq, res = cur_seq.split(), []

        for i in range(self.n - 2):
            res.append(list_seq[i])

        list_key = self.ngrams.keys()

        for _ in range(length):
            if cur_seq not in list_key:
                cur_seq = ''

                for key in list_key:
                    if pref in key:
                        cur_seq = key
                        break

                if not len(cur_seq):
                    cur_seq = list_key[np.random.choice(len(list_key))]

            list_seq = cur_seq.split()

            res.append(list_seq[-1])

            new_cur_seq = ''

            for i in range(1, self.n):
                new_cur_seq += list_seq[i] + ' '

            new_cur_seq += self.ngrams[cur_seq][np.random.choice(len(self.ngrams[cur_seq]))]

            cur_seq = new_cur_seq
            list_seq = cur_seq.split()

        return ' '.join(res)
