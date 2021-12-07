class Abonados:
    
    def __init__(self): 
        self.numero = "" 
        self.estado = "       "
        
    def getNumero(self): # con este metodo se obtiene el valor del input para el telefono
        return self.numero
    
    def getEstado(self): # con este metodo se obtiene el valor del input para el mensaje
        return self.estado
    
    def setNumero(self, _numero): # con este metodo se fija el valor del input para el telefono
        self.numero = _numero
        
    def setEstado(self, _estado): # con este metodo se fija el valor del input para el mensaje
        self.estado = _estado  