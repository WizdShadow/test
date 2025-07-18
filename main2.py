from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QIcon
import sys

class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Панель задач PyQt6")
        self.setGeometry(100, 100, 800, 600)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        
        self.power = QPushButton(QIcon("file/power.png"), "", self)
        
        toolbar = QToolBar("Моя панель задач")
        self.addToolBar(toolbar)
        self.addToolBar(Qt.ToolBarArea.BottomToolBarArea, toolbar)
        toolbar.setMovable(False)   
        toolbar.setFloatable(False)
        toolbar.addWidget(self.power)
        toolbar.setStyleSheet("""
           QToolBar {
            background: transparent;
                }
            """)
        
        self.player = QMediaPlayer()
        self.player.setSource(QUrl.fromLocalFile("file/backgorund.mp4"))
        self.video_widget = QVideoWidget()
        self.player.setVideoOutput(self.video_widget)
        self.player.setLoops(-1)
        self.video_widget.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatioByExpanding)

        
        
        self.setCentralWidget(self.video_widget)
        self.showFullScreen()
        self.player.play()
        
        self.power.clicked.connect(self.powers)
        
    def powers(self):
        exit()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindows()
    window.show()
    sys.exit(app.exec())