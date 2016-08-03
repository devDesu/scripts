__author__ = 'Anton'
import random


class Generator:
    def __init__(self, st):
        self.storage = st

    def weighted_next_word(self, word):
        temp = self.storage.get_word(word)
        total = sum(weight for item, weight in temp.items())
        r = random.uniform(0, total)
        upto = 0
        for item, weight in temp.items():
            # print(weight+upto)
            if upto + weight >= r:
                return item
            upto += weight
        assert False, "Shouldn't get here"

    def generate_sentence(self):
        sentence = ['START_TOKEN']
        while True:
            word = self.weighted_next_word(sentence[len(sentence)-1])
            sentence.append(word)
            if word == 'END_TOKEN':
                break
        temp = ' '.join(sentence)[len('START_TOKEN '):-len(' END_TOKEN')]+'.'
        return temp[0].upper()+temp[1:]