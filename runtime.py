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

def modify(x):
    return {
        "id": x.TrackID,
        "class": x.ClassID,
        "left": x.Left,
        "right": x.Right,
        "top": x.Top,
        "bottom": x.Bottom,
        "center": x.Center
    }

ss = socket.socket()
ss.connect(("192.168.12.238", 420))

def go(detections):
    for x in detections:
        mod = modify(x)
        js = json.dumps(mod)
        print(js)
        print(">>> Sending", js)
        js = js.encode('utf-8') + "\n"
        ss.sendall(js)

def complete():
    ss.close()