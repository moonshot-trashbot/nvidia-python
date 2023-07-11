import time
import runtime

fakelog = [
    [
        {
            "TrackID": 1,
            "Confidence": 0.75,
            "ClassID": 1,
            "Left": 394,
            "Right": 850,
            "Top": 123,
            "Bottom": 200
        }
    ],
    [
        {
            "TrackID": 2,
            "Confidence": 0.65,
            "ClassID": 1,
            "Left": 360,
            "Right": 890,
            "Top": 193,
            "Bottom": 210
        }
    ]
]
for detections in fakelog:
    runtime.go(detections)
    time.sleep(1)