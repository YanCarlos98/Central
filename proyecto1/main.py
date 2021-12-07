import os 
import sys 
from Central import Central

def menu(): 
    print(" ") 
    print(".:BIENVENID@ A LA CENTRAL TELEFÓNICA:.") 
    print("Seleccione la opción que desea realizar:") 
    print("1.Realizar llamada") 
    print("2.Consultar factura") 
    print("3.Pagar factura") 
    print("4.Salir") 
    print(" ")
    
central = Central() #Inicializamos la central telefonica

check = False
while True: #Aplicamos la estructura para realizar la accion correspondiente segun la entrada
    menu()
    sel = input()
    if sel == "1" : #Aqui se realiza la llamada, por ende llamamos a los abonados
        central.iniciarAbonados() #Se hace el llamado de los abonados
        central.iniciandoLlamada() #Se hace el llamado a la funcion iniciar llamada
        central.registrarLlamada() #Se hace el llamado de la funcion registrar llamada
        check = True
    elif sel == "2": 
        central.consultarFactura()
    elif sel == "3": #Aqui se realiza el pago de la factura
        central.Facturacion()
    elif sel == '4': #Salimos de la central telefonica
        sys.exit() 
    else: #Agregamos un else para el caso de que no se presione un valor asignado en el menu
        print('No presiono ninguna opcion, por favor ingrese una opcion valida')
    if check:
        os.system('cls') #Realizamos un limpiado de pantalla para ejecutar nuevamente el menu
        central=Central() #Atribuimos nuevamente a central los parametros de la clase Central para reiniciar la central
            

