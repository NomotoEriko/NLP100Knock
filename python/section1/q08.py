def cipher(string=None):
    if None == string:
        print('E: Empty string.')
        return None
    else:
        return ''.join(chr(219-ord(s)) if s.islower() else s for s in string)


if __name__ == '__main__':
    string = "Before running mongod for the first time," \
             " ensure that the user account running mongod has read and write permissions for the directory."
    print('pure sentence:\t', string)
    print('encoded sentence:\t', cipher(string))
