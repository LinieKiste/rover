import explorerhat
import time

# s = 60
# for i in range(10):
#     s -= 5
#     print(f"speed is {s}")
#     explorerhat.motor.backward(s)
#     time.sleep(2)
#     if s <= 0:
#         break

k = 0
for i in range(0):
    k += 0.005
    print(f"kickstart time is {k}")
    explorerhat.motor.forward(100)
    time.sleep(k)
    explorerhat.motor.forward(40)
    time.sleep(3)


explorerhat.motor.forward(100)
time.sleep(.03)
explorerhat.motor.forward(40)
time.sleep(10)
