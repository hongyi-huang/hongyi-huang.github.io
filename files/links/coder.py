import base64
import json
import os
#print(base64.b64decode(input.encode("ascii")).decode("ascii"))

os.chdir(input("Work Dir: "))
print(os.getcwd())

def encode(input):
    return base64.b64encode(input.encode("ascii")).decode("ascii")

def decode(input):
    return base64.b64decode(input.encode("ascii")).decode("ascii")

with open("raw.txt", "r") as fr, open("server.list", "w+") as fw1, open("server.list2", "w+") as fw2, open("server.list3", "w+") as fw3:
    lines = ""
    v2rayn_list = []
    for line in fr.readlines():
        # print(line)
        fw1.write(line)
        lines += line
        bts = line.strip()[8:]
        print(decode(bts))
        # chacha20-poly1305:cef93178-c454-4976-b499-ed4bd0d5331f@173.230.156.221:52209
        ob = json.loads(decode(bts))
        keywords = [encode("chacha20-poly1305:%s@%s:%s" % (ob["id"], ob["add"], ob["port"]))]
        keywords.append("network=%s&aid=0&tls=0&allowInsecure=1&mux=0&remark=%s" % (ob["net"], ob["ps"]))
        v2rayn_list.append("vmess://" + "?".join(keywords))
    fw2.write(encode("\n".join(v2rayn_list)))
    fw3.write(encode(lines))

