#Jakub Ambroz
#01.12.2020
#RPH - uloha SPAM FILTER
#krok1: cteni dict ze souboru a zapis dict do souboru

def read_classification_from_file(file):
    my_dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            p = line.strip().split()
            if(len(p)>0):
                my_dict[p[0]] = p[1]
    return my_dict

def write_dict_to_file(file, my_dict):
    with open(file, 'w', encoding='utf-8')as f:
        for x in my_dict:
            f.write(x + " " + my_dict[x] + "\n")



if __name__ == "__main__":
    print(read_classification_from_file("spam-data-12-s75-h25/1/!truth.txt"))
    write_dict_to_file(read_classification_from_file("!prediction.txt","spam-data-12-s75-h25/1/!truth.txt"))