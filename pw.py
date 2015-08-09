#! python3

# pw.py - An insecure password locker program

PASSWORDS = {'email': 'asdasfsgdfqrtq23',
            'blog': 'klsdj43reav323r',
             'luggage': '123124'
             }

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [accont] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'is ' + PASSWORDS[account] + '. It was copied to the clipboard')
else:
    print('The account ' + account + ' wasn\'t found.')


