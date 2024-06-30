import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    
    window = QWidget()
    window.setWindowTitle('Hello PyQt')
    window.setGeometry(100, 100, 300, 200)  # (posisi_x, posisi_y, lebar, tinggi)
    
    window.show()
    sys.exit(app.exec_())
