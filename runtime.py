import json

def modify(x):
    return {
        "id": x.TrackID | -1,
        "class": x.ClassID,
        "left": x.Left,
        "right": x.Right,
        "top": x.Top,
        "bottom": x.Bottom,
        "center": x.Center
    }

def go(detections):
    for x in detections:
        print(modify(x))