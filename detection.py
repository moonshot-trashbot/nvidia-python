import time
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput
import runtime

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
net.SetTrackingEnabled(True)
net.SetTrackingParams(minFrames=3, dropFrames=15, overlapThreshold=0.5)
display = videoOutput("display://0")

camera = videoSource("/dev/video0")

while True:
    img = camera.Capture()
    if img is None: continue
    display.render(img)
    detections = net.Detect(img)
    runtime.go(detections)
    time.sleep(0.33)