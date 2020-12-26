import re


def remove_html_tags(html_text):
    # for some reason regular expression can't go through \n
    html_text = html_text.replace("\n", " ")
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    non_html = re.sub(cleanr, '', html_text)
    return non_html


def remove_white_space(txt):
    txt = txt.replace("\t", " ")
    while "  " in txt:
        txt = txt.replace("  ", " ")
    return txt


def remove_punctutation(txt):
    txt = txt.replace('"', " ")
    for char in ".,!?:;'":
        txt = txt.replace(char, "")
    return txt


def word_arr_from_string(s):
    word_arr = s.split(" ")
    while("" in word_arr):
        word_arr.remove("")
    return word_arr


def sync_capitalization_of_arr(array):
    for i in range(len(array)):
        array[i] = array[i].lower()
    return array


if __name__ == "__main__":
    from utils_email import array_from_mail
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
        arr = word_arr_from_string(clean)
        print(arr)
