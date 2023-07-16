import json
import base64
import socket
import modeling
import time

def modify(x, frame):
    return modeling.SendableDetection({
        "id": x.TrackID,
        "type": x.ClassID,
        "left": x.Left,
        "right": x.Right,
        "top": x.Top,
        "bottom": x.Bottom,
        "center": x.Center,
        "frame": frame
    })

ss = socket.socket()
ss.connect(("192.168.12.238", 420))

def go(detections):
    frame = int(time.time())
    for x in detections:
        mod = modify(x, frame)
        js = mod.toJSON()
        print(js)
        print(">>> Sending", js)
        js = js.encode('utf-8') + "\\n".encode('utf-8')
        ss.sendall(js)

def complete():
    ss.close()