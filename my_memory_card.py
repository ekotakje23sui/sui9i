from PyQt5.QTCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QVBoxLayout,QMessageBox, QRadioButton
from random import randint


app = QApplication([])
main_win = QWidget
main_win = setWindowTitle('Memory Card')
main_win.resize(500, 500)

text_up = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')


RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()



layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)



RadioGroupBox.setLayout(layout_ans1)
  
  


AnsGroupBox = QGroupBox()
result = QLabel('Здесь правильно/неправильно')
layout_ans = QVBoxLayout()
layout_ans.addWidget(result)
AnsGroupBox.setLayout(layout_ans)
AnsGroupBox.hide()



layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)








