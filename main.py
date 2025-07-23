import sys
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import pyqtSlot, QObject, pyqtSignal
from PyQt6.QtWidgets import QApplication



class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)
        
    
    @pyqtSlot()
    def powers(self):
        QApplication.instance().quit()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    controller  = MainWindow()
    engine.rootContext().setContextProperty("controller", controller)
    
    engine.load("main.qml")
    sys.exit(app.exec())