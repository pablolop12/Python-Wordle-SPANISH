# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#IMPORTAMOS OPEN, PARA TRABAJAR CON EL ARCHIVO CON LAS PALABRAS
from io import open
import random
from colorama import init, Fore
init()



#RUTA DEL ARCHIVO FUENTE DE PALABRAS - CAMBIAR SI SE DESCARGA
archivo_palabras=open("D:\Principales\Documentos\EV2 Python\palabras.txt","r")





#DECLARACIÓN DE VARIABLES
palabraAleatoria = "" #ALMACENARA LA PALABRA RANDOM SELECCIONADA
palabraUsuario = ""   #ALMACENARA LA PALABRA INTRODUCIDA POR EL USUARIO
palabraExiste = True  #BOOLEANO QUE VERIFICA SI LA PALABRA EXISTE
intentos = 6          #CONTADOR DE LOS INTENTOS QUE TENEMOS

intento1 = ""         #VARIABLES QUE ALMACENAN LAS PALABRAS PREVIAMENTE INTRODUCIDAS
intento2 = ""
intento3 = ""
intento4 = ""
intento5 = ""

#DIVIDIMOS CADA PALABRA DEL TXT CON UN SPLIT Y LO METEMOS EN UNA LISTA (lista_palabras)
lineas = [linea.split() for linea in archivo_palabras]
lista_palabras = list()
for linea in lineas: 
    lista_palabras+=linea

#FUNCION DE SELECCION RANDOM DE UNA PALABRA
def selectRandom(lista_palabras):
    return random.choice(lista_palabras)

#INTRODUCE LA PALABRA RANDOM EN UNA VARIABLE (palabraAleatoria)
palabraAleatoria = selectRandom(lista_palabras)
print (Fore.WHITE + "PALABRA A ADIVINAR:",palabraAleatoria) 

#PALABRA DEL USUARIO INTRODUCCION NADA MÁS
palabraUsuario = input(Fore.WHITE + "Predicción: ").upper()
if palabraUsuario in lista_palabras:
   palabraExiste=True
else:
    palabraExiste=False


#VALIDACION DE PALABRA
# CASO 1: LA PALABRA SE ACIERTA
if palabraUsuario == palabraAleatoria:
    print(Fore.GREEN + "HAS ACERTADO LA PALABRA", palabraAleatoria) 
else:
    
    i = 0
    while i == 0:
        
        if intentos !=1:
            
            # CASO 2: PALABRA VÁLIDA PERO NO ACERTADA - JUEGO AVANZA
            if palabraExiste == True and len(palabraUsuario)==5 and palabraUsuario != palabraAleatoria:
                intentos -=1



                #MODULO DE COLOR DE LETRAS CORRECTAS: VERDE Y AMARILLO
                #✪PRIMER INTENTO: COLOREADOR DE PALABRAS
                if intentos == 5: 
                    intento1 = palabraUsuario
                    j = 0
                    while j !=5:
                        if(palabraAleatoria[j] is intento1[j]):
                            print(Fore.GREEN + intento1[j], end="")
                        elif (palabraAleatoria[j] is not intento1[j] and intento1[j] in palabraAleatoria):
                            print (Fore.YELLOW + intento1[j], end="")
                        else:
                            print(Fore.WHITE + intento1[j], end="")     
                        j+=1
                    print(" ")
                    
                #✪SEGUNDO INTENTO: COLOREADOR DE PALABRAS
                elif intentos ==4:
                    intento2 = palabraUsuario
                    print(Fore.CYAN + intento1)
                    j = 0
                    while j !=5:
                        if(palabraAleatoria[j] is intento2[j]):
                            print(Fore.GREEN + intento2[j], end="")
                        elif (palabraAleatoria[j] is not intento2[j] and intento2[j] in palabraAleatoria):
                            print (Fore.YELLOW + intento2[j], end="")
                        else:
                            print(Fore.WHITE + intento2[j], end="")     
                        j+=1
                    print(" ")

                #✪TERCER INTENTO: COLOREADOR DE PALABRAS    
                elif intentos ==3:
                    intento3 = palabraUsuario
                    print(Fore.CYAN + intento1)
                    print(Fore.CYAN + intento2)
                    j = 0
                    while j !=5:
                        if(palabraAleatoria[j] is intento3[j]):
                            print(Fore.GREEN + intento3[j], end="")
                        elif (palabraAleatoria[j] is not intento3[j] and intento3[j] in palabraAleatoria):
                            print (Fore.YELLOW + intento3[j], end="")
                        else:
                            print(Fore.WHITE + intento3[j], end="")     
                        j+=1
                    print(" ")
                    
                #✪CUARTO INTENTO: COLOREADOR DE PALABRAS    
                elif intentos ==2:
                    intento4 = palabraUsuario
                    print(Fore.CYAN + intento1)
                    print(Fore.CYAN + intento2)
                    print(Fore.CYAN + intento3)
                    j = 0
                    while j !=5:
                        if(palabraAleatoria[j] is intento4[j]):
                            print(Fore.GREEN + intento4[j], end="")
                        elif (palabraAleatoria[j] is not intento4[j] and intento4[j] in palabraAleatoria):
                            print (Fore.YELLOW + intento4[j], end="")
                        else:
                            print(Fore.WHITE + intento4[j], end="")     
                        j+=1
                    print(" ")
                    
                #✪QUINTO INTENTO: COLOREADOR DE PALABRAS     
                elif intentos ==1:
                    intento5 = palabraUsuario
                    print(Fore.CYAN + intento1)
                    print(Fore.CYAN + intento2)
                    print(Fore.CYAN + intento3)
                    print(Fore.CYAN + intento4)
                    j = 0
                    while j !=5:
                        if(palabraAleatoria[j] is intento5[j]):
                            print(Fore.GREEN + intento5[j], end="")
                        elif (palabraAleatoria[j] is not intento1[j] and intento5[j] in palabraAleatoria):
                            print (Fore.YELLOW + intento5[j], end="")
                        else:
                            print(Fore.WHITE + intento5[j], end="")     
                        j+=1
                    print(" ")
                
                
                
                

                # SISTEMA DE PALABRAS VALIDAS
                print(Fore.MAGENTA + "Te quedan", intentos, "intentos")
                
                #MODULO DE INTRODUCCION Y VALIDACIÓN TRAS NUEVO INTENTO
                palabraUsuario = input(Fore.WHITE + "Predicción: ").upper()
                if palabraUsuario == palabraAleatoria:
                    print(Fore.GREEN + "HAS ACERTADO LA PALABRA", palabraAleatoria)
                    i+=1
                elif palabraUsuario in lista_palabras:
                   palabraExiste=True
                else:
                    palabraExiste=False
                    
               
                    

            #CASO 3: PALABRA NO VALIDA    
            elif palabraExiste == False or len(palabraUsuario)!=5:
                print(Fore.WHITE + "La palabra no está en el diccionario o no tiene 5 carácteres")
                
                #MODULO DE INTRODUCCION Y VALIDACIÓN TRAS NUEVO INTENTO
                palabraUsuario = input(Fore.WHITE + "Predicción: ").upper()
                if palabraUsuario == palabraAleatoria:
                    print(Fore.GREEN + "HAS ACERTADO LA PALABRA", palabraAleatoria)
                    i+=1
                elif palabraUsuario in lista_palabras:
                   palabraExiste=True
                else:
                    palabraExiste=False
            
            
        else:
            print(Fore.RED + "HAS PERDIDO: Se han agotado tus intentos")
            print("La palabra era:", palabraAleatoria)
            i+=1
            
    