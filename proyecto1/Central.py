from Abonado import Abonados 
from tonos import tono 
import time 
import random
import pandas as pd 
import pygame 
from time import sleep

pygame.init()
pygame.mixer.init #Se inicilializa la libreria pygame para la reproduccion de audios

class Central:
    def __init__(self):
        self.abonado = Abonados()
        self.Libres = []
        self.FS = []
        self.Ocupados = []
        self.emisor = Abonados()
        self.duracion_llamada = 0.0
        self.tarifa = 1 # Establezco el valor de la llamada a 1 peso el segundo
        self.estado = ["./Tonos/Marcando.wav" ,
                       "./Tonos/Ocupado.wav" , 
                       "./Tonos/Abonado_Fuera.mp3" ,
                       "./Tonos/Silencio.mp3" 
                       ] 
                       #Carga de los audios a reproducir segun el estado del abonado
        self.conversacion = ["./Audios/Conversacion1.mp3" , "./Audios/Conversacion2.mp3" , 
        "./Audios/Conversacion3.mp3" , "./Audios/Conversacion4.mp3"]      
        
    def iniciarAbonados(self): 
        for i in range(1, 21):
            self.abonado.setNumero(int(5700 + int(i)))
            self.Libres.append(self.abonado.getNumero()) #Establezco los numeros que quedaran libres
            
        for i in range(1, 4):
            fs = random.choice(self.Libres) #Establezco los numeros que se encontraran fuera de servicio
            self.FS.append(fs) #
            self.Libres.remove(fs)
        
        for i in range(1, 6):
            oc = random.choice(self.Libres) #Establezco los numeros ocupados
            self.Ocupados.append(oc)
            self.Libres.remove(oc)
        # Muestro los numeros que estan libres, ocupados y fuera de servicio    
        print("Teléfonos Libres: " + str(self.Libres))
        print("Teléfonos Ocupados: " + str(self.Ocupados))
        print("Teléfonos Fuera de Servicio: " + str(self.FS))
        
    def iniciandoLlamada(self):
        global num 
        flag = False
        while (flag == False):
            print(" ")
            num = int(input("Por favor ingrese su número de teléfono: ")) # Le pido al usuario su numero telefonico
            self.num_mio = num
            if self.num_mio in self.Libres: #Se revisa que el numero se encuentre en la lista de disponibles
                print("Su numero es: ", num)
                self.emisor.setNumero(num)
                flag = True
            else:
                print(" ") 
                print("Por favor ingrese un número que se encuentre disponible")
        flag = False
        while (flag == False):
            llam = int(input("Por favor ingrese el número que desea llamar: ")) #Se pide al usuario el numero a llamar
            llamt = map(int, str(llam)) # mapeo el numero
            tono(llamt) #Llamo a la instancia tono para reproducirse en la marcacion de las teclas
            if num != llam: # Se revisa que no se llame a su propio numero
                self.num_llam = llam
                if self.num_llam in self.Libres: #Verificamos que se llame a un numero dsiponible
                    info = pd.read_excel('abonados.xlsx')
                    df = pd.DataFrame(info)
                    nom = df[df['Numero'] == llam]['Nombre'] # Busco el nombre en el registro de abonados
                    self.abonado.setEstado("Disponible")
                    print("-----> Llamada en curso...")
                    print("-----> Marcando a", nom.values)
                    print("----->", llam)
                    pygame.mixer.music.load(self.estado[0]) #Se reproduce el audio para un numero libre
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy(): 
                        sleep(1)
                    ti = time.time() # Se registra el tiempo de inicio de la llamada
                            
                    pygame.mixer.music.load(random.choice(self.conversacion)) # reproduzco una conversacion aleatoria
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy(): #Comprobamos si el audio se esta reproduciendo
                        sleep(1)
                    to = time.time() ## Se registra el tiempo final de la llamada
                    print("----- Fin de la llamada -------")
                    self.duracion_llamada = round(to - ti, 0) #Se calcula la duracion de la llamada y se redondea
                    print("----- duracion de la llamada:", self.duracion_llamada, "segundos-------")
                    time.sleep(3) 
                    flag = True
                else:
                    if self.num_llam in self.Ocupados: # Se revisa si se esta llamando a un numero ocupado
                        self.abonado.setEstado("Ocupado ")
                        print("El número al que llama se encuentra ocupado")
                        pygame.mixer.music.load(self.estado[1]) # reproduzco el audio para un abonado ocupado
                        pygame.mixer.music.play()
                        while pygame.mixer.music.get_busy():
                            sleep(1)
                                
                    else:
                        if self.num_llam in self.FS: # Reviso si estan llamando a un abonado fuera de servicio
                            self.abonado.setEstado("F.Servicio") 
                            print("El número al que llama se encuentra fuera de servicio")
                            pygame.mixer.music.load(self.estado[2]) #Reproduzco el audio para un abonado Fuera de Servicio
                            pygame.mixer.music.play() 
                            while pygame.mixer.music.get_busy():
                                sleep(1)
                                
                        else:
                            print('El numero al que se llama no pertenece a la central telefonica')
                            self.abonado.setEstado("Fuera de servicio")
                            pygame.mixer.music.load(random.choice(self.estado[2])) #Se reproduce el tono para un abonado fuera de servicio
                            pygame.mixer.music.play() 
                            while pygame.mixer.music.get_busy(): 
                                sleep(1)
            else:
                print("No se puede marcar a su propio numero") 
                self.abonado.setEstado("F.Servicio")
                self.numero_llamar = " "
                pygame.mixer.music.load(self.estado[3])
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy(): 
                    sleep(1) 
                self.numero_llamar = self.emisor.getNumero()
                    
    def registrarLlamada(self):
        info = pd.read_excel('abonados.xlsx')
        df = pd.DataFrame(info) # leemos el excel del registro y le agregamos aun DataFrame
        num_mio = df[df['Numero'] == self.num_mio]['#llamadas'] # buscamos el registro de numero de llamadas
        num_mio = num_mio + 1
        timellam = df[df['Numero'] == self.num_mio]['segundos'] # buscamos el registro de segundos
        timellam = timellam + self.duracion_llamada
        df.at[self.num_mio - 5701, '#llamadas'] = num_mio # agregamos el nuevo registro al df 
        df.at[self.num_mio - 5701, 'segundos'] = timellam
        df.drop(['Unnamed: 0'], axis='columns', inplace=True) # Eliminamos una columna que nos genera
        df.to_excel('abonados.xlsx', sheet_name='Registro') # guardamos el df en el excel
        
    def consultarFactura(self):
        con = False
        while (con == False):
            lin = int(input("Por favor ingrese su linea telefonica: "))
            if 5700 < lin <= 5720:
                info = pd.read_excel('abonados.xlsx')
                df = pd.DataFrame(info) # leemos el excel del registro y le agregamos a un DataFrame
                num_mio = df[df['Numero'] == lin]['#llamadas']
                timesllam = df[df['Numero'] == lin]['segundos']
                abon = df[df['Numero'] == lin]['Nombre'] # buscamos la informacion en el registro
                print(f"Bienvenido {abon.values}")
                print(f"Su numero es {lin}") 
                print(f"Usted ha realizado {num_mio.values} llamadas")
                print(f"con un total de {timesllam.values} segundos") 
                time.sleep(8) 
                con = True
            else:
                print('Ingrese un numero valido')
            
    def Facturacion(self):
        con = False 
        while (con == False):
            lin = int(input("Por favor ingrese su linea telefonica: "))
            if 5700 < lin <= 5720: # nos aseguramos que el numero exista
                info = pd.read_excel('abonados.xlsx')
                df = pd.DataFrame(info) # leemos el excel del registro y lo agregamos a un DataFrame
                num_mio = df[df['Numero'] == lin]['#llamadas']
                timesllam = df[df['Numero'] == lin]['segundos']
                abon = df[df['Numero'] == lin]['Nombre'] # buscamos la informacion en el registro
                print(f"Bienvenido {abon.values}") 
                print(f"Su numero es {lin}") 
                print(f"Usted ha realizado {num_mio.values} llamadas")
                print(f"con un total de {timesllam.values} segundos")
                if num_mio.values >= 2:
                    df.at[lin - 5701, '#llamadas'] = 0 # reiniciamos el registro pagado
                    df.at[lin - 5701, 'segundos'] = 0
                    df.drop(['Unnamed: 0'], axis='columns', inplace=True)
                    df.to_excel('abonados.xlsx', sheet_name='Registro')
                    print(f"Por favor cancele {timesllam.values} pesos")
                    time.sleep(4)
                    print(f"Factura Pagada")
                    time.sleep(5)
                    con = True
                else:
                    print('Lo sentimos, no has realizado dos o mas llamadas, no puedes facturar')
                    time.sleep(5)
                    con = True
            else:
                print('Ingrese un numero valido')
                    