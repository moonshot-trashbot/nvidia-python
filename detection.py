from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource("/dev/video0")

while True:
    img = camera.Capture()

    if img is None:
        continue

    detections = net.Detect(img)

    print(detections)