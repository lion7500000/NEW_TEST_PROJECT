import  os

while True:
    adress = input ("Enter adress of page:\n")

    if adress == 'end':
        break

    if 'https://' in adress:
        os.system('start ' + adress)
        print('1')

    if 'www.' in adress:
        adress = 'https://' + adress
        os.system('start ' + adress)
        print ('2')

    else:
        adress = 'https://www.' + adress
        os.system('start ' + adress)
        print ('3')
