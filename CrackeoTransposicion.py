# Transposition Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import detectEnglish, descifradoTransposicion

def main():
    # You might want to copy & paste this text from the source code at
    # https://invpy.com/transpositionHacker.py
    #propuesta: Iuirisr dnmoeisyfanctt ot uy
    myMessage = input("Ingresa frase a 'hackear': ")

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print(hackedMessage)


def hackTransposition(message):
    print('Hacking...')

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # Brute-force by looping through every possible key.
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))

        decryptedText = descifradoTransposicion.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
            # Ask user if this is the correct decryption.
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None

if __name__ == '__main__':
    main()
