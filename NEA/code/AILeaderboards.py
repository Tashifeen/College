from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QWidget, QScrollArea
from database import get_leaderboard

class LeaderboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Leaderboard")
        self.setGeometry(100, 100, 400, 300)
        
        # Fetch leaderboard data
        data = get_leaderboard()

        # Set up scroll area
        scroll = QScrollArea()
        widget = QWidget()
        layout = QVBoxLayout()

        # Set up table
        table = QTableWidget()
        table.setRowCount(len(data))
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Username", "Score", "Time Taken"])

        # Populate the table
        for row, (username, score, time_taken) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(username))
            table.setItem(row, 1, QTableWidgetItem(str(score)))
            table.setItem(row, 2, QTableWidgetItem(str(time_taken)))

        layout.addWidget(table)
        widget.setLayout(layout)
        scroll.setWidget(widget)
        self.setCentralWidget(scroll)

