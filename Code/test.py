import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from Model.fuma import Fuma
from Excel import ExcelLocal

class Controlador:
    def __init__(self):
        self.fuma = Fuma()
        self.creds = self.connect_sheets()
        self.sheet_service = build('sheets', 'v4', credentials=self.creds)
        self.drive_service = build('drive', 'v3', credentials=self.creds)
        self.folder_name = 'Formatos FUMA'
        self.file_name = 'FUMA'
        self.Local = ExcelLocal()
        self.formato = None

    def connect_sheets(self):
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        SERVICE_ACCOUNT_FILE = 'C:/Users/Mario/OneDrive/Escritorio/Documents/DocumentosPersonales/Repos git hub/Excel_Format_Manager/Code/credentials.json'
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        return creds

    def copy_and_rename_file(self):
        # Buscar la carpeta por nombre
        folder_query = f"name='{self.folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        print(f"Buscando carpeta '{self.folder_name}' con consulta: {folder_query}")
        folder_list = self.drive_service.files().list(q=folder_query).execute().get('files', [])
        if folder_list:
            folder = folder_list[0]
            print(f"Carpeta '{self.folder_name}' encontrada: {folder['name']} (ID: {folder['id']})")
            # Buscar el archivo dentro de la carpeta
            file_query = f"name='{self.file_name}' and '{folder['id']}' in parents and trashed=false"
            print(f"Buscando archivo con consulta: {file_query}")
            file_list = self.drive_service.files().list(q=file_query).execute().get('files', [])
            if file_list:
                file = file_list[0]
                print(f"Archivo encontrado: {file['name']} (ID: {file['id']})")
                # Generar el nombre para la copia con el ID obtenido
                new_file_name = f'FUMA_{self.fuma.get_id()}'
                # Hacer una copia del archivo
                copied_file = self.drive_service.files().copy(
                    fileId=file['id'],
                    body={'name': new_file_name, 'parents': [folder['id']]}
                ).execute()
                self.formato = copied_file['id']
                print("Archivo copiado y renombrado correctamente.")
            else:
                print("El archivo original no existe dentro de la carpeta especificada.")
        else:
            print(f"La carpeta '{self.folder_name}' especificada no existe.")
    
    def set_fuma(self):
        self.fuma = self.Local.fuma

    def obtener_datos(self, archivos):
        self.Local.obtener_id_desde_excel(archivos)
        self.Local.obtener_fecha_desde_excel(archivos)
        self.Local.obtener_solicitante_desde_excel(archivos)
        self.Local.obtener_departamento_desde_excel(archivos)
        self.Local.obtener_asignacion_desde_excel(archivos)
        self.Local.obtener_unidadnegocio_desde_excel(archivos)
        self.Local.obtener_proyecto_desde_excel(archivos)
        self.Local.obtener_productos_desde_excel(archivos)
        self.set_fuma()

    def actualizar_celda_k3(self):
        id_value = self.fuma.get_id()
        range_ = 'K2'
        self.actualizar_celda(range_,id_value)
    
    def actualizar_celda_k2(self):
        # Obtener la fecha desde self.fuma
        fecha_value = self.fuma.get_fecha()
        range_ = 'K3'
        self.actualizar_celda(range_,fecha_value)

    def actualizar_celda_k5(self):
        # Obtener la fecha desde self.fuma
        fecha_value = self.fuma.get_departamento()
        range_ = 'K5'
        self.actualizar_celda(range_,fecha_value)

    def actualizar_celda_k6(self):
        # Obtener la fecha desde self.fuma
        fecha_value = self.fuma.get_unidadnegocio()
        range_ = 'K6'
        self.actualizar_celda(range_,fecha_value)

    def actualizar_celda_k7(self):
        # Obtener la fecha desde self.fuma
        fecha_value = self.fuma.get_proyecto()
        range_ = 'K7'
        self.actualizar_celda(range_,fecha_value)
    
    def actualizar_celda_k8(self):
        # Obtener la fecha desde self.fuma
        fecha_value = self.fuma.get_solicitante()
        range_ = 'K8'
        self.actualizar_celda(range_,fecha_value)
    
    def actualizar_celda_asignacion(self):
        # Obtener la fecha desde self.fuma
        fecha_value = self.fuma.get_asignacion()
        if fecha_value == 'Instalación':
            range_ = 'D3'
        elif fecha_value == 'RMA':
            range_ = 'D7'
        elif fecha_value == 'Manufactura Interna' or fecha_value == 'Manufactura Externa':
            range_ = 'D5'
        elif fecha_value == 'Traspaso entre Almacenes':
            range_ = 'D6'
        else:
            range_ = 'D9'
        caracter = '☑'
        self.actualizar_celda(range_,caracter)
    
    def actualizar_productos(self):
        productos = self.fuma.get_productos()
        for indice, producto in enumerate(productos):
            celda = f'C{12 + indice}'
            self.actualizar_celda(celda, producto)
            celda = f'G{12 + indice}'
            cantidad = None
            while not cantidad:
                cantidad = 12
            self.actualizar_celda(celda, cantidad)

    
    def actualizar_celda(self,strn,valor):
        if self.formato:
            try:
                # Obtener la fecha desde self.fuma
                fecha_value = valor
                
                # Actualizar la celda K4 en el archivo copiado
                sheet_id = self.formato
                range_ = strn  # Cambiar esto según la celda que desees actualizar
                value_input_option = 'USER_ENTERED'
                values = [[fecha_value]]
                body = {'values': values}

                result = self.sheet_service.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range=range_,
                    valueInputOption=value_input_option,
                    body=body
                ).execute()
                
                print(f"Celda",strn,"actualizada correctamente con la fecha: {fecha_value}")
            except Exception as e:
                print(f"Error al actualizar la celda ",strn,": {e}")
        else:
            print("No se ha copiado ningún archivo para actualizar.")
    
    def actualizar_celdas(self):
        self.actualizar_celda_k3()
        self.actualizar_celda_k2()
        self.actualizar_celda_k5()
        self.actualizar_celda_k6()
        self.actualizar_celda_k7()
        self.actualizar_celda_k8()
        self.actualizar_celda_asignacion()
        self.actualizar_productos()
    
    def empezarMaquinaria(self,archivos):
        for archivo in archivos:
            while True:
                self.obtener_datos(archivo)
                self.copy_and_rename_file()
                #Mostrar parte de cantidad
                self.actualizar_celdas()
                #Ocultar

                if(self.Local.revizar_celda_abajo(archivo)):
                    break
            
            self.Local.mover_archivo(archivo)


ctrl = Controlador()
archivos = ctrl.Local.obtener_archivos()
ctrl.empezarMaquinaria(archivos)