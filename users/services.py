import random

def generation():
    password = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    return password