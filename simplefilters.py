# Jakub Ambroz
# 03.12.2020
# RPH - uloha SPAM FILTER
# krok4: base filter

import basefilter
from random import randint


class NaiveFilter(basefilter.BaseFilter):
    def create_dict(self):
        my_dict = {}
        for fname, fbody in self.corpus.emails():
            my_dict[fname] = "OK"
        return my_dict


class ParanoidFilter(basefilter.BaseFilter):
    def create_dict(self):
        my_dict = {}
        for fname, fbody in self.corpus.emails():
            my_dict[fname] = "SPAM"
        return my_dict


class RadnomFilter(basefilter.BaseFilter):
    def create_dict(self):
        my_dict = {}
        for fname, fbody in self.corpus.emails():
            if randint(0, 2) == 1:
                my_dict[fname] = "OK"
            else:
                my_dict[fname] = "SPAM"
        return my_dict


if __name__ == "__main__":
    import quality
    n = NaiveFilter()
    par = ParanoidFilter()
    ran = RadnomFilter()
    path = "spam-data-12-s75-h25/1"
    n.test(path)
    print(quality.compute_quality_for_corpus(path))
    # par.test(path)
    print(quality.compute_quality_for_corpus(path))
    # ran.test(path)
    print(quality.compute_quality_for_corpus(path))
