import string
import random

def getRandomPass(passSize = 10, useUpper = True, useLower = True, useDigits = True, useSpecial = True):
    chars = "";
    if useUpper:
        chars = chars + string.ascii_uppercase
    if useLower:
        chars = chars + string.ascii_lowercase
    if useDigits:
        chars = chars + string.digits
    if useSpecial:
        chars = chars + "!\"#$%&'()*+,-.:;<=>?@[\]^_`{|}~"
    return ''.join(random.SystemRandom().choice(chars) for _ in range(passSize))

def test():
    print getRandomPass();
    print getRandomPass(15, True, True, False, True)
    print getRandomPass()

if __name__ == "__main__":
    test()

