import email

def array_from_mail(mail):
    '''
    Standard .items() from email package, but content is added as last value in array
    '''
    msg = email.message_from_string(mail)
    arr = msg.items()
    arr.append(["Content-Actual",msg.get_payload()])
    return arr

if __name__ == "__main__":
    with open("spam-data-12-s75-h25/1/2408.9d2e0a6592738da2aad3f0657d436895") as soubor:
        print(array_from_mail(soubor.read()))
