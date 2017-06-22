#! python3
#passwordManager.py - an insecure password locker manager

import pyperclip    #copy and paste module
import sys          #system module
PASSWORDS = {'email': 'fakePassword',
            'blog': 'fakeBlog',
            'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: passwordManager.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] #first command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy([PASSWORDS[account]])
    print('Password for ' + account + 'copied to clipboard')
else:
    print('There is no account named' + account)