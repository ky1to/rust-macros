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



sens = 0.8/0.8

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

class Thread(QThread):

    global label
    global label_2

    def get_cursor_flags(self):
        info = CURSORINFO()
        info.cbSize = ctypes.sizeof(info)
        self.GetCursorInfo(ctypes.byref(info))
        return info.flags

    def run(self):

        self.GetCursorInfo = ctypes.windll.user32.GetCursorInfo
        self.GetCursorInfo.argtypes = [ctypes.POINTER(CURSORINFO)]

        while True:
            time.sleep(0.1)
            if keyboard.is_pressed("f3"):
                self.auto_identifier()   

    def auto_identifier(self):
        pyautogui.press("tab")
        time.sleep(0.01)
        img_name_weapon = ImageGrab.grab((650, 70, 1300, 150))
        img_modules = ImageGrab.grab((680, 380, 950, 460))
        print(type(img_modules))
        pyautogui.press("tab")
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe' 
        string_name_weapon = pytesseract.image_to_string(img_name_weapon, lang="rus")
        string_name_weapon = ' '.join(string_name_weapon.split())
        print(f"!{string_name_weapon}!")

        needle = cv2.imread('holo.png')
        result = cv2.matchTemplate(np.array(img_modules), needle, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        locations = []
        for y, x in zip(*np.where(result >= threshold)):
            locations.append((x, y))
        if locations == []:
            print("0")
            string_img_modules = ""
        else:
            print("1")
            string_img_modules = "holo"
        locations = []

        if string_name_weapon == """ШТУРМОВАЯ ВИНТОВКА""":
            if string_img_modules == "holo":
                self.ak47_rust_holo()
            else:
                self.ak47_rust()

        elif string_name_weapon == """МР5А4""":
            if string_img_modules == "holo":
                self.mp5_rust_holo()
            else:
                self.mp5_rust()

        elif string_name_weapon == """ПИСТОЛЕТ-ПУЛЕМЕТ ТОМПСОНА""":
            if string_img_modules == "holo":
                self.tomson_rust_holo()
            else:
                self.tomson_rust()

        elif string_name_weapon == """ПОЛУАВТОМАТИЧЕСКАЯ ВИНТОВКА""":
             self.berdanka_rust()

        elif string_name_weapon == """РЕВОЛЬВЕР ПИТОН""":
             self.python_rust()

        elif string_name_weapon == """САМОДЕЛЬНЫЙ ПИСТОЛЕТ-ПУЛЕМЕТ""":
            if string_img_modules == "holo":
                self.smg_holo_rusr()
            else:
                self.smg_rusr()

        elif string_name_weapon == """ПОЛУАВТОМАТИЧЕСКИЙ ПИСТОЛЕТ""":
             self.peshka_rusr()
        
        elif string_name_weapon == """САМОДЕЛЬНЫЙ РУЧНОЙ ПУЛЕМЁТ""":
            if string_img_modules == "holo":
                self.fake_m249_holo_rust()
            else:
                self.fake_m249_rust()
        
        elif string_name_weapon == """ПУЛЕМЁТ М249""":
            if string_img_modules == "holo":
                self.m249_holo_rust()
            else:
                self.m249_rust()

    def m249_holo_rust(self):
        label.setText("weapon: m249 (holo)")
        label.update()
        n = 0 
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                elif win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    print(n)
                    if n < 91:
                        win32api.mouse_event(win32con.MOUSE_MOVED, -5, 11)
                        time.sleep(0.04)
                    else:
                        win32api.mouse_event(win32con.MOUSE_MOVED, 0, 11)
                        time.sleep(0.04)
                    n += 1 
                else:
                    n = 0 

    def m249_rust(self):
        label.setText("weapon: m249")
        label.update()
        n = 0 
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                elif win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    print(n)
                    if n < 91:
                        win32api.mouse_event(win32con.MOUSE_MOVED, -4, 8)
                        time.sleep(0.031)
                    else:
                        win32api.mouse_event(win32con.MOUSE_MOVED, 0, 9)
                        time.sleep(0.031)
                    n += 1 
                else:
                    n = 0 

    def fake_m249_holo_rust(self):
        label.setText("weapon: fake m249 (holo)")
        label.update()
        n = 0 
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                elif win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    print(n)
                    if n < 92:
                        win32api.mouse_event(win32con.MOUSE_MOVED, 5, 10)
                        time.sleep(0.031)
                    else:
                        win32api.mouse_event(win32con.MOUSE_MOVED, 0, 9)
                        time.sleep(0.031)
                    n += 1 
                else:
                    n = 0 

    def fake_m249_rust(self):
        label.setText("weapon: fake m249")
        label.update()
        n = 0 
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                elif win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    print(n)
                    if n < 92:
                        win32api.mouse_event(win32con.MOUSE_MOVED, 4, 9)
                        time.sleep(0.033)
                    else:
                        win32api.mouse_event(win32con.MOUSE_MOVED, 0, 8)
                        time.sleep(0.033)
                    n += 1 
                else:
                    n = 0 

    def peshka_rusr(self):
        label.setText("weapon: peshka")
        label.update()
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                if win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    win32api.mouse_event(win32con.MOUSE_MOVED, 0, 2)
                    time.sleep(0.008)

    def smg_rusr(self):
        label.setText("weapon: SMG")
        label.update()
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                if win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    win32api.mouse_event(win32con.MOUSE_MOVED, 0, 2)
                    time.sleep(0.008)
    
    def smg_holo_rusr(self):
        label.setText("weapon: SMG (holo)")
        label.update()
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                if win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    win32api.mouse_event(win32con.MOUSE_MOVED, 0, 3)
                    time.sleep(0.008)

    def ak47_rust(self):
        label.setText("weapon: AK47")
        label.update()
        n = 0 
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                elif win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    print(n)
                    if n < 13:
                        win32api.mouse_event(win32con.MOUSE_MOVED, -3, 10)
                        time.sleep(0.04)
                    else:
                        win32api.mouse_event(win32con.MOUSE_MOVED, -7, 10)
                        time.sleep(0.04)
                    n += 1 
                else:
                    n = 0 

    def ak47_rust_holo(self):
        label.setText("weapon: AK47 (holo)")
        label.update()
        n = 0 
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                elif win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    print(n)
                    if n < 13:
                        win32api.mouse_event(win32con.MOUSE_MOVED, -4, 12)
                        time.sleep(0.04)
                    else:
                        win32api.mouse_event(win32con.MOUSE_MOVED, -8, 13)
                        time.sleep(0.044)

                    n += 1 
                else:
                    n = 0 
    

    def python_rust(self):
        label.setText("weapon: Python")
        label.update()
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                if win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    win32api.mouse_event(win32con.MOUSE_MOVED, 0, 13)
                    time.sleep(0.01)

    def berdanka_rust(self):
        label.setText("weapon: Berdanka")
        label.update()
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                if win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    win32api.mouse_event(win32con.MOUSE_MOVED, 0, 4)
                    time.sleep(0.01)

    def tomson_rust(self):
        label.setText("weapon: Tomson")
        label.update()
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                if win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    win32api.mouse_event(win32con.MOUSE_MOVED, 0, 2)
                    time.sleep(0.015)

    def tomson_rust_holo(self):
        label.setText("weapon: Tomson (holo)")
        label.update()
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                if win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    win32api.mouse_event(win32con.MOUSE_MOVED, 0, 3)
                    time.sleep(0.015)
    
    def mp5_rust(self):
        label.setText("weapon: MP5")
        label.update()
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                if win32api.GetKeyState(0x01)<0 and self.get_cursor_flags() == 0: #if mouse left button is pressed
                    win32api.mouse_event(win32con.MOUSE_MOVED, 0, 3)
                    time.sleep(0.011)

    def mp5_rust_holo(self):
        label.setText("weapon: MP5 (holo)")
        label.update()
        while True:
                time.sleep(0.01)
                if keyboard.is_pressed("u"):
                    label.setText("weapon: None")
                    label.update()
                    return
                if win32api.GetKeyState(0x01) and self.get_cursor_flags() == 0<0: #if mouse left button is pressed
                    win32api.mouse_event(win32con.MOUSE_MOVED, 0, 4)
                    time.sleep(0.012)

class MyWindow(object):

    def setupUi(self, MainWindow):

        global label
        global label_2

        self.thread = Thread()
        self.thread.start()

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
        MainWindow.setWindowTitle(_translate("MainWindow", "SBERBANK"))
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