import hashlib
import getpass 

def startup():
    mode = str(input('Hello! Type \"1\" if you want to create a new username & password to be stored, or \"2\" if you want to authenticate a current username & password: \n'))

    while mode != '1' and mode != '2':
        mode = str(input('Please type \"1\" or \"2\": \n'))

    if mode == '1': createNewCredentials()
    if mode == '2': authenticate()

file = open('creds.txt').read().splitlines()
currentUsers = []

for line in file:
    if ':' in line:
        lim = line.index(':')

        thisUser = ''
        i=0
        while i < lim:
            thisUser+=line[i]
            i+=1
        currentUsers.append(thisUser)



def createNewCredentials():
    global currentUsers
    f = open('creds.txt','a')

    newUser = input('Please input the new username: \n')

    while newUser in currentUsers:
        newUser = input('That username already exists. Pick a different username: \n')

    newPass = getpass.getpass(prompt='Please input the new password: \n')
    confPass = getpass.getpass(prompt='Confirm your password: \n')

    while newPass != confPass:
        print('Passwords do not match. Please try again.')
        newPass = getpass.getpass(prompt='Please input the new password: \n')
        confPass = getpass.getpass(prompt='Confirm your password: \n')

    e_newPass = encrypt(newPass)

    f.write(f'{newUser}:{e_newPass}\n')

    print(f'New user {newUser} created.')
    return 



def authenticate():
    global currentUsers
    global file

    inputUser = input('Username: ')
    inputPass = getpass.getpass(prompt='Password: ')
    
    e_inputPass = encrypt(inputPass)
    loginAttempts = 0

    if inputUser in currentUsers:
        pIndex = currentUsers.index(inputUser)
        thisLine = file[pIndex]

        minIndex = thisLine.index(':') + 1

    validPass = thisLine[minIndex:len(thisLine)]


    while (inputUser not in currentUsers or validPass != e_inputPass):
        loginAttempts+=1
        if loginAttempts == 3: 
            print('Login attempts exceeded. Goodbye')
            exit()
        else: 
            print('Incorrect username or password.')
            print(f'Attempts remaining: {3 - loginAttempts}')

            inputUser = input('Username: ')
            inputPass = getpass.getpass(prompt='Password: ')
            e_inputPass = encrypt(inputPass)
    
    print(f'\nUser {inputUser} validated.')

    



        

        



def encrypt(pw):
    return hashlib.sha256(pw.encode('utf-8')).hexdigest()


startup()