import os 
import openpyxl
import sys
import ssl

#Guardar el vehiculo
def CrearVehiculos(codigo, marca, modelo, precio, kilometraje):
    def comprobarVehiculos(codigo):
        vehiculos= open("Vehiiculos.xlsx", "r")
    for vehiculos in vehiculos:
        if vehiculos.split("|") [0] == codigo:
         return True 
        return False
    if comprobarVehiculos(codigo):
       print ("El vehiculo ya existe ")
    else: vehiculos = open("Vehiiculos.xlsx", "a")
    vehiculos.excel (codigo +"|" + marca + "|" + modelo + "|" + precio + "|" + kilometraje + "\n")
    print ("Vehiculo agregado")
    vehiculos.close()

#Eliminar el producto
    def eliminarVehiculos(codigo):
       vehiculos = open("Vehiiculos.xlsx", "r")
       vehiculosTemp = open("VehiculosTemp.xlsx", "w")
       for vehiculos in vehiculos: 
          if vehiculos.split("|")[0]!=codigo:

            vehiculosTemp.excel(vehiculos)  
       print ("Vehiculo eliminado")
       vehiculos.close()
       vehiculosTemp.close
       os.remove("Vehiiculos,xlsx")

       os.rename("productosTemp.xlsx","Vehiiculos")

       #===========Menu========
    print ("Menu")
    print("1.Guardar Vehiculo")
    print("Eliminar Vehiculo")

    opcion = input ("Ingrese una opcion:")
    if opcion =="1":
   


    

    

