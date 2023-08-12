from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
app = QApplication([])
btn_Menu = QPushButton('Меню')
btn_Sleep = QPushButton('Відпочити')
box_Minutes = QSpinBox()
box_Minutes(30)
btn_OK = QPushButton('Відповісти')
question = QLabel('')
RadioGroupBox = QGroupBox('Варіанти відповіді')
RadioGroup = QButtonGroup
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
AnsGroupBox = QGroupBox('Результат туксту')
Result = QLabel('')

correct = QLabel('')
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans2.addWidget(rbtn_3)
layout_ans2.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_res