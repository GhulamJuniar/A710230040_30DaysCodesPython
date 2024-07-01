import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Contoh Layout PyQt")

      
        hbox_layout = QHBoxLayout()
        vbox_layout = QVBoxLayout()
        grid_layout = QGridLayout()

       
        hbox_layout.addWidget(QPushButton('Tombol 1'))
        hbox_layout.addWidget(QPushButton('Tombol 2'))
        hbox_layout.addWidget(QPushButton('Tombol 3'))

       
        vbox_layout.addWidget(QLabel('Label 1'))
        vbox_layout.addWidget(QLabel('Label 2'))
        vbox_layout.addWidget(QLabel('Label 3'))

  
        grid_layout.addWidget(QLabel('Tombol Grid  1'), 0, 0)
        grid_layout.addWidget(QPushButton('Tombol Grid 1'), 0, 1)
        grid_layout.addWidget(QLabel('Tombol Grid 2'), 1, 0)
        grid_layout.addWidget(QPushButton('Tombol Grid 2'), 1, 1)


        main_layout = QVBoxLayout()
        main_layout.addLayout(hbox_layout)
        main_layout.addLayout(vbox_layout)
        main_layout.addLayout(grid_layout)

        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
