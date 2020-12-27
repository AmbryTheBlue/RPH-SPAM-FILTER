import utils
import os
import random


def random_subset(number, name, percantage_used):
    path = "spam-data-12-s75-h25"
    dict_train = {}
    dict_test = {}
    save_path = "my_data/"
    dictionary = utils.read_classification_from_file(
        path+"/"+ str(number) +"/!truth.txt")
    save_path += name
    print("Removing '" + save_path + "' if exists")
    os.system("rm -rf " + save_path)
    print("Creating appropriate directories.")
    os.system("mkdir " + save_path)
    os.system("mkdir " + save_path+"/train/")
    os.system("mkdir " + save_path+"/test/")
    print("Saving file into data set:")
    for name, status in dictionary.items():
        if (random.randint(1, 100) <= percantage_used): # percantage portion that is used for training
            dict_train[name] = status
            #print("Train: " + name + " : " + status)
            os.system("cp " + path + "/" + str(number) + "/" +
                      name + " " + save_path+"/train/"+name)
        else:
            dict_test[name] = status
            #print("Test: " + name + " : " + status)
            os.system("cp " + path + "/" + str(number) + "/" +
                      name + " " + save_path+"/test/"+name)
    utils.write_dict_to_file(save_path+"/train/!truth.txt", dict_train)
    utils.write_dict_to_file(save_path+"/test/!truth.txt", dict_test)
    print("Succcess!\n Subsets created:\n" +
          save_path+"/train/\n"+save_path+"/test/")
    print("Used dataset: " + str(number))
    print("Used portion for trianing " + str(percantage_used) + "% ")


if __name__ == "__main__":
    random_subset(1, "sub", 10)
