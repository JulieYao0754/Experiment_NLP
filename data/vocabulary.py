import os
import json
import logging
import pypinyin


class Vocabulary(object):
    def __init__(self, filename, corpus_path, max_word_length):
        """
        filename: the filename of vocabulary file
        corpus_path: the path of corpus folder.
            The source of corpus I use from is https://storage.googleapis.com/nlp_chinese_corpus/wiki_zh_2019.zip.
        max_word_length: maximum length of a world
        """
        self.dict_file = filename
        self.corpus_path = corpus_path
        self._word_to_id = {}
        self._id_to_word = []

    def build_dict(self):
        if os.path.exists(self.dict_file):
            logging.info('The file of word is already existed, load directly.')
            with open(self.dict_file) as f:
                idx = 0
                for line in f:
                    character = line.strip()
                    self._id_to_word.append(character)
                    self._word_to_id[character] = idx
                    idx += 1
        else:
            ''' structure of wiki_zh folder
             wiki_zh
                    |AA
                        |wiki_00
                        |wiki_01
                        |wiki_02
                        |...
                    |AB
                        |...
                    |...
            '''
            idx = 0
            memu = os.listdir(self.corpus_path)
            for directory in memu:
                cur_path = self.corpus_path + directory
                if os.path.isdir(cur_path):
                    data_list = os.listdir(cur_path)
                    for data_file in data_list:
                        with open(cur_path+'/'+data_file, 'r', encoding='UTF-8') as f:
                             for line in f:
                                 sentences = json.loads(line)['text']
                                 for character in sentences:
                                     if character not in self._word_to_id.keys():               
                                         self._word_to_id[character] = idx
                                         self._id_to_word.append(character)
                                         idx += 1
            with open(self.dict_file, 'w+', encoding='UTF-8') as f:
                for character in self._id_to_word:
                    f.write(character)
                    f.write('\n')
            f.close()
