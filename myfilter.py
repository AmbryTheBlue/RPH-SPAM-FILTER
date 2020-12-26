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
import trainingcorpus  # zatim k nicemu
import utils
import utils_cleaner as cleaner
import utils_analyzer as analyzer
from utils_email import array_from_mail


class MyFilter(basefilter.BaseFilter):
    """
    Bayessian classifier using word count, url/href count etc.
    """

    def __init__(self):
        pass

    def train(self, train_dir):
        file_dict = utils.read_classification_from_file(
            train_dir+"/!truth.txt")
        corp = corpus.Corpus(train_dir)
        spam_word_counter = Counter()
        ham_word_counter = Counter()
        all_word_counter = Counter()
        for fname, body in corp.emails():
            content = array_from_mail(body)[-1][1]
            non_html = cleaner.remove_html_tags(content)
            spaceless = cleaner.remove_white_space(non_html)
            clean = cleaner.remove_punctutation(spaceless)
            arr = cleaner.word_arr_from_string(clean)
            arr = cleaner.sync_capitalization_of_arr(arr)
            all_word_counter += Counter(arr)
            if(file_dict[fname] == "SPAM"):
                spam_word_counter += Counter(arr)
            else:
                ham_word_counter += Counter(arr)
        c_diff = spam_word_counter - ham_word_counter
        print(c_diff.most_common(50))
        print("--------------------")
        c_diff_my = analyzer.counter_difference(
            spam_word_counter, ham_word_counter, 200, 150)
        print(c_diff_my)

    def eval_mail(string):
        mail_array = array_from_mail(string)
        pass


if __name__ == "__main__":
    f = MyFilter()
    f.train("my_data/sub1/train")
