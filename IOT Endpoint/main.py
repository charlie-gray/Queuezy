import cv2
import numpy
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from cv2 import imshow, waitKey
from msrest.authentication import CognitiveServicesCredentials
import LocalImageProcess
from CrowdMetrics import countPeople
import SQLInterface
from configOpen import configOpen


class IOTApp:
    def __init__(self, debugEnabled=False):
        self.config = configOpen("CameraConfig.json")
        self.debugEnabled = debugEnabled
        self.imagePath = "capture.jpg"
        self.numberOfPeople = 0

        # Setup Azure
        self.subscription_key = self.config["AzureKey"]
        self.endpoint = self.config["AzureEndpoint"]

        self.client = ComputerVisionClient(self.endpoint, CognitiveServicesCredentials(self.subscription_key))

        self.db = SQLInterface.SQLConnection(self.config["SQLServerAddr"], self.config["SQLServerUser"],
                                             self.config["SQLServerPass"], self.config["CameraName"])

    def loop(self):
        while True:
            LocalImageProcess.captureImage(self.imagePath)

            with open(self.imagePath, "rb") as data:
                detect_objects_results_remote = self.client.detect_objects_in_stream(data)

            self.numberOfPeople = countPeople(detect_objects_results_remote.objects)
            self.db.updateDB(self.numberOfPeople)

            if self.debugEnabled:
                self.debug(detect_objects_results_remote.objects)

            cv2.waitKey(5000)

    def debug(self, objects):
        im = LocalImageProcess.drawObjectBoundingBoxes(objects, self.imagePath)

        open_cv_image = cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR)
        imshow("LiveView", open_cv_image)


if __name__ == "__main__":
    cam = IOTApp(True)
    cam.loop()
