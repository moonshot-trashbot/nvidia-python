import json
import base64
import socket
import modeling
import time
import zmq

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

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.12.238:420")

def go(detections):
    if(detections.__len__() == 0): return
    global socklist
    frame = int(time.time())
    ss = socket.socket()
    socklist.append(ss)
    ss.connect(("192.168.12.238", 420))
    # ss.connect(("127.0.0.1", 420))
    build = ["["]
    for x in detections:
        mod = modify(x, frame)
        js = mod.toJSON()
        build.append(js + ",")
    build.append("]")
    compile = "".join(build).replace(",]", "]")
    print(">>> Sending", compile)
    socket.send(bytes(compile))

def complete():
    socket.term()