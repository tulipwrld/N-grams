import argparse
import re
import pickle
from class_model import Model


def to_line(s):
    return s.lower() + ' '

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--input-dir', default = None)
    parser.add_argument('--model')

    args = parser.parse_args()
    text = ''

    if args.input_dir == None:
        try:
            while True:
                text += to_line(input())
        except:
            pass
    else:
        with open(args.input_dir) as f:
            for line in f:
                text += to_line(line)

    text = re.sub(r'[^\w\s]', ' ', text).split()
    n = 2

    model = Model(n, {})
    model.fit(text)

    with open(args.model, 'wb') as f:
        pickle.dump(model.ngrams, f)
