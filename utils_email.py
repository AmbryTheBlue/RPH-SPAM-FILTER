import email


def recursive_msg(msg):
    if(msg.is_multipart()):
        content = ""
        for sub_msg in msg.get_payload():
            content += recursive_msg(sub_msg)
    else:
        content = msg.get_payload()
    return content


def array_from_mail(mail):
    '''
    Standard .items() from email package, but content is added as last value in array
    '''
    msg = email.message_from_string(mail)
    arr = msg.items()  # creates an array of twos
    content = recursive_msg(msg)
    arr.append(["Content-Actual", content])
    return arr


if __name__ == "__main__":
    with open("spam-data-12-s75-h25/1/00090.52630c4c07cd069c7bc7658c1a7a7253") as soubor:
        print(array_from_mail(soubor.read()))
