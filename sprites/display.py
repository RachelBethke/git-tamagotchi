from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
import sys
import random

class SpriteWidget(QWidget):
    def __init__(self, parent=None):
        super(SpriteWidget, self).__init__(parent)

        # window flags and attributes
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint |
            Qt.WindowDoesNotAcceptFocus |
            Qt.Window
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFocusPolicy(Qt.NoFocus)

        # pixmap label creation
        self.label = QLabel(self)
        pixmap = QPixmap('sprites/sprite_images/eggSprite.png')
        if pixmap.isNull():
            print("sprite didn't load")
            return
        else:
            print("sprite loaded")

        self.label.setPixmap(pixmap)
        self.label.adjustSize()
        self.setFixedSize(pixmap.size()) #size of the widget to the size of the pixmap
        self.move(100, 100) #window pos 
        self.timer = QTimer()
        #self.timer.timeout.connect(self.move_sprite)
        self.timer.start(1000) #moves every second

    # def move_sprite(self):
    #     screen_geometry = QApplication.primaryScreen().geometry()
    #     x = random.randint(0, screen_geometry.width() - self.width())
    #     y = random.randint(0, screen_geometry.height() - self.height())
    #     self.move(x, y)

    def focusOutEvent(self, event):
        event.ignore()

def show_sprite():
    """Show the sprite on home screen window"""
    # init app
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    sprite = SpriteWidget()
    sprite.show()
    app.sprite = sprite #ref so there isn't garbage collection
    sys.exit(app.exec_()) # event loop

if __name__ == '__main__':
    show_sprite()
