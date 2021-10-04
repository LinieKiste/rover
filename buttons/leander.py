#!/usr/bin/python3

import explorerhat

def check_if_button_is_pressed():
    counter = 0
    for e in range(1000):
        if explorerhat.touch.one.is_pressed():
            counter += 1
    return counter > 900
button_pressed = False
while True:
    button_is_currently_pressed = check_if_button_is_pressed()
    if not(button_is_currently_pressed):
        button_pressed = button_is_currently_pressed
    if not(button_pressed) and button_is_currently_pressed:
        explorerhat.output.toggle()
        button_pressed = True
