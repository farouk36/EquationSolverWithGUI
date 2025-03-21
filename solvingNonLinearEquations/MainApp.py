from main import EquationSolverApp
from non_linear_solver import NonLinearSolver
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
)
from PyQt5.QtCore import Qt
import sys

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Application")
        self.setGeometry(200, 200, 450, 450)

        # Set background color
        self.setStyleSheet("background-color: #000000; font-family: Arial, sans-serif;")

        # Welcome label
        self.label = QLabel("Welcome to the Equations Solver!")
        self.label.setStyleSheet("font-size: 24px; color: #55e339; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)

        # Choose label
        self.choose_label = QLabel("Choose the type of equations:")
        self.choose_label.setStyleSheet("font-size: 18px; color: #249c06;")
        self.choose_label.setAlignment(Qt.AlignCenter)

        # Create buttons
        self.linear_button = QPushButton("Linear Equations", self)
        self.nonlinear_button = QPushButton("Non-Linear Equations", self)

        # Style the buttons
        self.set_button_styles()

        # Connect buttons to their respective actions
        self.linear_button.clicked.connect(self.open_linear_window)
        self.nonlinear_button.clicked.connect(self.open_nonlinear_window)

        # Create layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        layout.addWidget(self.label)
        layout.addWidget(self.choose_label)
        layout.addWidget(self.linear_button)
        layout.addWidget(self.nonlinear_button)
        layout.setContentsMargins(40, 40, 40, 40)

        self.setLayout(layout)

    def set_button_styles(self):
        """Apply custom styles to the buttons."""
        button_style = """
            QPushButton{
                background-color: #181a18;  /* Background color */
                color: #249c06;                /* Text color */
                border: 2px solid #181a18;      /* Border color and width */
                border-radius: 10px;         /* Rounded borders */
                padding: 5px;                /* Optional padding */
                height: 20px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #249c06;   /* Background color on hover */
                color: #ccc;
                border: 2px solid #249c06;
            }
        """

        
        # Apply style to both buttons
        self.linear_button.setStyleSheet(button_style)
        self.nonlinear_button.setStyleSheet(button_style)

    def open_linear_window(self):
        """
        This method will open the Linear Equations Solver window.
        """
        self.linear_window = EquationSolverApp()  # Assuming EquationSolverApp is the class to solve linear equations
        self.linear_window.return_to_main.connect(self.show)
        self.linear_window.open_non_linear_solver.connect(self.open_nonlinear_window)
        self.linear_window.show()
        self.close()  # Close the main window after opening the linear solver

    def open_nonlinear_window(self):
        """
        This method will open the Non-Linear Equations Solver window.
        """
        
        self.nonlinear_window = NonLinearSolver()  # Assuming NonLinearSolver is the class to solve non-linear equations
        self.nonlinear_window.return_to_main.connect(self.show)
        self.nonlinear_window.open_equation_solver.connect(self.open_linear_window)
        self.nonlinear_window.show()
        self.close()  # Close the main window after opening the non-linear solver


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    main_app = MainApp()
    main_app.show()

    sys.exit(app.exec_())
