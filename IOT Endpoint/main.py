import cv2
import numpy
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from cv2 import imshow, waitKey
from msrest.authentication import CognitiveServicesCredentials
import LocalImageProcess
from CrowdMetrics import countPeople
import SQLInterface
from configOpen import configOpen

# Change to "False" to disable camera view + logs
debug = True

class IOTApp:
    def __init__(self, debugEnabled=False):
        # Parse CameraConfig.json
        self.config = configOpen("CameraConfig.json")

        # Object vars
        self.debugEnabled = debugEnabled
        self.imagePath = "capture.jpg"
        self.numberOfPeople = 0

        # Setup Azure
        self.subscription_key = self.config["AzureKey"]
        self.endpoint = self.config["AzureEndpoint"]

        self.client = ComputerVisionClient(self.endpoint, CognitiveServicesCredentials(self.subscription_key))

        # Connect to SQL
        self.db = SQLInterface.SQLConnection(self.config["SQLServerAddr"], self.config["SQLServerUser"],
                                             self.config["SQLServerPass"], self.config["CameraName"])

    def loop(self):
        while True:

            # Capture image from default cam and send to self.imagePath
            LocalImageProcess.captureImage(self.imagePath)

            # Send image to Azure
            with open(self.imagePath, "rb") as data:
                detect_objects_results_remote = self.client.detect_objects_in_stream(data)

            # Process Azure data
            self.numberOfPeople = countPeople(detect_objects_results_remote.objects)
            self.db.updateDB(self.numberOfPeople)

            # Process debug logs + annotations if enabled
            if self.debugEnabled:
                self.debug(detect_objects_results_remote.objects)
            
            # Delay 5 seconds to avoid Azure charge + rate limit
            cv2.waitKey(5000)
    
    # Overlay Azure object bounding boxes over image capture
    def debug(self, objects):
        im = LocalImageProcess.drawObjectBoundingBoxes(objects, self.imagePath)

        open_cv_image = cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR)
        imshow("LiveView", open_cv_image)

# Entrypoint
if __name__ == "__main__":
    cam = IOTApp(debug) 
    cam.loop()
