# Katerina Kucerova, Jakub Ambroz
# RPH - SPAM_FILTER
# https://cw.fel.cvut.cz/wiki/courses/b4b33rph/cviceni/spam/start

# Full source code:
# Main: https://gitlab.fel.cvut.cz/ambrojak/rph-spam-filter
# Backup: https://github.com/AmbryTheBlue/RPH-SPAM-FILTER

import os
from collections import Counter
import basefilter
import corpus
import utils
import utils_cleaner as cleaner
import utils_analyzer as analyzer
from utils_email import array_from_mail


class MyFilter(basefilter.BaseFilter):
    """
    Ambroz, Kucerova. Filter counts word (or metadata) occurences in spam/ham train set.
    Then predicts if each word (/ metadata) in mail is more likely to be in spam or ham.
    If more spam words (and metadata) then ham predict the entire mail is spam
    """

    def __init__(self):
        self.trained = False
        #Using content
        self.spam_mail_quantity = 0
        self.ham_mail_quantity = 0
        self.spam_word_quantity = 0
        self.ham_word_quantity = 0
        self.spam_word_counter = Counter()
        self.ham_word_counter = Counter()
        self.all_word_counter = Counter()
        #Using metadata
        self.spam_meta_counter_dict = {}
        self.ham_meta_counter_dict = {}

    def train(self, train_dir):
        self.trained = True
        file_dict = utils.read_classification_from_file(
            train_dir+"/!truth.txt")
        corp = corpus.Corpus(train_dir)
        for fname, body in corp.emails():
            mail_data = array_from_mail(body)
            #Using metadata
            for i in range(len(mail_data)-1):
                key = mail_data[i][0]
                value = mail_data[i][1]
                if(file_dict[fname] == "SPAM"):
                    self.spam_meta_counter_dict[key] = self.spam_meta_counter_dict.get(key, Counter()) + Counter([value])
                else:
                    self.ham_meta_counter_dict[key] = self.ham_meta_counter_dict.get(key, Counter()) + Counter([value])

            #Using content
            content = mail_data[-1][1]
            non_html = cleaner.remove_html_tags(content)
            spaceless = cleaner.remove_white_space(non_html)
            clean = cleaner.remove_punctutation(spaceless)
            arr = cleaner.word_arr_from_string(clean)
            arr = cleaner.sync_capitalization_of_arr(arr)
            self.all_word_counter += Counter(arr)
            if(file_dict[fname] == "SPAM"):
                self.spam_mail_quantity += 1
                self.spam_word_quantity += len(arr)
                self.spam_word_counter += Counter(arr)
            else:
                self.ham_mail_quantity +=1
                self.ham_word_quantity += len(arr)
                self.ham_word_counter += Counter(arr)
        c_diff = self.spam_word_counter - self.ham_word_counter
        c_diff_my = analyzer.counter_difference(
            self.spam_word_counter, self.ham_word_counter, 200, 150)

    def create_dict(self):
        my_dict = {}
        for fname, fbody in self.corpus.emails():
            if self.eval_mail(fbody):
                my_dict[fname] = "SPAM"
            else:
                my_dict[fname] = "OK"
        return my_dict

    def eval_mail(self,string):
        mail_data = array_from_mail(string)
        content = mail_data[-1][1]
        href_frequency = analyzer.count_href(content)
        non_html = cleaner.remove_html_tags(content)
        spaceless = cleaner.remove_white_space(non_html)
        exclamation_mark_frequency  = analyzer.char_count("!",spaceless)
        dollar_frequency  = analyzer.char_count("$",spaceless)
        percent_frequency  = analyzer.char_count("%",spaceless)
        clean = cleaner.remove_punctutation(spaceless)
        arr = cleaner.word_arr_from_string(clean)
        capslock_frequency = analyzer.count_capslocked_words(arr)
        arr = cleaner.sync_capitalization_of_arr(arr)
        word_count = len(arr)
        
        #Eval by metadata:
        spam_meta_frequency = 0
        ham_meta_frequency = 0
        for i in range(len(mail_data)-1):
            key = mail_data[i][0]
            value = mail_data[i][1]
            spam_chance = self.spam_meta_counter_dict.get(key, Counter())[value] /self.spam_mail_quantity
            ham_chance = self.ham_meta_counter_dict.get(key, Counter())[value] / self.ham_mail_quantity
            if (spam_chance>ham_chance ):
                spam_meta_frequency += 1
            elif (spam_chance<ham_chance):
                ham_meta_frequency += 1

        #Eval by words
        spam_word_frequency = 0
        ham_word_frequency = 0
        for word in arr:
            spam_chance = self.spam_word_counter[word] /self.spam_word_quantity
            ham_chance = self.ham_word_counter[word] /self.ham_word_quantity
            if (spam_chance>ham_chance ):
                spam_word_frequency += 1
            elif (spam_chance<ham_chance):
                ham_word_frequency += 1
        if(spam_meta_frequency>=ham_meta_frequency and  spam_word_frequency>=ham_word_frequency):
            return True
        else:
            return False


if __name__ == "__main__":
    f = MyFilter()
    f.train("my_data/sub/train")
    f.test("my_data/sub/test")
    print("Success!")
