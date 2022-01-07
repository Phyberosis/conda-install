import os
import pathlib

Lel = 'yup, it loaded'

def pres():
    path = pathlib.Path(__file__).parent.resolve()

    with open(f'{path}/res/res.txt') as res:
        r = res.readlines()
        for line in r:
            print(line)


def ld():
    for d in os.listdir():
        print(d)