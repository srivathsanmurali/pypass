import string
import random
import config

def getRandomPass():
    chars = "";
    if config.useUpper:
        chars = chars + string.ascii_uppercase
    if config.useLower:
        chars = chars + string.ascii_lowercase
    if config.useDigits:
        chars = chars + string.digits
    if config.useSpecial:
        chars = chars + "!\"#$%&'()*+,-.:;<=>?@[\]^_`{|}~"
    return ''.join(random.SystemRandom().choice(chars) for _ in range(config.passSize))

def test():
    print getRandomPass();
    print getRandomPass()

if __name__ == "__main__":
    test()

