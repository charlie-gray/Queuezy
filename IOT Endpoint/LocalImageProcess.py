import time

from PIL import ImageDraw, Image
from cv2 import VideoCapture, imwrite

# Captures image from default webcam and saves to filePath
def captureImage(filePath):
    cam_port = 0
    cam = VideoCapture(cam_port)
    time.sleep(3)
    result, image = cam.read()

    if result:
        imwrite(filePath, image)
    else:
        print("ERROR: Unable to capture image from camera")


# Takes in a detect_objects_results_remote.objects object and overlays bounding boxes over image at imagePath 
# Returns annotated image
def drawObjectBoundingBoxes(objects, imagePath):
    im = Image.open(imagePath)
    img1 = ImageDraw.Draw(im)
    
    # Logs object location + draws bounding boxes/labels over image
    for o in objects:
        print(o.object_property)
        print("object at location {}, {}, {}, {}".format( \
            o.rectangle.x, o.rectangle.x + o.rectangle.w, \
            o.rectangle.y, o.rectangle.y + o.rectangle.h))

        shape = [(o.rectangle.x, o.rectangle.y),
                 (o.rectangle.x + o.rectangle.w, o.rectangle.y + o.rectangle.h)]

        # Outline Objects
        img1.rectangle(shape, outline="red")

        # Add Labels
        img1.text((o.rectangle.x, o.rectangle.y), o.object_property, fill=(0, 50, 255))

    return im
