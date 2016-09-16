# coding:utf-8
import codecs
import os
import ConfigParser


class WordDictionary(object):
    """
        use to create chinese word dictionary
    """
    def __init__(self):
        self.punctuation_mark = []
        self.read_punctuation()

        self.key_dictionary = dict()
        self.text_set = list()
        config_read = ConfigParser.ConfigParser()
        config_read.read("conf/corpus.conf")
        self.path = config_read.get("corpus", "corpus_dir")

        self.read_file()

        for passage in self.text_set:
            self.setup_key_dictionary(passage)

    def read_punctuation(self):
        file_open = codecs.open("Chinese_punctuation.txt", 'r', 'utf-8')
        punctuation_set = file_open.readlines()
        for punctuation in punctuation_set:
            self.punctuation_mark.append(punctuation[0])

    def read_file(self):
        file_set = os.listdir(self.path)
        for file_name in file_set:
            file_open = codecs.open(self.path + '/' + file_name, 'r', 'utf-8')
            article = file_open.readlines()
            self.text_set += article

    def setup_key_dictionary(self, text):
        is_start = False
        for i in range(len(text) - 1):
            if text[i] in self.punctuation_mark:
                is_start = False
            else:
                if is_start:
                    key_tail = text[i]
                    if key_head not in self.key_dictionary:
                        self.key_dictionary[key_head] = dict()
                        self.key_dictionary[key_head][key_tail] = 1
                    else:
                        if key_tail not in self.key_dictionary[key_head]:
                            self.key_dictionary[key_head][key_tail] = 1
                        else:
                            self.key_dictionary[key_head][key_tail] += 1
                    key_head = key_tail
                else:
                    key_head = text[i]
                    is_start = True


if __name__ == '__main__':
    my_word_dictionary = WordDictionary()
