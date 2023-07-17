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

socklist = []

def go(detections):
    global socklist
    frame = int(time.time())
    ss = socket.socket()
    socklist.append(ss)
    ss.connect(("192.168.12.238", 420))
    # ss.connect(("127.0.0.1", 420))
    for x in detections:
        mod = modify(x, frame)
        js = mod.toJSON()
        print(js)
        print(">>> Sending", js)
        js = js.encode('utf-8') + b"\n"
        ss.sendall(js)
    ss.shutdown(socket.SHUT_WR)
    ss.close()

def complete():
    global socklist