import random

platinum = 557675
classic = 417401
prepaid = 549630
standart = 511477
business = 457601

def escolherbin():
    binSorteada = random.choice([platinum, classic, prepaid, standart, business])
    print(binSorteada)
    return binSorteada
