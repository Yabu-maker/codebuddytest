import os
import time

def testline():
    int i = 0
    for i in range(10):
        print(i)
        time.sleep(1)
        i += 1

    print("testline")

testline()