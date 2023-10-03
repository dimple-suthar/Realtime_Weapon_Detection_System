from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import os
import cv2
#os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")
import numpy as np
import time
import requests
from detection import Detection


# Manages detection window, starts and stops detection thread
class DetectionWindow(QMainWindow):
    def __init__(self):
        super(DetectionWindow, self).__init__()
        loadUi('ui/detection_window.ui', self)
        self.stop_detection_button.clicked.connect(self.close)
       # self.detection = Detection()

    # Created detection instance
    # class create_detection_instance:
    #     def __init__(self, token, location, receiver):
    #         self.detection = Detection(token, location, receiver)
    def create_detection_instance(self, token, location, receiver):
        try:
            self.detection = Detection(token, location, receiver)
            print("Detection instance created successfully.")
        except Exception as e:
            print(f"Error creating Detection instance: {str(e)}")

    # Assigns detection output to the label in order to display detection output
    @pyqtSlot(QImage)
    def set_image(self, image):
        self.label_detection.setPixmap(QPixmap.fromImage(image))

    # Starts detection
    def start_detection(self):
        self.detection.changePixmap.connect(self.set_image)
        self.detection.start()
        self.show()

    # When closed
    def closeEvent(self, event):
        self.detection.running = False
        event.accept()
