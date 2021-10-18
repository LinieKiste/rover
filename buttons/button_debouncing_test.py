#!/usr/bin/python3

import explorerhat

counter = 0
counter2 = 0

while True:
    if counter2 == 10000:
        counter2 = 0
        print(counter)
        counter = 0

    if explorerhat.touch.one.is_pressed():
        counter += 1
        print("True")
    else:
        print("False")
        pass

    counter2 += 1
