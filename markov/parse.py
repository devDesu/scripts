# -*- coding: utf-8 -*-
__author__ = 'Anton'
import re
from storage import Storage


class Parser:
    def __init__(self, store, sentence_split=['.', '!', '?', '...', '\n'], word_split=[' ', ',', ':', '—']):
        self.sentences = []
        self.storage = store
        self.word_split = word_split
        temp = '['+''.join(['\{}'.format(i) for i in sentence_split])+']'
        print(temp)
        self.sentence_split = re.compile(temp, flags=re.MULTILINE+re.UNICODE)
        temp = '['+''.join(['\{}'.format(i) for i in word_split])+']'
        print(temp)
        self.word_split = re.compile(temp, flags=re.UNICODE)

    def split_sentences(self, text):
        temp = self.sentence_split.split(text)
        for i in temp:
            if len(i) > 1:
                self.sentences.append('START_TOKEN ' + i.strip() + ' END_TOKEN')

    # debug method
    def get_sentences(self):
        return self.sentences

    def build_tree(self):
        for k in self.sentences:
            temp = self.word_split.split(k)
            temp = [i for i in temp if i]
            temp[1] = temp[1].lower()
            for i in range(0, len(temp)-1):
                self.storage.add_pair((temp[i], temp[i+1],))