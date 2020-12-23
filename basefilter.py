#Jakub Ambroz
#03.12.2020
#RPH - uloha SPAM FILTER
#krok4: base filter
import utils
import corpus
import os
class BaseFilter():
    """
    Basic filter for RPH, SPAM filter
    """
    def __init__(self):
        """
        Initialization without parameters
        """
        pass
    
    def train(self, corpus_test_dir):
        pass

    def test(self, corpus_test_dir):
        self.corpus = corpus.Corpus(corpus_test_dir)
        self.dict = self.create_dict()
        file = "!predictions.txt"
        utils.write_dict_to_file(os.path.join(corpus_test_dir, file),self.dict)
    
    def crete_dict(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError("Base filter does not evaluate")
