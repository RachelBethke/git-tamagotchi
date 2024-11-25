import sys
from PyQt5.QtWidgets import QApplication
from sprite import Sprite

def main():
    app = QApplication(sys.argv)
    pet = Sprite()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()