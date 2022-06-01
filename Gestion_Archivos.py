# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:31:17 2022

@author: Alfredo Vilca
"""

import os
# Para crear archivo, recibe como parámetro el nombre del archivo
# y el contenido del archivo
def crear_archivo(nombre, contenido):
    archivo = open(nombre,"wt")
    archivo.write(contenido)
    archivo.close()
# Para eliminar recibe como parámetro el nombre del archivo a eliminar
def eliminar_archivo(nombre):
    os.remove(nombre)
# Para agregar contenido a un archivo plano, debe existir un archivo
# Se envia como parámetro el nombre y el contenido del archivo
def agregar_contenido_archivo(nombre, contenido):
    archivo = open(nombre,"at")
    archivo.write("\n" + contenido)
    archivo.close()
# Para leer un archivo, ya debe existir un archivo plano 
# Ejemplo: txt, py, java, ...
# Recibe como parámetro el nombre del archivo a leer
# y devuelve el contenido del archivo
def leer_archivo(nombre):
    archivo = open(nombre,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido