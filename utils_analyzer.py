from collections import Counter


def counter_from_array(array):
    # useless function
    c = Counter(array)
    return c


def counter_difference(c1, c2):
    pass

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
    with open("spam-data-12-s75-h25/1/0001.bfc8d64d12b325ff385cca8d07b84288") as soubor:
        content = array_from_mail(soubor.read())[-1][1]
        # print(content)
        #print("\n -------------------------------------- \n")
        non_html = remove_html_tags(content)
        print(non_html)
        spaceless = remove_white_space(non_html)
        print(spaceless)
        print("Amount of exclamation marks('!'): " +
              str(count_exclamation(spaceless)))
        print("Amount of percentages('%'): " +
              str(count_percantage(spaceless)))
        clean = remove_punctutation(spaceless)
        print(clean)
        array = word_arr_from_string(clean)
        print(array)
        print("Count capslocked: " + str(count_capslocked_words(array)))
        array2 = sync_capitalization_of_arr(array)
        print(array2)
        c = counter_from_array(array2)
        print(c)
