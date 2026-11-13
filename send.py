import sys, json, urllib.request, urllib.parse

TOKEN = open(r"token.txt").read().strip()
CHAT  = int(sys.argv[1])
HTML  = open(sys.argv[2], "rb").read()

data = urllib.parse.urlencode({
    "chat_id": CHAT,
    "html": HTML.decode("utf-8"),
}).encode()

req = urllib.request.Request(
    f"https://api.telegram.org/bot{TOKEN}/sendWidget", data=data)
resp = json.load(urllib.request.urlopen(req))
print(json.dumps(resp, indent=2))
