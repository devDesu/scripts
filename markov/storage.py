# -*- coding: utf-8 -*-
class Storage:
    def __init__(self, name=None):
        self.words = {}
        # words is a list with structure {word1:{nextWord1: n, nextWord2: k}, word2:{...}}
        if not name:
            self.name = 'tree.data'
        else:
            self.name = name

    def save_file(self):
        f = open(self.name, 'w', encoding='utf-8')
        for key, value in self.words.items():
            f.write('{}*&{}\n'.format(key, value))
        f.close()

    def read_file(self):
        f = open(self.name, 'r', encoding='utf-8')
        temp = [i for i in f.readlines() if i]
        for i in temp:
            key, value = i.split('*&')
            self.words[key] = eval(value)
        f.close()

    def add_pair(self, word_tuple, weight=1):
        if word_tuple[0] in self.words:
            if word_tuple[1] in self.words[word_tuple[0]]:
                self.words[word_tuple[0]][word_tuple[1]] += weight
            else:
                self.words[word_tuple[0]][word_tuple[1]] = weight
        else:
            self.words[word_tuple[0]] = {word_tuple[1]: weight}

    # debug
    def output(self):
        print(self.words)

    def get_word(self, word):
        return self.words[word]