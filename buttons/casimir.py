#!/usr/bin/python3

import explorerhat

explorerhat.output.off()

while True:

    explorerhat.touch.one.on_changed(explorerhat.output.toggle(), 500)


