#!/usr/bin/python3

import explorerhat

isOn = False

while True:
    if explorerhat.touch.one.is_pressed():
        print("button one pressed")
        if not isOn:
            while not explorerhat.touch.one.is_pressed():
                isOn = True
                explorerhat.output.on()

        else:
            while not explorerhat.touch.one.is_pressed():
                isOn = False
                explorerhat.output.off()

