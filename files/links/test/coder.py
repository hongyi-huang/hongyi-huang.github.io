import base64

#print(base64.b64decode(input.encode("ascii")).decode("ascii"))

def encode(input):
    return base64.b64encode(input.encode("ascii")).decode("ascii")

def decode(input):
    return base64.b64decode(input.encode("ascii")).decode("ascii")

with open("raw.txt", "r") as fr, open("server.list", "w+") as fw1, open("v2rayn.list", "w+") as fw2, open("server.list3", "w+") as fw3:
    lines = ""
    for line in fr.readlines():
        print(line)
        fw1.write(line)
        lines += line
        bts = line[8:]
    fw2.write(encode(lines))
    fw3.write(encode(lines))

