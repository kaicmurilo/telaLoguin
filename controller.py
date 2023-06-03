import os
import shutil
from PyQt5.QtWidgets import QFileDialog


class UploadController:
    def __init__(self, model):
        self.model = model
        self.view = None
        self.update_uploads_list = None

    def select_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Arquivos ZIP (*.zip)")
        file_path, _ = file_dialog.getOpenFileName(None, "Selecionar arquivo")

        if file_path:
            # Verificar se a pasta "uploads" existe, caso contrário, criar a pasta
            if not os.path.exists("uploads"):
                os.makedirs("uploads")

            # Obter apenas o nome do arquivo
            file_name = os.path.basename(file_path)

            # Construir o caminho de destino
            destination_path = os.path.join("uploads", file_name)

            # Copiar o arquivo para a pasta de destino
            shutil.copy(file_path, destination_path)

            self.model.set_file_path(destination_path)

            # Atualizar a lista de uploads e a exibição na tela
            uploads = self.list_uploads()
            if self.update_uploads_list and self.view:
                self.update_uploads_list(uploads)
                self.view.update_uploads_list(uploads)

    def list_uploads(self):
        uploads = []
        if os.path.exists("uploads"):
            uploads = os.listdir("uploads")
        return uploads

    def delete_selected_file(self):
        file_path = self.model.get_file_path()
        if file_path:
            os.remove(file_path)
            self.model.set_file_path(None)
            uploads = self.list_uploads()
            if self.update_uploads_list and self.view:
                self.update_uploads_list(uploads)
                self.view.update_uploads_list(uploads)
