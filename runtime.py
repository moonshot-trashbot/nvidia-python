import json

def modify(y):
    x = {};
    x.__dict__ = y.__dict__.copy()
    if(hasattr(x, "TrackId") == False): x["TrackId"] = -1;
    return {
        "id": x["TrackId"],
        "left": x["Left"],
        "right": x["Right"],
        "top": x["Top"],
        "bottom": x["Bottom"],
        "center": [x["Center"][0], x["Center"][1]]
    }

def go(detections):
    for x in detections:
        print(modify(x))