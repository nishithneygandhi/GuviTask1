import hashlib
import re


def solve(s):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat,s):
        return True
    return False


def isPwdValid(s):
    l, u, p, d = 0, 0, 0, 0
    if (len(s) >= 8):
        for i in s:

            # counting lowercase alphabets
            if (i.islower()):
                l += 1

                # counting uppercase alphabets
            if (i.isupper()):
                u += 1

                # counting digits
            if (i.isdigit()):
                d += 1

                # counting the mentioned special characters
            if (i == '@' or i == '$' or i == '_' or i == '#'):
                p += 1
    if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(s)):
        return True
    else:
        return False


def signup():
    email = input('Enter email address: ')
    if not solve(email):
        print('The email id entered is not valid. Try again')
        return

    pwd = input('Enter password: ')
    if not isPwdValid(pwd):
        print('The password entered is not valid. Try again')
        return

    enc = pwd.encode()
    hash1 = hashlib.md5(enc).hexdigest()
    with open('credentials.txt', 'a') as f:
        f.write(email + '\t')
        f.write(hash1)
        f.write('\n')
        f.close()
    print('You have registered successfully!')


def login():
    email = input('Enter email: ')
    pwd = input('Enter password: ')
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    file = open('credentials.txt', 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        stored_email, stored_pwd = line.split('\t')
        if email == stored_email and auth_hash == stored_pwd.rstrip():
            print('Logged in Successfully ')
            file.close()
            return
    print('Login failed!. Please register or choose forgot password to reset \n')
    file.close()


def forgotPassword():
    email = input('Enter email: ')

    file = open('credentials.txt', 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        stored_email, stored_pwd = line.split('\t')
        if email == stored_email:
            pwd = input('Enter new password to change: ')
            if not isPwdValid(pwd):
                print('The password entered is not valid. Try again')
                file.close()
                return

            enc = pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            lines[index] = stored_email + '\t' + hash1 + '\n'
            file = open('credentials.txt', 'w')
            file.writelines(lines)
            file.close()
            print('password changed successfully \n')
            return
    print('user does not exist failed!. Please register \n')
    file.close()
    return


while 1:
    print('********** Login System **********')
    print('1.Signup')
    print('2.Login')
    print('3.Forgot Password')
    print('4.Exit')
    ch = int(input('Enter your choice: '))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        forgotPassword()
    elif ch == 4:
        break
    else:
        print('Wrong Choice!')