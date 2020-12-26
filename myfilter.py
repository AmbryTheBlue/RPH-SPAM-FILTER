# Katerina Kucerova, Jakub Ambroz
# RPH - SPAM_FILTER
# https://cw.fel.cvut.cz/wiki/courses/b4b33rph/cviceni/spam/start

# Full source code:
# Main: https://gitlab.fel.cvut.cz/ambrojak/rph-spam-filter
# Backup: https://github.com/AmbryTheBlue/RPH-SPAM-FILTER

import os
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

    def train(self, corpus_test_dir):
        pass

    def eval_mail(string):
        mail_array = array_from_mail(string)
        pass


if __name__ == "__main__":
    os.system("echo Ahoj!")
