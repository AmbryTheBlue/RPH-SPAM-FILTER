# Jakub Ambroz
# 01.12.2020
# RPH - uloha SPAM FILTER
# krok3: Binary confusion matrix

class BinaryConfusionMatrix():
    """
    For counting true/false postives/negatives
    """

    def __init__(self, pos_tag="SPAM", neg_tag="OK"):
        self.pos_tag = pos_tag
        self.neg_tag = neg_tag
        self.q_dict = {'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0}

    def as_dict(self):
        return self.q_dict

    def update(self, truth, prediction):
        if truth == self.pos_tag:
            if prediction == self.pos_tag:
                self.q_dict['tp'] += 1
            elif prediction == self.neg_tag:
                self.q_dict['fn'] += 1
            else:
                raise ValueError('Error: incorrect parametr for update function: %s\n Expected %s or %s'%(prediction, self.pos_tag, self.neg_tag))
        elif truth == self.neg_tag:
            if prediction == self.neg_tag:
                self.q_dict['tn'] += 1
            elif prediction == self.pos_tag:
                self.q_dict['fp'] += 1
            else:
                raise ValueError("Error: incorrect parametr for update function: {}\n Expected {} or {}".format(prediction, self.pos_tag, self.neg_tag))
        else:
            raise ValueError("Error: incorrect parametr for update function: {}\n Expected {} or {}".format(truth, self.pos_tag, self.neg_tag))
    
    def compute_from_dicts(self, truth_dict, pred_dict):
        for key in pred_dict:
            if key in truth_dict:
                self.update(truth_dict[key], pred_dict[key])

if __name__ == "__main__":
    print("----------cm1-----------")
    cm1 = BinaryConfusionMatrix(pos_tag=True, neg_tag=False)
    print(cm1.as_dict())
    cm1.update(True, True)
    print(cm1.as_dict())
    print("--------cm2---------")
    truth_dict = {'em1': 'SPAM', 'em2': 'SPAM', 'em3': 'OK', 'em4':'OK'}
    pred_dict = {'em1': 'SPAM', 'em2': 'OK', 'em3': 'OK', 'em4':'SPAM'}
    cm2 = BinaryConfusionMatrix(pos_tag='SPAM', neg_tag='OK')
    cm2.compute_from_dicts(truth_dict, pred_dict)
    print(cm2.as_dict())
