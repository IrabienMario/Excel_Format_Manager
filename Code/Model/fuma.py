class Fuma:
    def __init__(self):
        self.id = 0
        self.fecha = ''
        self.solicitante = ''
        self.departamento = ''
        self.asignacion = ''
        self.unidadnegocio = ''
        self.proyecto = ''
        self.productos = []

    def set_id(self, nuevo_id):
        self.id = nuevo_id

    def set_fecha(self, fecha):
        self.fecha = fecha
    
    def set_solicitante(self, solicitante):
        self.solicitante = solicitante
    
    def set_departamento(self, departamento):
        self.departamento = departamento

    def set_asignacion(self, asignacion):
        self.asignacion = asignacion
    
    def set_unidadnegocio(self, unidadnegocio):
        self.unidadnegocio = unidadnegocio
    
    def set_proyecto(self, proyecto):
        self.proyecto = proyecto

    def set_productos(self, producto_string):
        productos = producto_string.split('/')
        self.productos = productos

    def get_id(self):
        return self.id
    
    def get_fecha(self):
        return self.fecha
    
    def get_solicitante(self):
        return self.solicitante
    
    def get_departamento(self):
        return self.departamento
    
    def get_asignacion(self):
        return self.asignacion
    
    def get_unidadnegocio(self):
        return self.unidadnegocio
    
    def get_proyecto(self):
        return self.proyecto
    
    def get_productos(self):
        return self.productos

    def get_solicitante(self):
        return self.solicitante

    
