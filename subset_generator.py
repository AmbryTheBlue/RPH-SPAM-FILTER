import utils
import os
import random

path = "spam-data-12-s75-h25"
dictionary1 =  utils.read_classification_from_file(path+"/1/!truth.txt")
dictionary2 =  utils.read_classification_from_file(path+"/2/!truth.txt")
print(dictionary1)
print(dictionary2)
dict_train = {}
dict_test = {}

save_path = "my_data/sub1"
percantage_used = 50
for name, status in dictionary1.items():
    print(name + " : " + status)
    if (random.randint(1,100)>=50):
        dict_train[name] = status
        os.system("cp " + path + "/1/"+name + " " + save_path+"/train/"+name)
    else:
        dict_test[name] = status
        os.system("cp " + path + "/1/"+name + " " + save_path+"/test/"+name)

utils.write_dict_to_file(save_path+"/train/!truth.txt", dict_train)
utils.write_dict_to_file(save_path+"/test/!truth.txt", dict_test)