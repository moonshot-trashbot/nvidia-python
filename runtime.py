import json

def modify(x):
    if(hasattr(x, "TrackId") == False): return {"fake": True};
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