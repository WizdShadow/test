import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Панель задач PyQt6")
        self.setGeometry(100, 100, 800, 600)
        
        toolbar = QToolBar("Моя панель задач")
        self.addToolBar(toolbar)
        self.addToolBar(Qt.ToolBarArea.BottomToolBarArea, toolbar)
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setStyleSheet("""QToolBar { border: none;
                              border-top: 3px solid white;

                              }""")
        
        toolbar2 = QToolBar("")
        self.addToolBar(toolbar2)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar2)
        
        power = QPushButton(QIcon("power.png"), "", self)
        btn1 = QPushButton(QIcon("icon1.png"), "Кнопка 1", self)
        btn2 = QPushButton(QIcon("icon2.png"), "Кнопка 2", self)

        
        toolbar.addWidget(power)
        toolbar.addWidget(btn1)
        toolbar.addWidget(btn2)

        
        btn1.clicked.connect(self.on_btn1_click)
        btn2.clicked.connect(self.on_btn2_click)
        power.clicked.connect(self.power)
    
    def on_btn1_click(self):
        print("Кнопка 1 нажата")
    
    def on_btn2_click(self):
        print("Кнопка 2 нажата")
        
    def power(self):
        exit()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())