# Using the python 3.13 !
from pybase64 import b64encode, b64decode

def encode(chaine):
    """
    Encode a string in base 64
    :param chaine: string to encode
    :type chaine: str
    :return: encoded string
    :rtype: str
    """
    return b64encode(chaine.encode()).decode()


def decode(chaine):
    """
    Decode a string in base 64
    :param chaine: string to
    :type chaine: str
    :return: decoded string
    :rtype: str
    """
    return b64decode(chaine).decode()


def main():
    print("Menu:\n\t1. 1. Encode in base 64\n\t2. Decode in base  64\n3. Quit\n\n")
    choix = input("\tYour choice? ?")
    if choix == "1":
        chaine = input("Enter the string to encode : ")
        print(f"Result : {encode(chaine)}")
    elif choix == "2":
        chaine = input("Enter the string to decode : ")
        print(f"Result : {decode(chaine)}")


if __name__ == "__main__":
    main()
