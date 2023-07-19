import json
import base64
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
sock = context.socket(zmq.PUSH)
sock.bind("tcp://192.168.12.238:420")

def go(detections):
    global sock
    if(detections.__len__() == 0): return
    frame = int(time.time())
    build = ["["]
    for x in detections:
        mod = modify(x, frame)
        js = mod.toJSON()
        build.append(js)
        build.append(",")
    build.append("]")
    compile = "".join(build).replace(",]", "]")
    print(">>> Sending", compile)
    sock.send(compile.encode("utf-8"))

def complete():
    sock.term()