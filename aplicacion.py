# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:42:20 2022

@author: Alfredo Vilca
"""

import Gestion_Archivos

def menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Crear Archivo")
    print("2. Eliminar Archivo")
    print("3. Agregar Contenido")
    print("4. Mostrar Contenido de Archivo")
    print("5, Salir")
    
def crear():
    print("** CREAR ARCHIVO **")
    archivo = input("Crear archivo: ")
    contenido = input("Contenido del archivo: ")
    Gestion_Archivos.crear_archivo(archivo, contenido)
    
def eliminar():
    print("** ELIMINAR ARCHIVO **")
    archivo = input("Quiero eliminar el archivo:")
    Gestion_Archivos.elimiar_archivo(archivo)

def agregar():
    print("** AGREGAR CONTENIFO A UN ARCHIVO **")
    archivo = input("Quiero agregar contenido al archivo: ")
    contenido = input("El contenido adicional del archivo sera: ")
    Gestion_Archivos.agregar_contenido_archivo(archivo, contenido)
    
def listar():
    print("** MOSTRAR CONTENIDO DE UN ARCHIVO**")
    archivo = input("Quiero mostrar el contenido del archivo: ")
    print(Gestion_Archivos.leer_archivo(archivo))
    
def salir():
    print("Gracias... Vuelva pronto")
    
def error():
    print("Opcion incorrecta")
    
opcion = 1
while opcion != 5:
    menu()
    opcion = int(input("Seleccione una opcion [1-5]: "))
    if opcion == 1:
        crear()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        salir()
    else:
        error()