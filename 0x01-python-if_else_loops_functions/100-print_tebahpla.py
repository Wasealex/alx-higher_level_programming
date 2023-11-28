#!/usr/bin/python3
output = ""
for letter in range(ord('z'), ord('a') - 1, -1):
    if ((ord('z') - letter) % 2 == 0):
        output = output + chr(letter)
    else:
        output = output + chr(letter - 32)
print("{}".format(output), end='')
