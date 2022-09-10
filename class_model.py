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

        for i in range(self.n - 1):
            res.append(list_seq[i])

        for _ in range(length):
            if cur_seq in self.ngrams.keys():
                res.append(list_seq[-1])

                new_cur_seq = ''

                for i in range(1, self.n):
                    new_cur_seq += list_seq[i] + ' '

                new_cur_seq += self.ngrams[cur_seq][np.random.choice(len(self.ngrams[cur_seq]))]

                cur_seq = new_cur_seq
                list_seq = cur_seq.split()
            else:
                break

        return ' '.join(res)
