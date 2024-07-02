import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Contoh Widget')
        
        layout = QVBoxLayout()
        
        label = QLabel('Nama:')
        edit = QLineEdit()
        button = QPushButton('Submit')
        
        layout.addWidget(label)
        layout.addWidget(edit)
        layout.addWidget(button)
        
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
