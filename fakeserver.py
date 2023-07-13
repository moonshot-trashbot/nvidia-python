import time
import runtime
import modeling
        
fakelog = [
    [
        modeling.CustomizedTestingInput({
            "TrackID": 1,
            "Confidence": 0.75,
            "ClassID": 1,
            "Left": 394,
            "Right": 850,
            "Top": 123,
            "Bottom": 200,
            "Center": [0, 0]
        })
    ],
    [
        modeling.CustomizedTestingInput({
            "TrackID": 1,
            "Confidence": 0.75,
            "ClassID": 1,
            "Left": 394,
            "Right": 850,
            "Top": 123,
            "Bottom": 200,
            "Center": [0, 0]
        }),
        modeling.CustomizedTestingInput({
            "TrackID": 2,
            "Confidence": 0.65,
            "ClassID": 1,
            "Left": 360,
            "Right": 890,
            "Top": 193,
            "Bottom": 210,
            "Center": [0, 0]
        })
    ]
]
for detections in fakelog:
    runtime.go(detections)
    time.sleep(1)