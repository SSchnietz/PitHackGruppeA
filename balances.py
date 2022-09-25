print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
#clearscreen
balance = 0
creditammount = 10000
usedcredit = 'false'
print('You have', balance, '$')
while True:
    print('\n\nYou now have', balance, '$')
    inorout = str(input('Do you want to pay out or in?\nuse [in] or [out]!\n -> '))
    if inorout == 'in':
        ammountin = float(input('Ammount to pay in? '))
        print('You paid ', ammountin, '$ to the bank.')
        balance = balance + ammountin
    elif inorout == 'out':
        ammountout = float(input('Ammount to pay out? '))
        print('The bank paid you', ammountout)
        balance = balance - ammountout
    elif inorout == 'eco set':
        ammountset = float(input('Set ammount to?'))
        balance = ammountset
    else:
        print('Invalid argument!')
    if balance > 1000 and usedcredit == 'false':
        credit = str(input('Credit? y/n \n'))
        if credit == 'y':
            balance = balance + creditammount
            usedcredit = 'true'
        else:
            if usedcredit == 'false':
                print('No credit.')
            else:
                continue
    else:
        continue
    #print('\n\nYou now have', balance, '$')
    if balance < 0:
        print('You are out of money.')
        break
    #else:
    #    continue
    #print('\n\nYou now have', balance, '$')