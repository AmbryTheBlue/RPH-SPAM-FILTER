from collections import Counter


def count_href(array):
    words = array.lower().split()
    counter = 0
    for word in words:
        if ("href" in word):
            counter += 1
    return counter
    

def counter_from_array(array):
    # useless function, remains for compatibility
    c = Counter(array)
    return c


def counter_difference(c_spam, c_ham, limit_spam, limit_ham):
    spam_most = c_spam.most_common(limit_spam)
    ham_most = c_ham.most_common(limit_ham)
    i = 0
    while (i < len(spam_most)):
        intersection = False
        for el in ham_most:
            if(el[0] == spam_most[i][0]):
                #print(el[0])
                intersection = True
                break
        if(intersection):
            spam_most.pop(i)
        else:
            i += 1
    return spam_most


def char_count(char, txt):
    count = 0
    for c in txt:
        if(c == char):
            count += 1
    return count


def count_capslocked_words(array):
    count = 0
    for word in array:
        capitalized = 0
        for char in word:
            if (char.isupper()):
                capitalized += 1
            if(capitalized > 2):
                count += 1
                break
    return count


if __name__ == "__main__":
    from utils_email import array_from_mail
    from utils_cleaner import *

    def count_exclamation(txt):
        count = 0
        for char in txt:
            if char == '!':
                count += 1
        return count

    def count_percantage(txt):
        count = 0
        for char in txt:
            if char == '%':
                count += 1
        return count
    c1 = {}
    with open("spam-data-12-s75-h25/1/0001.bfc8d64d12b325ff385cca8d07b84288") as soubor:
        content = array_from_mail(soubor.read())[-1][1]
        # print(content)
        #print("\n -------------------------------------- \n")
        non_html = remove_html_tags(content)
        # print(non_html)
        spaceless = remove_white_space(non_html)
        # print(spaceless)
        #print("Amount of exclamation marks('!'): " + str(count_exclamation(spaceless)))
        #print("Amount of percentages('%'): " + str(count_percantage(spaceless)))
        clean = remove_punctutation(spaceless)
        # print(clean)
        array = word_arr_from_string(clean)
        # print(array)
        #print("Count capslocked: " + str(count_capslocked_words(array)))
        array2 = sync_capitalization_of_arr(array)
        # print(array2)
        c1 = counter_from_array(array2)
        print("---------------------------")
        print(c1)
        print("---------------------------")
    c2 = {}
    with open("spam-data-12-s75-h25/1/00029.cc0c62b49c1df0ad08ae49a7e1904531") as soubor:
        content = array_from_mail(soubor.read())[-1][1]
        non_html = remove_html_tags(content)
        spaceless = remove_white_space(non_html)
        clean = remove_punctutation(spaceless)
        array = word_arr_from_string(clean)
        array2 = sync_capitalization_of_arr(array)
        c2 = counter_from_array(array2)
        print(c2)
        print("---------------------------")
    c_diff = counter_difference(c1, c2, 50,50)
    c_diff2 = c1-c2
    print(c_diff)
    print("---------------------------")
    print(c_diff2)
    c_diff3 = c2-c1
    print("---------------------------")
    print(c_diff3)
    print("---------------------------")
    c_href = count_href("Href refh ref ahref <href="">")
    print(c_href)
