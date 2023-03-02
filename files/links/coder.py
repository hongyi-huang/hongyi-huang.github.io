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
        server_remark, uri = line.strip().split(',')
        bts = uri[8:] # strip "vmess://"
        print("decode the raw text",decode(bts))
        # example:  "auto:cef93178-c454-4976-b499-ed4bd0d5331f@173.230.156.221:52209"
        ob = json.loads(decode(bts))
        # change remark name
        ob["ps"]=server_remark
        new_uri = "vmess://" + encode(json.dumps(ob)) + "\n"
        # lines used for server.list3
        lines += new_uri
        # dump to server.list
        fw1.write(new_uri)
        
        keywords = [encode("auto:%s@%s:%s" % (ob["id"], ob["add"], ob["port"]))]
        # check if tls
        if ob["net"]=="ws":
            if ob["tls"] != "":
                keywords.append("network=%s&wsHost=%s&aid=0&tls=1&allowInsecure=0&mux=0&remark=%s" % (ob["net"], ob["host"], ob["ps"]))
            else:
                keywords.append("network=%s&aid=0&allowInsecure=1&mux=0&remark=%s" % (ob["net"],  ob["ps"]))
        else:
            keywords.append("network=%s&aid=0&tls=0&allowInsecure=0&mux=0&remark=%s" % (ob["net"], ob["ps"]))
        v2rayn_list.append("vmess://" + "?".join(keywords))
    fw2.write(encode("\n".join(v2rayn_list)))
    fw3.write(encode(lines))

"""
    {
"v": "2",
"ps": "233v2.com_kx.hongyi-huang.com",
"add": "kx.hongyi-huang.com",
"port": "443",
"id": "cef93178-c454-4976-b499-ed4bd0d5331f",
"aid": "0",
"net": "ws",
"type": "none",
"host": "kx.hongyi-huang.com",
"path": "/",
"tls": "tls"
}

    {"port":"443",
     "ps":"tls_test",
     "tls":"tls",
     "id":"9c9e3219-64bd-42eb-a94a-7565d4e3e625",
     "aid":"0",
     "v":"2",
     "host":"kx.hongyi-huang.com",
     "type":"none",
     "path":"\/",
     "net":"ws",
     "add":"kx.hongyi-huang.com"}
"""
