#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 18:15:24 2019

@author: gvr
"""
import helpers
import re
import csv

""" Administrador de registros """

class Registro:

    def __init__(self, dni=None, nombre=None, apellidos=None):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {} {}'.format(self.dni,self.nombre,self.apellidos)

    def listacontenido(self):
        return [self.dni,self.nombre,self.apellidos]

    def strcontenido (self):
        return '{} {} {}'.format(self.dni,self.nombre,self.apellidos)


class Agenda:

    def __init__(self, entradas=None):
        if entradas is None:
            self.entradas = []
        else:
            self.entradas = entradas

    def listado_completo(self):
        for item in self.entradas:
            print(item) 
            
    def anade_registro(self, registro=None):        
        self.entradas.append(registro)
    
    def busca_registro_dni(self, dni=None):
        if dni is None:
            dni = input_terminal_dni()
        if dni != False:
            for item in self.entradas:
                if item.dni == dni:
                    print(item)
                    return True
            print("No se ha encontrado ningún registro con ese DNI")
        return False
    
    def devuelve_registro_dni(self, dni=None):
        if dni is None:
            dni = input_terminal_dni()
        if dni != False:
            for item in self.entradas:
                if item.dni == dni:
                    return item
        print("No se ha encontrado ningún registro con ese DNI")
        return False
         
    def entrada_registro(self, dni=None):
        if dni is None:
            dni = input_terminal_dni()
        if dni != False:
            # Comprueba que el dni no esté repetido
            if not agenda.check_dni_enuso(dni):
                nueva_entrada = Registro()
                nueva_entrada.dni = dni
                print("Introduce nombre (De 2 a 30 caracteres)")
                nueva_entrada.nombre = helpers.input_text(2, 30)
                print("Introduce apellido (De 2 a 30 caracteres)")
                nueva_entrada.apellidos = helpers.input_text(2, 30)
                self.anade_registro(nueva_entrada)
                print('Registro añadido:',nueva_entrada)            
                return True
            print("DNI en uso")
        return False
    
    def edita_registro(self):
        dni = input_terminal_dni()
        if dni != False:
            # Solicita nuevas entradas
            for item in self.entradas:
                if item.dni == dni:
                    print(f"Introduce nuevo nombre ({item.nombre})")
                    item.nombre = helpers.input_text(2, 30)
                    print(f"Introduce nuevo apellido ({item.apellidos})")
                    item.apellidos = helpers.input_text(2, 30)
                    print('Registro modificado:',item)
                    return True
            print('Registro no existe\n')
        return False

    def borra_registro(self, dni=None):
        if dni is None:
            dni = input_terminal_dni()
        if dni != False:
            # Buscar registro y lo borra si existe
            if agenda.busca_item_dni(dni) == True:
                contenido = str(agenda.contenido_item_dni(dni))
                agenda.borra_item_dni(dni)
                print('Registro borrado:',contenido,'\n')
                return True
            print('Registro no existe\n')
        return False

    def borra_item_dni(self, dni):
        if agenda.busca_item_dni(dni) != False:
            for i, entrada in enumerate(self.entradas):
                if entrada.dni == dni:
                    self.entradas.pop(i)
                    return True
        else:
            return False

    def busca_item_dni(self, dni):
        for entrada in self.entradas:
            if entrada.dni == dni:
                return True
        return False

    def contenido_item_dni(self, dni):
        for entrada in self.entradas:
            if entrada.dni == dni:
                print(entrada)
                return entrada.__str__()
        return False

    def check_dni_enuso(self, dni):
        for item in self.entradas:
            if item.dni == dni:
                return True
        return False

# Objetos soporte
agenda = Agenda()

# =============================================================================
# # Datos de prueba
# agenda.anade_registro(Registro("15J", "Marta", "Perez"))
# agenda.anade_registro(Registro("48H", "Manolo", "Lopez"))
# agenda.anade_registro(Registro("28Z", "Ana", "Garcia"))
# =============================================================================


def leefichero(fichero=None):
    try:
         handler = open(fichero,mode='r', encoding="utf8")
    except Exception as e:
         print("Ha ocurrido un error no previsto", type(e).__name__)
    with open(fichero,mode='r', encoding="utf8") as handler:
        reader = csv.reader(handler, delimiter=",", quoting=csv.QUOTE_NONE)
        for item in reader:
            agenda.anade_registro(Registro(item[0], item[1],item[2]))
        agenda.entradas.pop(0)
        handler.close()
        return True

def grabafichero(datos, fichero=None):
    handler = open(fichero,'w', encoding="utf8")
    handler.write('dni,nombre,apellidos\n')
    for entrada in datos.entradas:
        linea = str(entrada.dni) + ',' + str(entrada.nombre) + ',' + str(entrada.apellidos) +'\n' 
        handler.write(linea)
    handler.close()
    return

def input_terminal_dni():
    while True:
        print("Introduce DNI (2 números y 1 carácter en mayúscula): ")
        dni = helpers.input_text(3, 3)  
        # Comprueba que el dni cumple con un patrón
        if not re.match('[0-9]{2}[A-Z]', dni):
            print("DNI incorrecto\n")
        else:
            return dni
    return False

        
        
    

    
    

