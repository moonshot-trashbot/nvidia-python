import json

def modify(x):
    if(x.TrackId is None): return {"fake": True};
    return {
        "id": x.TrackID,
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