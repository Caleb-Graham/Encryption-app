# My attempt to create a simple encryption program
import sys


def encrypt():
    message = input('Enter the message you would like to encrypt: ')
    print('')
    for i in message:
        print(ord(i), end=" ")
    print('')


def decrypt():
    decryption = input('Enter the message you would like to decode here: ')
    print('')
    decodedMessage = ' '

    for i in decryption.split():
        codeNum = int(i)    # convert digits to a number
        decodedMessage = decodedMessage + chr(codeNum)  # concatenate character to message
    print(decodedMessage.lstrip())


def main():
    print("This is an application that allows you to encrypt and decrypt messages at will.")

    while True:
        print('')
        runProgram = input("Enter a 1 if you want to encrypt a message, a 2 if you want to decrypt a message,"
                           " or a 3 if you want to end the program: ")
        print('')

        if runProgram == '1':
            encrypt()

        elif runProgram == '2':
            decrypt()

        elif runProgram == '3':
            sys.exit()

        else:
            print("You did not enter a valid option. Please try again!")


main()
