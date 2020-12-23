#Jakub Ambroz
#01.12.2020
#RPH - uloha SPAM FILTER
#krok2: Corpus, going through emails
import os
class Corpus():
    """
    ambrojak Corpus
    """
    def __init__(self, path_to_emails):
        """
        vytvoreni korpusu obalujiciho emaily
        """
        self.path = path_to_emails
    def emails(self):
        """
        Generator for reading email, yields filename and its contents
        """
        file_list = os.listdir(self.path)
        for file in file_list:
            if(file[0]!='!'):
                yield file, open(os.path.join(self.path, file), 'r').read()

if __name__ == "__main__":
    c = Corpus("spam-data-12-s75-h25/1")
    count = 0
    for fname, body in c.emails():
        #print(fname)
        #print(body)
        #print("-------------------------")
        count+=1
    print('Finished: ', count, 'files processed.')