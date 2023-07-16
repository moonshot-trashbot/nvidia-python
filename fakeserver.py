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
            "Center": [-85, 0]
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
            "Center": [20, 0]
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
            "Center": [45, 0]
        })
    ]
]
for detections in fakelog:
    runtime.go(detections)
    time.sleep(3)