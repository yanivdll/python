import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


message = "Please call me at 917-370-4008. Thanks and see you soon"

#for i in range(len(message)):
#    chunk = message[i:i+12]
#    if isPhoneNumber(chunk):
#        print('Phone number was found: ' + chunk)

heroRegex = re.compile(r'Agent (\w)\w*')
#heroRegex = re.compile(r'(HaHa){1,5}')
mo = heroRegex.sub(r'\1****', 'Agent Alice gave the secret document to Agent Bob')
print(mo.group())
print('Done.')
