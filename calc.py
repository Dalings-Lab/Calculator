import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


def warning(numero):
    if numero == '':
        numero.input.setText('Выберите цифры, ничего не выбрано')


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_operations = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_operations)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_7 = QPushButton("7", self)
        self.hbox_third.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_third.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_third.addWidget(self.b_9)

        self.b_0 = QPushButton("0", self)
        self.hbox_third.addWidget(self.b_0)

        # OPERATIONS
        self.b_plus = QPushButton("+", self)
        self.hbox_operations.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_operations.addWidget(self.b_minus)

        self.b_umnoj = QPushButton("x", self)
        self.hbox_operations.addWidget(self.b_umnoj)

        self.b_delen = QPushButton("/", self)
        self.hbox_operations.addWidget(self.b_delen)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        # Методы - обработчики
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_umnoj.clicked.connect(lambda: self._operation("x"))
        self.b_delen.clicked.connect(lambda: self._operation("/"))
        self.b_result.clicked.connect(self._result)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))

    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    def _operation(self, op):
        # Исключение на ввод числа, а не знака
        try:
            self.num_1 = float(self.input.text())
        except:
            return self.input.setText('Введите сначала число')

        self.op = op
        self.input.setText("")

    def _result(self):
        # Исключение пустого поля
        try:
            # Исключение на ввод числа, а не знака
            try:
                self.num_2 = float(self.input.text())
            except:
                return self.input.setText('Введите сначала число')

            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))

            elif self.op == "-":
                self.input.setText(str(self.num_1 - self.num_2))

            elif self.op == "x":
                self.input.setText(str(self.num_1 * self.num_2))

            elif self.op == "/":
                # Исключение деления на ноль
                if self.num_2 == 0:
                    return self.input.setText('ОШИБКА')

                return self.input.setText(str(self.num_1 / self.num_2))

        except:
            return self.input.setText('Введите корректное значение')


app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())
