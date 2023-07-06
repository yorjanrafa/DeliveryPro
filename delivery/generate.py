import random 
def password():
    numbers = "0123456789"
    letters = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
    simbols = "!·$%&/()=?|@#~½¬{[]}º"
    joinxx  = f'{letters}{numbers}{simbols}'
    size    = 60
    passwordx = "".join(random.sample(joinxx, size))
    return passwordx
