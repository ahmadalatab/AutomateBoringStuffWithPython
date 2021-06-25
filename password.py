#! python3
# An insecure password locker program

PASSWORDS = {
    'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage': '12345'
}

#sys.argv() is an array for command line arguments in python. Those are the arguments passed after the program call

import sys, pyperclip 
if len(sys.argv) < 2:
    print('Usage: python password.py [account] - copy account password')
    sys.exit()
account = sys.argv[1] #first command line argument is the account name

#Check whether account exist in PASSWORD dictionary
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard")
else:
    print("There is no account named " + account)