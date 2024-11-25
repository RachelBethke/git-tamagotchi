from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Sprite(QLabel):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        pixmap = QPixmap('sprites/eggSprite.png')
        if pixmap.isNull():
            print("Failed to load image")
            return
        self.setPixmap(pixmap)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()
