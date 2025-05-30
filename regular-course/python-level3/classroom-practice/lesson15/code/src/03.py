import datetime
import os
from PyQt5.Qt import *
from utils import CSVHandler


class HomeworkWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.sub = QLabel("科目")
        self.subEdit = QLineEdit()
        self.con = QLabel("内容")
        self.conEdit = QLineEdit()
        self.addBtn = QPushButton("添加作业")
        self.layout.addWidget(self.sub, 0, 0)
        self.layout.addWidget(self.subEdit, 0, 1)
        self.layout.addWidget(self.con, 0, 2)
        self.layout.addWidget(self.conEdit, 0, 3)
        self.layout.addWidget(self.addBtn, 0, 4)
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(['日期', '科目', '内容', '状态'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table, 1, 0, 1, 5)
        self.addBtn.clicked.connect(self.add)
        self.data = []
        self.show()
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.showMenu)
        # 老师提前预留的修改配置 设置表格每次选中为整行
        # self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 老师提前预留的修改配置  设置单元格不可编辑
        # self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showMenu(self, pos):

    # 创建菜单

    # 创建选项并添加到菜单中

    # 将选项添加到菜单中

    # 显示菜单

    def addRow(self, rowData):
        count = self.table.rowCount()
        self.table.insertRow(count)
        for col in range(len(rowData)):
            item = QTableWidgetItem(rowData[col])
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(count, col, item)

    def show(self):
        if os.path.exists('homeworks.csv'):
            self.data = CSVHandler.load('homeworks.csv')
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        for hw in self.data:
            if hw[0] == today:
                self.addRow(hw)

    def add(self):
        date_today = datetime.datetime.today().strftime("%Y-%m-%d")
        subject = self.subEdit.text()
        content = self.conEdit.text()
        if not subject or not content:
            return
        hw = [date_today, subject, content, '未完成']
        self.data.append(hw)
        CSVHandler.save('homeworks.csv', self.data)
        self.addRow(hw)
        self.subEdit.clear()
        self.conEdit.clear()


app = QApplication([])
window = QMainWindow()
window.setWindowTitle('记作业')
widget = HomeworkWidget()
window.setCentralWidget(widget)
window.showMaximized()
app.exec_()
