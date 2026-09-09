import json
import random
import string
from pathlib import Path


class Bank:

    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.loads(fs.read())
        else:
            print('No such file exists')

    except Exception as err:
        print(f'An exception occurred: {err}')

    @staticmethod
    def update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data, indent=12))

    def CreateAccount(self):

        info = {
            'name': input('Enter your Name: '),
            'age': int(input('Enter your Age: ')),
            'email': input('Enter your Email: '),
            'pin': int(input('Enter your PIN: ')),
            'accountNo': random.randint(1000, 9999),
            'balance': 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:

            print('Sorry, you cannot create your account.')

        else:

            print('Account has been created successfully')

            for i in info:
                print(f'{i}: {info[i]}')

            print('Please note down your account number.')

            Bank.data.append(info)
            Bank.update()

    def depositmony(self):

        accNo = int(input('Please Enter your Account no. '))
        pin = int(input('Enter your pin '))

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accNo and i['pin'] == pin
        ]

        if not userdata:
            print('Sorry, no data found')

        else:
            amount = int(input('How much you want to deposit: '))

            if amount > 100000 or amount <= 0:
                print('Sorry, you can deposit between 1 and 100000')

            else:
                userdata[0]['balance'] += amount

                Bank.update()

                print('Amount deposited successfully')
                print('Your current balance:', userdata[0]['balance'])
    def withdrawmoney(self):
        accNo = int(input('Please Enter your Account no. '))
        pin = int(input('Enter your pin '))

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accNo and i['pin'] == pin
        ]

        if not userdata:
            print('Sorry, no data found')

        else:
            amount = int(input('How much you want to withdraw: '))

            if userdata[0]['balance'] < amount:
                print('sorry you dont have that much money')
                
            else:
                print(userdata)
                userdata[0]['balance'] -= amount

                Bank.update()

                print('Amount withdrow successfully')
                print('Your current balance:', userdata[0]['balance'])
    def Showdetails(self):
        accNo = int(input('Please Enter your Account no. '))
        pin = int(input('Enter your pin '))
        
        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accNo and i['pin'] == pin
        ]
        print('Your informtion are:\n\n\n')
        for i in userdata[0]:
            print(f'{i}:{userdata[0][i]}')
    def updatedetails(self):
        accNo = int(input('Please Enter your Account no. '))
        pin = int(input('Enter your pin '))

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accNo and i['pin'] == pin
        ]

        if userdata == False:
            print('no such user found')
        else:
            print('yu can not change the age, account, number, balance')
            print('Fill the details for change or leave it empty if no change')

            newdata = {
                'name':input('please Enter new name or press enter: '),
                'email':input('Plese Enter your new email or press enter'),
                'pin': input('please Entre new pin or press enter')
            }

            if newdata['name']=='':
                newdata['name'] =userdata[0]['name']
            if newdata['email']=='':
                newdata['email'] =userdata[0]['email']
            if newdata['pin']=='':
                newdata['pin'] =userdata[0]['pin']

            newdata['age'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']


    def deleteAccount(self):
        accNo = int(input('Please Enter your Account no. '))
        pin = int(input('Enter your pin '))

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accNo and i['pin'] == pin
        ]
        if userdata == False:
            print('sorry no such data exist')
        else:
            check = input('press y if you actully want to delet the account or press enter ')
            if check == 'n' or check == 'y':
                print('bypassed')
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print('account deleted succesfully ')
                Bank.__update()
            
                
user = Bank()

print('Press 1 for Creating an Account')
print('Press 2 for Deposit the Money in the Bank')
print('Press 3 for Withdrawing the Money')
print('Press 4 for Details')
print('Press 5 for Updating your Account')
print('Press 6 for Deleting your Account')

check = int(input('Tell your response: '))

if check == 1:
    user.CreateAccount()

if check ==2:
    user.depositmony()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.Showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.deleteAccount()
 