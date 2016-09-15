# coding:utf-8
import codecs


class WordDictionary(object):
    def __init__(self):
        self.key_dictionary = dict()
        self.text_set = list()
        self.read_file()
        self.char_ignore = [
            '，', '。', '：'
        ]
        for article in self.text_set:
            for passage in article:
                self.setup_key_dictionary(passage)

    def read_file(self):
        file_set = list()
        for i in range(1, 2):
            file_set.append('text' + str(i) + '.txt')
        for item in file_set:
            print(item)
            file_open = codecs.open('data/' + item, 'r', 'utf-8')
            new_text = file_open.readlines()
            self.text_set.append(new_text)

    def setup_key_dictionary(self, text):
        key_head = text[0]
        for i in range(1, len(text)):
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

if __name__ == '__main__':
    my_word_dictionary = WordDictionary()
    for key in my_word_dictionary.key_dictionary.keys():
        print(key, my_word_dictionary.key_dictionary[key])
