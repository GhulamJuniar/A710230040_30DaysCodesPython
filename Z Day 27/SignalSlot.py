import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Contoh Signal Slot')
        
        button = QPushButton('Tekan Di Sini')
        button.clicked.connect(self.show_message)
        
        layout = QVBoxLayout()
        layout.addWidget(button)
        
        self.setLayout(layout)
    
    def show_message(self):
        QMessageBox.information(self, 'Info', 'Tombol telah di tekan!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
