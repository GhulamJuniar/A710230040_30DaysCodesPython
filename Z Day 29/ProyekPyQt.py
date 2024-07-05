import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulator")
        self.setGeometry(100, 100, 300, 300)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout(self.centralWidget)
        self.input_line = QLineEdit(self)
        self.input_line.setAlignment(Qt.AlignRight)
        self.input_line.setFixedHeight(50)
        self.layout.addWidget(self.input_line)

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0, 1, 4)
        ]

        for button_data in buttons:
            if len(button_data) == 3:
                btn_text, x, y = button_data
                rowspan, colspan = 1, 1
            else:
                btn_text, x, y, rowspan, colspan = button_data
            
            button = QPushButton(btn_text)
            button.clicked.connect(self.on_click)
            self.grid_layout.addWidget(button, x, y, rowspan, colspan)

    def on_click(self):
        button = self.sender()
        button_text = button.text()

        if button_text == 'C':
            self.input_line.clear()
        elif button_text == '=':
            try:
                result = eval(self.input_line.text())
                self.input_line.setText(str(result))
            except Exception as e:
                self.input_line.setText("Error")
        else:
            self.input_line.setText(self.input_line.text() + button_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
