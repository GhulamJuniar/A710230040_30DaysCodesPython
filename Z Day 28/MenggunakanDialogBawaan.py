import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QInputDialog, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Contoh Dialog')
        
        button_message = QPushButton('Tampilkan Pesan')
        button_input = QPushButton('Masukan Teks')
        
        button_message.clicked.connect(self.show_message)
        button_input.clicked.connect(self.get_input)
        
        layout = QVBoxLayout()
        layout.addWidget(button_message)
        layout.addWidget(button_input)
        
        self.setLayout(layout)
    
    def show_message(self):
        QMessageBox.information(self, 'Info', 'Ini adalah pesan informatif.')
    
    def get_input(self):
        text, ok = QInputDialog.getText(self, 'Input', 'Masukkan teks:')
        if ok:
            print(f'Input pengguna: {text}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
