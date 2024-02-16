# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore    import QThread 
from PIL import Image, ImageGrab
import win32api, win32con
import numpy as np
import pytesseract
import keyboard
import pyautogui
import ctypes
import time
import sys
import cv2
import settings

global label
global label_2

class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class CURSORINFO(ctypes.Structure):
    _fields_ = [('cbSize', ctypes.c_uint),
                ('flags', ctypes.c_uint),
                ('hCursor', ctypes.c_void_p),
                ('ptScreenPos', POINT)]

# Load function from user32.dll and set argument types
    
class Thread(QThread):
    def run(self):

        self.number = 7
        self.max_blue_pixel = 0
        self.list_max = []
        while True:
            time.sleep(0.1)
            img = ImageGrab.grab((0, 969, 1920, 971))
            list_pixel = []
            self.list_max = []
            list_pixel.append([img.getpixel((683,1)), 680])
            list_pixel.append([img.getpixel((775,1)), 775])
            list_pixel.append([img.getpixel((875,1)), 875])
            list_pixel.append([img.getpixel((970,1)), 970])
            list_pixel.append([img.getpixel((1065,1)), 1065])
            list_pixel.append([img.getpixel((1160,1)), 1160])
            for i in range(6):
                self.list_max.append(list_pixel[i][0][2]-list_pixel[i][0][1]-list_pixel[i][0][0])
                self.max_blue_pixel = max(self.list_max)
            if self.max_blue_pixel > -10 : 
                self.number = self.list_max.index(self.max_blue_pixel) + 1 

    def get_number(self):
        return self.number
    
    def get_test(self):
        return f"{self.max_blue_pixel} {self.list_max}"

    def search_active_inventory_weapon(self, img):
        if img.getpixel((0,0))[2]> 100: 
            return 0
        else:
            return 1 


class Main(QThread):

    global label
    global label_2

    def get_cursor_flags(self):
        info = CURSORINFO()
        info.cbSize = ctypes.sizeof(info)
        self.GetCursorInfo(ctypes.byref(info))
        return info.flags

    def get_bt(self):
        if win32api.GetKeyState(win32con.VK_CONTROL) < -1:
            return "sitting"
        return "got_up"
    
    def get_rmb(self):
        if win32api.GetKeyState(0x02) < -1:
            return "taking_aim"
        return "hip"

    def run(self):

        self.thread2 = Thread()
        self.thread2.start()

        self.GetCursorInfo = ctypes.windll.user32.GetCursorInfo
        self.GetCursorInfo.argtypes = [ctypes.POINTER(CURSORINFO)]
        
        self.weapon_pattern = settings.Settings.weapon_pattern
        self.path_tesseract = settings.Settings.path_tesseract
        self.btn_off = settings.Settings.btn_off
        self.btn_start = settings.Settings.btn_start
        
        while True:
            time.sleep(0.1)
            label.setText(f"inv:{self.thread2.get_number()}")
            if keyboard.is_pressed(self.btn_start):
                self.auto_identifier()   

    

    def search_modules(self, img_modules, name, file):
        needle = cv2.imread(file)
        result = cv2.matchTemplate(np.array(img_modules), needle, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        locations = []
        for y, x in zip(*np.where(result >= threshold)):
            locations.append((x, y))
        if locations == []:
            string_img_modules = "normal"
        else:
            string_img_modules = name
        locations = []
        return string_img_modules

    def auto_identifier(self):
        pyautogui.press("tab")
        time.sleep(0.01)
        img_name_weapon = ImageGrab.grab((650, 100, 1300, 150))
        img_modules = ImageGrab.grab((680, 380, 950, 460))
        pyautogui.press("tab")
        pytesseract.pytesseract.tesseract_cmd = self.path_tesseract
        string_name_weapon = pytesseract.image_to_string(img_name_weapon, lang="rus")
        string_name_weapon = ' '.join(string_name_weapon.split())
        
        string_img_modules = self.search_modules(img_modules, "holo", "search/holo.png")

        if string_img_modules == "normal":
            string_img_modules = self.search_modules(img_modules, "x8", "search/x8.png")

        try:
            if self.weapon_pattern[string_name_weapon]:
                if string_name_weapon in ["ШТУРМОВАЯ ВИНТОВКА"]:
                    self.sample2(weapon_name=string_name_weapon, status=string_img_modules)
                else:
                    self.sample(weapon_name=string_name_weapon, status=string_img_modules)
        except KeyError:
            print(string_name_weapon)

    def sample(self, weapon_name, status):
        label.setText(f"weapon: {self.weapon_pattern[weapon_name][status]['Text']}")
        label.update()
        number = self.thread2.get_number()

        while True:
                time.sleep(0.01)

                if keyboard.is_pressed(self.btn_off):
                    label.setText("weapon: None")
                    label.update()
                    return 

                if self.thread2.get_number() == number:
                    if win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0 :
                        bt = self.get_bt()
                        rmb = self.get_rmb()
                        time1 = self.weapon_pattern[weapon_name][status][bt][rmb]['Time1']
                        x = self.weapon_pattern[weapon_name][status][bt][rmb]['X']
                        y = self.weapon_pattern[weapon_name][status][bt][rmb]['Y']
                        win32api.mouse_event(win32con.MOUSE_MOVED, int(x + 0.5), int(y + 0.5))
                        time.sleep(time1)
    
    
                

    
    def sample2(self, weapon_name, status):
        n = 0 
        label.setText(f"weapon: {self.weapon_pattern[weapon_name][status]['Text']}")
        label.update()

        bt = self.get_bt()
        rmb = self.get_rmb()
        tick = self.weapon_pattern[weapon_name][status][bt][rmb]['Tick']
        number = self.thread2.get_number()

        while True:
                time.sleep(0.01)
                if keyboard.is_pressed(self.btn_off):
                    label.setText("weapon: None")
                    label.update()
                    return 0

                if win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0 and self.thread2.get_number() == number:
                    if n < tick:
                        bt = self.get_bt()
                        rmb = self.get_rmb()
                        time1 = self.weapon_pattern[weapon_name][status][bt][rmb]['Time1']
                        x = self.weapon_pattern[weapon_name][status][bt][rmb]['X']
                        y = self.weapon_pattern[weapon_name][status][bt][rmb]['Y']
                        label.setText(f"weapon: {self.weapon_pattern[weapon_name][status]['Text']} {x} {y}")
                        win32api.mouse_event(win32con.MOUSE_MOVED, int(x + 0.5), int(y + 0.5))
                        time.sleep(time1)
                    else:
                        bt = self.get_bt()
                        rmb = self.get_rmb()
                        time2 = self.weapon_pattern[weapon_name][status][bt][rmb]['Time2']
                        x = self.weapon_pattern[weapon_name][status][bt][rmb]['X2']
                        y = self.weapon_pattern[weapon_name][status][bt][rmb]['Y2']
                        label.setText(f"weapon: {self.weapon_pattern[weapon_name][status]['Text']} {x} {y}")
                        win32api.mouse_event(win32con.MOUSE_MOVED, int(x + 0.5), int(y + 0.5))
                        time.sleep(time2)
                    n += 1 
                else:
                    n = 0 

class MyWindow(object):

    def setupUi(self, MainWindow):

        global label
        global label_2

        self.thread1 = Main()
        self.thread1.start()

        MainWindow.resize(250, 70)
        MainWindow.setWindowOpacity(0.7)
        MainWindow.setMinimumSize(QtCore.QSize(250, 70))
        MainWindow.setMaximumSize(QtCore.QSize(250, 70))
        MainWindow.setStyleSheet("background-color: rgb(63, 63, 63);\n""color: rgb(0,255,127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        label = QtWidgets.QLabel(self.centralwidget)
        label.setGeometry(QtCore.QRect(10, 10, 201, 16))
        label_2 = QtWidgets.QLabel(self.centralwidget)
        label_2.setGeometry(QtCore.QRect(10, 30, 201, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "-_-"))
        label.setText(_translate("MainWindow", "weapon: None"))
        label_2.setText(_translate("MainWindow", "this macro for Rust was created by ky1to"))

if __name__ == "__main__":
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.png'))
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
    ui = MyWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
