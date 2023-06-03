from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
)
from PyQt5.QtCore import Qt
from model import UploadModel
from controller import UploadController  # Adicionado o import


import os
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
    QHBoxLayout,
)


class UploadView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Upload Application")

        self.file_label = QLabel("Nenhum arquivo selecionado.")
        self.upload_button = QPushButton("Selecionar arquivo")
        self.upload_button.clicked.connect(self.controller.select_file)

        self.list_label = QLabel("Uploads:")

        self.delete_button = QPushButton("Excluir")
        self.delete_button.clicked.connect(self.controller.delete_selected_file)
        self.delete_button.setEnabled(False)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.file_label)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.upload_button)
        button_layout.addWidget(self.delete_button)
        self.layout.addLayout(button_layout)

        self.layout.addWidget(self.list_label)

        self.setLayout(self.layout)

    def update_file_label(self):
        file_path = self.controller.model.get_file_path()
        self.file_label.setText(
            file_path if file_path else "Nenhum arquivo selecionado"
        )
        self.delete_button.setEnabled(bool(file_path))

    def update_uploads_list(self, uploads):
        uploads_text = "\n".join(uploads)
        self.list_label.setText(f"Uploads:\n{uploads_text}")


def run_application():
    app = QApplication([])
    model = UploadModel()
    controller = UploadController(model)
    view = UploadView(controller)

    controller.view = view
    controller.update_file_label = view.update_file_label
    controller.update_uploads_list = view.update_uploads_list

    # Listar os uploads e atualizar a lista na tela
    uploads = controller.list_uploads()
    view.update_uploads_list(uploads)

    view.show()
    app.exec_()
