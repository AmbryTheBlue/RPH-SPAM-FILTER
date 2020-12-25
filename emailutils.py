import email

def array_from_mail(mail):
    '''
    Standard
    '''
    msg = email.message_from_string(mail)
    arr = msg.items()
    arr.append(["Content-Actual",msg.get_payload()])
    return arr

if __name__ == "__main__":
    import os
    with open("spam-data-12-s75-h25/1/2408.9d2e0a6592738da2aad3f0657d436895") as soubor:
        print(array_from_mail(soubor.read()))
