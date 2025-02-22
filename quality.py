# Jakub Ambroz
# 02.12.2020
# RPH - uloha SPAM FILTER
# krok3: quality calculation

import os
import utils
from confmat import BinaryConfusionMatrix as BCM


def compute_quality_for_corpus(corpus_dir):
    truth_dict = utils.read_classification_from_file(
        os.path.join(corpus_dir, "!truth.txt"))
    pred_dict = utils.read_classification_from_file(
        os.path.join(corpus_dir, "!prediction.txt"))
    cm = BCM(pos_tag="SPAM", neg_tag="OK")
    cm.compute_from_dicts(truth_dict, pred_dict)
    print("tp: " + str(cm.as_dict()['tp']))
    print("tn: " + str(cm.as_dict()['tn']))
    print("fp: " + str(cm.as_dict()['fp']))
    print("fn: " + str(cm.as_dict()['fn']))
    return quality_score(cm.as_dict()['tp'], cm.as_dict()['tn'], cm.as_dict()['fp'], cm.as_dict()['fn'])


def quality_score(tp, tn, fp, fn):
    return (tp+tn)/(tp+tn+10*fp+fn)


if __name__ == "__main__":
    print(compute_quality_for_corpus("my_data/sub/test"))
