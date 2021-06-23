# 1928. Base64 Decoder

import base64


def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')


t = int(input())

for i in range(1, t + 1):
    print("#" + str(i), base64ToString(input()))