import json
import base64
import socket

class Fake:
    def __init__(self, data):
        self.TrackID = data["TrackID"]
        self.Confidence = data["Confidence"]
        self.ClassID = data["ClassID"]
        self.Left = data["Left"]
        self.Right = data["Right"]
        self.Top = data["Top"]
        self.Bottom = data["Bottom"]
        self.Center = data["Center"]

class DetectorObject:
    def __init__(self, data):
        self.id = data["id"]
        self.type = data["type"]
        self.left = data["left"]
        self.right = data["right"]
        self.top = data["top"]
        self.bottom = data["bottom"]
        self.center = data["center"]
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

def modify(x):
    return DetectorObject({
        "id": x.TrackID,
        "type": x.ClassID,
        "left": x.Left,
        "right": x.Right,
        "top": x.Top,
        "bottom": x.Bottom,
        "center": x.Center
    })

ss = socket.socket()
ss.connect(("192.168.12.238", 420))

def go(detections):
    for x in detections:
        mod = modify(x)
        js = mod.toJSON() + "\n"
        print(js)
        print(">>> Sending", js)
        js = js.encode('utf-8')
        ss.sendall(js)

def complete():
    ss.close()