import argparse
import pickle
import numpy as np
from class_model import Model

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--model')
    parser.add_argument('--prefix', default = None)
    parser.add_argument('--length')

    args = parser.parse_args()

    with open(args.model, 'rb') as f:
        ngrams = pickle.load(f)

    pref = args.prefix

    if pref == None:
        pref = ngrams.keys()[np.random.choice(len(ngrams))]

    model = Model(len(list(ngrams.keys())[0].split()), ngrams)

    print(model.generate(pref, int(args.length)))
