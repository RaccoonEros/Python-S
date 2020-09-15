#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import sys
import os


# In[2]:


def muro_solido(murox,muroy,veces):
    """
    Esta función repite las coordenadas en x de la línea base en cada bloque-fila que forma el mapa,
    y cada repetición aumenta la coordenada y agregandola al arreglo que contiene todas las coordendas
    que conforman cada bloque-fila
    
    Las entradas son el arreglo de coordenadas x de la fila, el arreglo de coordenadas(base) 
    de la fila y las veces que se desea repetir, para rellenar el bloque.
    
    """
    
    MURO_TOTAL_x=np.array([])
    MURO_TOTAL_y=np.array([])
    for i in range(veces-1):
        add_x = np.copy(murox)
        MURO_TOTAL_x=np.append(MURO_TOTAL_x,add_x)
        add_y= muroy + np. array(list(map(lambda murox:0.25*(i+1) ,murox)))
        MURO_TOTAL_y=np.append(MURO_TOTAL_y,add_y)
        
    return(MURO_TOTAL_x,MURO_TOTAL_y)


# In[3]:


#Inicialización de los arreglos que contienen las coordenadas del mapa:
MUROX=np.array([])
MUROY=np.array([])

#El mapa se construye rellenando puntos entre un número entero hasta otro entero mayor, a pasos
#de 0.25, tanto en coordenada x, como coordenda y, dejando espacio para los caminos que tendrian
# 3 espaciós para colocar otros puntos separados de los muros una longitud igual a 0.25 o 0.5,
# de esta forma el usario debería poder moverse por los caminios usando las coorenadas (x.5,y.5)
# donde x, y son enteros, con pasos de unidad para cada coordenada.

#Aquí se construye las coordenadas base de cada bloque-fila que conforman el mapa, para luego ser
#ingresadas la función que robustece el bloque-fila, se va agregando las coordenadas de
#cada bloque-fila a los arreglos inicializados anteriormente
#Primera linea----0-1
#------------------------------------------------------------------------------
#Esta sección corresponde a la creación de las coordendas base de la fila
muro_cordenada_x=np.arange(0,1.25, 0.25)
add_muro_x=np.arange(2,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:0 ,muro_cordenada_x)))
#-------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#Aquí se agregan las coordendas base de la fila a cada arreglo que va contener todas la coordendas
#de los muros
MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)
#--------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#Pasamos las coordenadas base de la fila por la función para, robustecer el bloque-fila
# y se agregan a los arreglos que contenedrán todas la coordendas de los muros
ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,5)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)
#--------------------------------------------------------------------------------

#Segunda linea  1.25-2
muro_cordenada_x=np.arange(0,1.25, 0.25)
add_muro_x=np.arange(2,10.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(12,17.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(19,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:1.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)


#Tercera linea  2.25-3
muro_cordenada_x=np.arange(0,1.25, 0.25)
add_muro_x=np.arange(23,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:2.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)


#Cuarta linea  3.25-4

muro_cordenada_x=np.arange(0,3.25, 0.25)
add_muro_x=np.arange(4,6.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(7,10.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(12,17.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(19,22.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(23,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:3.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)


#Quinta linea  4.25-5

muro_cordenada_x=np.arange(0,3.25, 0.25)
add_muro_x=np.arange(4,6.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(7,22.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(23,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:4.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

#Sexta linea  5.25-6

muro_cordenada_x=np.arange(0,1.25, 0.25)
add_muro_x=np.arange(4,6.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(7,22.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(23,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:5.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

#Séptima lina 6.25-7

muro_cordenada_x=np.arange(0,1.25, 0.25)
add_muro_x=np.arange(2,6.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(7,14.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(17,18.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(20,22.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(23,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:6.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

#Octava linea 7.25-8

muro_cordenada_x=np.arange(0,1.25, 0.25)
add_muro_x=np.arange(2,5.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(8,14.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(17,18.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(20,21.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(24,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:7.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)


#Novena linea 8.25-9

muro_cordenada_x=np.arange(0,1.25, 0.25)
add_muro_x=np.arange(2,5.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(8,15.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(16,19.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(20,21.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(24,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:8.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

#Décima linea 9.25-10

muro_cordenada_x=np.arange(0,1.25, 0.25)
add_muro_x=np.arange(2,14.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(17,19.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(20,21.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(24,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:9.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

#Onceava linea 10.25-11

muro_cordenada_x=np.arange(0,1.25, 0.25)
add_muro_x=np.arange(4,14.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(15,16.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(17,19.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(20,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:10.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

#Doceava linea 11.25-12

muro_cordenada_x=np.arange(0,3.25, 0.25)
add_muro_x=np.arange(4,14.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(15,16.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(17,19.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(20,22.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(24,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:11.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

#Treceava linea 12.25-13

muro_cordenada_x=np.arange(0,3.25, 0.25)
add_muro_x=np.arange(9,11.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(15,16.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(24,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:12.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

#Catorceava linea 13.25-14

muro_cordenada_x=np.arange(0,3.25, 0.25)
add_muro_x=np.arange(9,11.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(12,20.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(21,22.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(24,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:13.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

#Quinceava linea 14.25-15

muro_cordenada_x=np.arange(0,3.25, 0.25)
add_muro_x=np.arange(9,11.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(12,15.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(18,20.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(21,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:14.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

# Décima sexta linea 15.25-16

muro_cordenada_x=np.arange(0,8.25, 0.25)
add_muro_x=np.arange(9,11.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(12,15.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(18,19.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(24,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:15.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

# Décima séptima linea 16.25-17

muro_cordenada_x=np.arange(0,4.25, 0.25)
add_muro_x=np.arange(7,8.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(9,11.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(14,15.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(18,19.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(20,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:16.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

# Décima octava linea 17.25-18

muro_cordenada_x=np.arange(0,4.25, 0.25)
add_muro_x=np.arange(5,6.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(7,8.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(9,13.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(14,16.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(17,19.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(20,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:17.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

# Décima novena linea 18.25-19

muro_cordenada_x=np.arange(0,4.25, 0.25)
add_muro_x=np.arange(5,6.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(12,13.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(17,18.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(20,21.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(24,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:18.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

# Vigésima linea 19.25-20

muro_cordenada_x=np.arange(0,4.25, 0.25)
add_muro_x=np.arange(5,8.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(9,11.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(12,15.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(16,18.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(19,21.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(24,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:19.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

# Vigésima primera linea 20.25-21

muro_cordenada_x=np.arange(0,4.25, 0.25)
add_muro_x=np.arange(5,8.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(9,11.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(12,14.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(17,18.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(19,22.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(23,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:20.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

# Vigésima segunda linea 21.25-22

muro_cordenada_x=np.arange(0,4.25, 0.25)
add_muro_x=np.arange(9,11.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(12,14.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(17,18.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(23,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:21.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

# Vigésima tercera linea 22.25-23

muro_cordenada_x=np.arange(0,4.25, 0.25)
add_muro_x=np.arange(5,8.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(9,11.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(12,15.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(16,18.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(19,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:22.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

# Vigésima cuarta linea 23.25-24

muro_cordenada_x=np.arange(0,2.25, 0.25)
add_muro_x=np.arange(6,8.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(9,11.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(19,20.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(23,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:23.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

# Vigésima quinta linea 24.25-25

muro_cordenada_x=np.arange(0,2.25, 0.25)
add_muro_x=np.arange(6,8.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(9,20.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(23,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:24.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

# Vigésima sexta linea 25.25-26

muro_cordenada_x=np.arange(0,2.25, 0.25)
add_muro_x=np.arange(6,8.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
add_muro_x=np.arange(23,25.25,0.25)
muro_cordenada_x=np.append(muro_cordenada_x,add_muro_x)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:25.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)

# Vigésima séptima linea 26.25-27
muro_cordenada_x=np.arange(0,25.25, 0.25)
muro_coordenada_y=np. array(list(map(lambda muro_cordenada_x:26.25 ,muro_cordenada_x)))

MUROX=np.append(MUROX,muro_cordenada_x)
MUROY=np.append(MUROY,muro_coordenada_y)

ADDX, ADDY = muro_solido(muro_cordenada_x,muro_coordenada_y,4)
MUROX=np.append(MUROX,ADDX)
MUROY=np.append(MUROY,ADDY)


# In[4]:


# Inialiación de ubicación del personaje/Coordenadas de inicio del juego
ubicacion_personaje_x=1.5
ubicacion_personaje_y=0.5  


# In[5]:


def permitir_avanzar(MURO_CORD_X,MURO_CORD_y, PUPX,PUPY):
    """
    Esta función evalua si en la direccion en la que se ha elegido moverse es permitido.
    Las entradas:
    -Las coordenadas x del muro
    -Las coordenadas y del muro
    -Las coordenadas x,y del usuario
    
    Retorna
    -True si (x,y) no se encuentra en un par de coordenada del muro
    -False si (x,y) se encuentra en un par de coordenada del muro
    """
    for i, j in zip(MURO_CORD_X,MURO_CORD_y) :
        if (i==PUPX and j==PUPY):
            return(False)
    return(True)


# In[6]:


def mapa(x,y,murox,muroy):
    """
    Esta función se encarga de mostrar el mapa en un plot
    Entradas
    -Las coordenadas x del muro
    -Las coordenadas y del muro
    -Las coordenadas x,y del usuario
    
    Retorna
    -Nada
    """
    puertas_coordx=[12,12,12,17,17,17,22.25,22.5,22.75,15.25,15.5,15.75,20,20,20,16.25,16.5,16.75]
    puertas_coordy=[2.25,2.5,2.75,2.25,2.5,2.75,7,7,7,22,22,22,25.25,25.5,25.75,17,17,17]
    cofres_coorde_x=[6.5,15.5,18.5,23.5,22.5]
    cofres_coorde_y=[8.5,6.5,6.5,12.5,18.5]
    plt.plot(murox, muroy, '+',label="Muro del Mapa")
    plt.plot(puertas_coordx,puertas_coordy,'.',label="Puertas")
    plt.plot(cofres_coorde_x,cofres_coorde_y,"x",label="Cofres")
    plt.plot(x, y, 'o', color='r',label="Tu ubicacion" )
    plt.legend(loc='lower right', bbox_to_anchor=(1.1, 0.9))
    plt.title("Mapa del Calabozo")
    plt.tick_params(
        axis='x',         
        which='both',      
        bottom=False,      
        top=False,         
        labelbottom=False)
    plt.tick_params(
        axis='y',         
        which='both',      
        bottom=False,      
        top=False,         
        labelbottom=False)


# In[7]:


def caminar(UPX, UPY,lista_eventos_pendientes):
    """
    Esta funcion hace de swich para tomar las entradas de las direcciones que ingresa el usuario
    
    Entradas
    -Las coordenadas x,y de ubicacion del usuario
    
    Retorna
    -Tuplas como (0,1)->Ir hacia arriba/(1,0)->Ir hacia derecha... si la nueva posible ubicacion del usario es permitida
    -None si no es permitido ir tal dirección
    -Tupla (0,0) para cuando se decir pausar/por ahortia corta el flujo de ejecucion
    """
    direccion=input()
    
    if direccion=='w':
        if permitir_avanzar(MUROX,MUROY,UPX, UPY+1):
            return(0,1)
    
        else:
            print("Muro en esa dirección, intente ir en otro sentido")
            return(None)
    
    elif direccion=='d':
        if (permitir_avanzar(MUROX,MUROY,UPX+1, UPY)):
            return(1,0)
    
        else:
            print("Muro en esa dirección, intente ir en otro sentido")
            return(None)
        
    elif direccion=='a':
        if (permitir_avanzar(MUROX,MUROY,UPX-1, UPY)):
            return(-1,0)
    
        else:
            print("Muro en esa dirección, intente ir en otro sentido")
            return(None)
    
    elif direccion=='s':
        if (permitir_avanzar(MUROX,MUROY,UPX, UPY-1)):
            if(UPX==1.5 and UPY==0.5):
                print("No puedes huir del calabozo, una pared transparente no te permite salir")
                return(None)
            
            elif (UPX==16.5 and UPY==17.5):
                # Condicionante para no pasar a la sala del jefe sin haber conseguido la llave en en evento 2 (primer subjefe)     
                if (2 in lista_eventos_pendientes): 
                    print("No puedes pasar, necesitas la llave que custodia el Subjefe A")
                    return(None)
                else:
                    return(0,-1)
                
            elif (UPX==15.5 and UPY==22.5):
                # Condicionante para no pasar a la tercera habitacion trampa, sin abrir puerta del otro lado   
                if (6 in lista_eventos_pendientes): 
                    print("Puerta bloqueada, no puedes pasar")
                    return(None)
                else:
                    return(0,-1)
            else:
                return(0,-1)
    
        else:
            print("Muro en esa dirección, intente ir en otro sentido")
            return(None)

    elif direccion=='p':
        print("Descansando....zzZZZ")
        return(0,0)
    
    else:
        print("Ha ingresado caracter incorrecto, intente de nuevo= ")
        return(None)


# In[8]:


#Creación del mapa de caracteres
mapa_ch='#########################'+'\n'
agg_muro='##    ##               ##'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='##    ## ###########   ##'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='##    ## ##        #   ##'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='#### ### ## ### ## ######'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='####     ## ##   #     ##'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='#### ### ## ##   # ### ##'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='#### ### ## ### ## ##   #'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='#### #      #    #  # D #'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='#### # # #### ## ## #####'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='####   # ##   #   # #####'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='######## ## ###   #     #'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='###      ## ###   ## ####'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='###      ## ######## #  #'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='###      ##    #       D#'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='### ########## # ## ##  #'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='#   ########## # ## #####'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='# ############   ## #   #'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='# ### D ####### ### #   #'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='# ###   ######   #  #   #'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='# #### ####### D #D ## ##'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='#   ## ############### ##'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='### ## ############### ##'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='### ## ###  #####  ### ##'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='#                      ##'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='# ########  #####  ######'+'\n'
mapa_ch=mapa_ch+agg_muro
agg_muro='#o#######################'+'\n'
mapa_ch=mapa_ch+agg_muro
mapa_ch=(mapa_ch,None)


# In[9]:


def actualizar_mapa(mapy,paso_x,paso_y):
    """
    Esta funcion actualziza el mapa de caracteres que se va imprimir en ejecucion
    
    Entradas
    -La cadena de caracteres del mapa
    -El paso en x y en y que se permite al usuario según, ingrese una dirección, estas entradas son tomadas del retorno de
     las tuplas de la funcion caminar()
    
    Retorna
    -Cadena de caracteres para el nuevo mapa
    -None si ha ingresado un caracter no adecuado
    """
     
    i=mapy.index("o")
    if(paso_x==0 and paso_y==1):
        mi=-26
    elif (paso_x==1 and paso_y==0):
        mi=1
    elif (paso_x==-1 and paso_y==0):
        mi=-1
    elif (paso_x==0 and paso_y==-1):
        mi=26
    elif (paso_x==0 and paso_y==0):
        mi=0
    else:
        print("Ha ingresado un comando inválido, intente de nuevo")
        actualizar_mapa(mapy)
        return(None)
    
    lista_mapa=[]
    for caracter in mapy:
        lista_mapa.append(caracter)
        
    lista_mapa[i]=" "
    lista_mapa[i+mi]="o"
    nuevo_mapa="".join(lista_mapa)
    return(nuevo_mapa,i)


# In[10]:


# Definicion de clase para las diferentes zonas de enemigos/moustros en el mapa
class Zona_caliente:
    def __init__(self, nombre, coord_x, coord_y, num_enemigos, tipos, porcentaje_aparicion):
        self.nombre=nombre
        self.coord_x=coord_x
        self.coord_y=coord_y
        self.num_enemigos=num_enemigos
        self.tipos=tipos
        self.porcentaje_aparicion=porcentaje_aparicion
    
    def __str__(self):
        return(f"{self.nombre}, con {self.num_enemigos} enemigos vivos, posibilidades:{self.tipos}")
    
    def __repr__(self):
        return(f"{self.nombre}, con {self.num_enemigos} enemigos vivos, posibilidades:{self.tipos}")
        


# In[11]:


# Dfinicion de cada zona utilizando la clase
########################################################################################
#   Eros aquí te queda a liberta la eleccion de que zona poner cada enemigo, mi idea es que cada vez aumenta el número de
#   la zona, los enemigos deben ser mas fuertes. Entonces ahí en los corchetes donde dice "enemigo1","enemigo2"
#   ahi pones el nombre del moustro que penses para ese lugar, y la par el porcentaje que queres con que aparesca, de 
#   forma correspondiente
########################################################################################
#Definiendo zona enemiga 1
coordx_zona1=[1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,3.5,3.5,3.5,2.5,1.5]
coordy_zona1=[2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,3.5,4.5,5.5,5.5,5.5]

zona1=Zona_caliente("Primer corredor",coordx_zona1,coordy_zona1,3,["enemigo1","enemigos2"],[20,15])

#Definiendo zona enemiga 2
coordx_zona2=[6.5,6.5,6.5,6.5,1.5,1.5,1.5,1.5,1.5,2.5,3.5,3.5]
coordy_zona2=[3.5,4.5,5.5,6.5,6.5,7.5,8.5,9.5,10.5,10.5,10.5,11.5]

zona2=Zona_caliente("Territorio 13",coordx_zona2,coordy_zona2,3,["enemigo1","enemigos2"],[20,15])

#Definiendo zona enemiga 3
coordx_zona3=[3.5,4.5,5.5,6.5,7.5,8.5,3.5,4.5,5.5,6.5,7.5,8.5,3.5,4.5,5.5,6.5,7.5,8.5]
coordy_zona3=[12.5,12.5,12.5,12.5,12.5,12.5,13.5,13.5,13.5,13.5,13.5,13.5,14.5,14.5,14.5,14.5,14.5,14.5]

zona3=Zona_caliente("Territorio 18",coordx_zona3,coordy_zona3,5,["enemigo1","enemigos2","enemigos3"],[20,15,15])

#Definiendo zona enemiga 4
coordx_zona4=[8.5,8.5,8.5,6.5,7.5,8.5,9.5,10.5,11.5,6.5,6.5,5.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5]
coordy_zona4=[15.5,16.5,17.5,18.5,18.5,18.5,18.5,18.5,18.5,17.5,16.5,16.5,16.5,17.5,18.5,19.5,20.5,21.5,22.5]

zona4=Zona_caliente("Corredor d",coordx_zona4,coordy_zona4,5,["enemigo1","enemigos2","enemigos3"],[20,15,15])

#Definiendo zona enemiga 5
coordx_zona5=[8.5,8.5,8.5,8.5,8.5,8.5,8.5,5.5,6.5,7.5,11.5,11.5,11.5,11.5]
coordy_zona5=[19.5,20.5,21.5,22.5,23.5,24.5,25.5,21.5,21.5,21.5,19.5,20.5,21.5,22.5]

zona5=Zona_caliente("Corredor d",coordx_zona5,coordy_zona5,5,["enemigo1","enemigos2"],[20,15])

#Definiendo zona enemiga 6
coordx_zona6=[9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5]
coordy_zona6=[25.5,25.5,25.5,25.5,25.5,25.5,25.5,25.5,25.5]

zona6=Zona_caliente("Corredor d",coordx_zona6,coordy_zona6,4,["enemigo1","enemigos2"],[20,15])

#Definiendo zona enemiga 7
coordx_zona7=[11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5,15.5,18.5,18.5,18.5,18.5,18.5,19.5,20.5,21.5,22.5,22.5]
coordy_zona7=[23.5,23.5,23.5,23.5,23.5,23.5,23.5,23.5,22.5,22.5,21.5,20.5,19.5,18.5,21.5,21.5,21.5,21.5,20.5]

zona7=Zona_caliente("Corredor d",coordx_zona7,coordy_zona7,4,["enemigo1","enemigos2","enemigos3"],[20,15,15])

#Definiendo zona enemiga 8
coordx_zona8=[12.5,13.5,14.5,15.5,16.5]
coordy_zona8=[2.5,2.5,2.5,2.5,2.5]

zona8=Zona_caliente("Corredor d",coordx_zona8,coordy_zona8,4,["enemigo1","enemigos2"],[20,15])

#Definiendo zona enemiga 9
coordx_zona9=[19.5,20.5,21.5,22.5,22.5,22.5]
coordy_zona9=[2.5,2.5,2.5,2.5,3.5,4.5]

zona9=Zona_caliente("Corredor d",coordx_zona9,coordy_zona9,4,["enemigo1","enemigos2"],[20,15])

#Definiendo zona enemiga 10
coordx_zona10=[19.5,19.5,19.5,19.5,20.5,21.5,22.5,23.5,20.5,20.5,16.5,17.5,18.5,19.5,20.5,21.5,19.5,19.5,19.5,19.5,16.5,16.5,16.5,15.5,15.5]
coordy_zona10=[18.5,17.5,16.5,15.5,15.5,15.5,15.5,15.5,14.5,13.5,12.5,12.5,12.5,12.5,12.5,12.5,11.5,10.5,9.5,8.5,11.5,10.5,9.5,9.5,8.5]

zona10=Zona_caliente("Corredor d",coordx_zona10,coordy_zona10,8,["enemigo1","enemigos2","enemigos3"],[20,15,15])

#Definiendo zona enemiga 11
coordx_zona11=[14.5,14.5,14.5,14.5,13.5,12.5,11.5,11.5,11.5,11.5,11.5,12.5,13.5,13.5,13.5,14.5]
coordy_zona11=[9.5,10.5,11.5,12.5,12.5,12.5,12.5,13.5,14.5,15.5,16.5,16.5,16.5,17.5,18.5,18.5]

zona11=Zona_caliente("Corredor al Jefe",coordx_zona11,coordy_zona11,7,["enemigo1","enemigos2", "enemigos3","enemigos4"],[20,15,15,15])


# In[12]:


# Creacion de diccionario para luego llamar de forma general las coordenadas de las zonas enemigas
zonas_enemigas={"1": [zona1.coord_x,zona1.coord_y],"2":[zona2.coord_x,zona2.coord_y], "3":[zona3.coord_x,zona3.coord_y], "4":[zona4.coord_x,zona4.coord_y], "5":[zona5.coord_x,zona5.coord_y], "6":[zona6.coord_x,zona6.coord_y], "7":[zona7.coord_x,zona7.coord_y], "8":[zona8.coord_x,zona8.coord_y], "9":[zona9.coord_x,zona9.coord_y], "10":[zona10.coord_x,zona10.coord_y], "11":[zona11.coord_x,zona11.coord_y]}


# In[13]:


# Creacion de diccionario para luego llamar de forma general los tipos de enemigos y su porcentaje de aparicion en cada zona
aparicion_enemigos={"1":zona1.tipos,"2":zona2.tipos, "3":zona3.tipos,"4":zona4.tipos,"5":zona5.tipos,"6":zona6.tipos,"7":zona7.tipos, "8":zona8.tipos, "9":zona9.tipos, "10":zona10.tipos,"11":zona11.tipos}
porcentajes={"1":zona1.porcentaje_aparicion,"2":zona2.porcentaje_aparicion, "3":zona3.porcentaje_aparicion,"4":zona4.porcentaje_aparicion,"5":zona5.porcentaje_aparicion,"6":zona6.porcentaje_aparicion,"7":zona7.porcentaje_aparicion,"8":zona8.porcentaje_aparicion, "9":zona9.porcentaje_aparicion,"10":zona10.porcentaje_aparicion,"11":zona11.porcentaje_aparicion}


# In[14]:


def comprobacion_zona(x,y,zonas_enemigas):
    """
    Esta función coprueba si el usuario se encuentra en una zona enemiga
    
    Entradas
    -Elemento del diccionario zonas_enemigas que contiene las coordenadas de las mismas
    -Coordenadas (x,y) de ubicación del usuario
    
    Retorna
    -True si detecta que el usuario está en zona enemiga
    """
    
    x_prueba,y_prueba=zonas_enemigas
    for i,j in zip(x_prueba,y_prueba):
        if(x==i and y==j):
            return(True)
            break


# In[15]:


def aparicion(n,ratio):
    """
    Esta funcion controla la eleccion aleatoria sobre que tipo de enemigo va salir en la zona enemiga número n
    Tine tres opciones que dependen de la cantidad de enemigos que pueden aparecer en la zona, definidos anteriormente,
    con el uso de clase
    
    Entradas
    -ratio es un número que debe elegirse aleatoriamente entre 1 a 100
    -n es el número de la zona en la que se encuentra el usuario, 
    
    Retorna
    ****************************************
    -Por ahora solo imprime que enemigo aparece,aun hay que implementar las funciones de batallas
    ****************************************
    """
    
    if (len(aparicion_enemigos[str(n)])==2):
        enemigo1,enemigo2=aparicion_enemigos[str(n)]
        porcent1,porcent2=porcentajes[str(n)]
        
        if(ratio<=porcent1):
            print(f"Aparece {enemigo1}")
            #Llamar funcion para batalla
        elif(ratio<=porcent1+porcent2):
            print(f"Aparece {enemigo2}")
            #Llamar funcion para batalla
    
    elif(len(aparicion_enemigos[str(n)])==3):
        enemigo1,enemigo2, enemigo3=aparicion_enemigos[str(n)]
        porcent1,porcent2,porcent3=porcentajes[str(n)]
        
        if(ratio<=porcent1):
            print(f"Aparece {enemigo1}")
            #Llamar funcion para batalla
        elif(ratio<=porcent1+porcent2):
            print(f"Aparece {enemigo2}")
            #Llamar funcion para batalla
        elif(ratio<=porcent1+porcent2+porcent3):
            print(f"Aparece {enemigo3}")
            #Llamar funcion para batalla
        
    
    else:
        enemigo1,enemigo2, enemigo3,enemigo4=aparicion_enemigos[str(n)]
        porcent1,porcent2,porcent3,porcent4=porcentajes[str(n)]
        
        if(ratio<=porcent1):
            print(f"Aparece {enemigo1}")
            #Llamar funcion para batalla
        elif(ratio<=porcent1+porcent2):
            print(f"Aparece {enemigo2}")
            #Llamar funcion para batalla
        elif(ratio<=porcent1+porcent2+porcent3):
            print(f"Aparece {enemigo3}")
            #Llamar funcion para batalla
        elif(ratio<=porcent1+porcent2+porcent3+porcent4):
            print(f"Aparece {enemigo4}")
            #Llamar funcion para batalla


# In[16]:


def posibilidad_enemigo(x,y):
    """
    Esta funcion termina implementa las dos anteriores, para ser llamadas en la ejecucion
    
    Entradas
    -Ubicacion del usuario en coordenadas (x,y)
    
    Retorna
    -No retorna nada
    """
    for k in range(len(zonas_enemigas)):
        if(comprobacion_zona(x,y,zonas_enemigas[str(k+1)])==True):
            posibilidad=np.random.choice(range(1,100))
            aparicion(k+1,posibilidad)
    


# In[17]:


def instrucciones():
    """
    Esta funcion imprime las intrucciones en pantalla
    """
    os.system("cls")
    print("                  -INSTRUCCIONES-                  ")
    print("\n")
    print("---------------------------------------------------")
    print("#################    MOVILIDAD     ################")
    print("---------------------------------------------------")
    print("   -Para moverser hacia delante presionar -w-")
    print("   -Para moverser hacia atrás presionar -s-")
    print("   -Para moverser hacia la derecha presionar -d-")
    print("   -Para moverser hacia la izquierda presionar -a-")
    print("\n")
    print("---------------------------------------------------")
    print("#################     Pausa       ################")
    print("---------------------------------------------------")
    print("   -Para pausar presione -p-")
    print("\n")
    print("\n")
    print("   [q]-Salir de instrucciones)")
    opcion_i=input("> ")
    while opcion_i !="q":
        print("Porfavor ingresar un comando válido(q:Salir de instrucciones)")
        opcion_i=input("> ")
    pantalla_titulo()
    return(None)
    


# In[18]:


def seleccion_menu_titulo():
    """
    Esta funcion controla el menú principal del juego, es decir la elección de si el usuario quiere empejar el juego, ver 
    instrucciones, salir y posiblemente implementado después: jugar partida guardada
    """
    opcion=input("> ")
    if opcion =="p":
        return(True)
    elif opcion=="i":
        instrucciones()
        return(None)
    elif opcion=="q":
        sys.exit()
    while opcion not in ["p","i","q"]:
        print("Porfavor ingresar un comando válido(p:comenzar partida,i:instrucciónes,q:salir)")
        opcion=input("> ")
        if opcion =="p":
            return(True)
        elif opcion=="i":
            instrucciones()
            return(None)
        elif opcion=="q":
            sys.exit()


# In[19]:


#Iniciando el juego:
def pantalla_titulo():
    """
    Esta funcion imprime el titulo del juego y el menú principal en pantalla
    """
    
    os.system("cls")
    print("###################################################")
    print("|                  Expirience RPG                 |")
    print("###################################################")
    print("\n")
    print("    [p]-Comenzar Partida")
    print("    [i]-Instrucciones")
    print("    [q]-Salir")
    confirmacion=seleccion_menu_titulo()
    print(confirmacion)
    if(confirmacion==True):
        return(True)
    elif(confirmacion==None):
        return(True)


# In[20]:


# Definicion de la clase a usar para las zonas que contienen eventos
class Zona_evento():
    def __init__(self, nombre,descripcion,coord_x, coord_y):
        self.nombre=nombre
        self.descripcion=descripcion
        self.coord_x=coord_x
        self.coord_y=coord_y
    
    #def __conseguido__(self):
     #   return(True)
    
    def __str__(self):
        return(f"{self.nombre}.{self.descripcion}")
    
    def __repr__(self):
        return(f"{self.nombre}.{self.descripcion}")


# In[21]:


#Creación de las zonas de evento con la clase:
#Evento 1
evento1_coordx=[3.5,4.5,5.5,6.5,7.5,8.5,3.5,4.5,5.5,6.5,7.5,8.5,3.5,4.5,5.5,6.5,7.5,8.5]
evento1_coordy=[12.5,12.5,12.5,12.5,12.5,12.5,13.5,13.5,13.5,13.5,13.5,13.5,14.5,14.5,14.5,14.5,14.5,14.5]
descrip1="Este es un campo minado por los mounstros de la zona, un paso al lugar equivocado puede causarte daño"

zn_evento1=Zona_evento("Territorio de minas",descrip1, evento1_coordx,evento1_coordy)
#Evento 2
evento2_coordx=[20.5,21.5,22.5,20.5,21.5,22.5,20.5,21.5,22.5]
evento2_coordy=[23.5,23.5,23.5,24.5,24.5,24.5,25.5,25.5,25.5]
descrip2="Se encuentra Subjefe A custiodiando la llave que habre la puerta al Jefe"

zn_evento2=Zona_evento("Sub boss A",descrip2, evento2_coordx,evento2_coordy)

#Evento 3
evento3_coordx=[10.5,11.5,10.5,11.5,10.5,11.5]
evento3_coordy=[1.5,1.5,2.5,2.5,3.5,3.5]
descrip3="Hay un enemigo custodiando el paso"

zn_evento3=Zona_evento("Primera habitación trampa",descrip3, evento3_coordx,evento3_coordy)

#Evento 4
evento4_coordx=[17.5,18.5,17.5,18.5,17.5,18.5]
evento4_coordy=[1.5,1.5,2.5,2.5,3.5,3.5]
descrip4="Hay un enemigo custodiando el paso"

zn_evento4=Zona_evento("Segunda habitación trampa",descrip4, evento4_coordx,evento4_coordy)

#Evento 5
evento5_coordx=[21.5,22.5,23.5,21.5,22.5,23.5,21.5,22.5,23.5]
evento5_coordy=[7.5,7.5,7.5,8.5,8.5,8.5,9.5,9.5,9.5]
descrip5="Se encuentra el Subjefe B custodiando un objeto especial"

zn_evento5=Zona_evento("Subjefe B",descrip5, evento5_coordx,evento5_coordy)

#Evento 6
evento6_coordx=[14.5,15.5,16.5,14.5,15.5,16.5]
evento6_coordy=[20.5,20.5,20.5,21.5,21.5,21.5]
descrip6="Hay un enemigo custodiando el paso"

zn_evento6=Zona_evento("Tercera habitación trampa",descrip6, evento6_coordx,evento6_coordy)

#Evento 7
evento7_coordx=[15.5,16.5,17.5,15.5,16.5,17.5,15.5,16.5,17.5]
evento7_coordy=[14.5,14.5,14.5,15.5,15.5,15.5,16.5,16.5,16.5]
descrip7="Se encuentra reposando el Jefe del calabozo, es necesario una llave para ingresar"

zn_evento7=Zona_evento("Jefe del Calabozo",descrip7, evento7_coordx,evento7_coordy)


# In[22]:


#plt.ion()
#plt.plot(MUROX, MUROY, '+')
#plt.plot(ubicacion_personaje_x,ubicacion_personaje_y, 'o', color='r' )
#plt.plot(zn_evento7.coord_x,zn_evento7.coord_y,'v',color='g')


# In[23]:


# Creación de diccionarios que contienen informacion de la zonas de eventos, para llamarlas de forma generalizada
eventos_nombres={"1":zn_evento1.nombre,"2":zn_evento2.nombre,"3":zn_evento3.nombre,"4":zn_evento4.nombre,
              "5":zn_evento5.nombre,"6":zn_evento6.nombre,"7":zn_evento7.nombre}

eventos_coord={"1":[zn_evento1.coord_x,zn_evento1.coord_y],"2":[zn_evento2.coord_x,zn_evento2.coord_y],
              "3":[zn_evento3.coord_x,zn_evento3.coord_y],"4":[zn_evento4.coord_x,zn_evento4.coord_y],
              "5":[zn_evento5.coord_x,zn_evento5.coord_y],"6":[zn_evento6.coord_x,zn_evento6.coord_y],
              "7":[zn_evento7.coord_x,zn_evento7.coord_y]}
eventos_completados={"1":False,"2":False, "3":False, "4":False,"5":False,"6":False,"7":False}


# In[24]:


def posible_evento(x,y,coordendas_zona,eventos_pendientes):
    """
    Esta funcion verifica si el usuario se encuentra en una zona de evento, aun no cumplido
    
    Entradas:
    -Coordenadas (x,y) de ubicación del usuario
    -Diccionario que contiene lista de coordenadas (x,y) de las zonas de evento
    -Lista de eventos pendientes(numérica)
    
    Retorna:
    -El número de evento en que se encuentra el usuarios
    """
    for i in eventos_pendientes:
        x_prueba,y_prueba=coordendas_zona[str(i)]
        for j,k in zip(x_prueba,y_prueba):
            if(x==j and y==k):
                return(i)


# In[25]:


#funcion_evento={"1":funcion_ev1()}
#,"2":funcion_ev2(),"3":funcion_ev3(),"4":funcion_ev4(),
 #               "5":funcion_ev5(),"6":funcion_ev6(),"7":funcion_ev7()}


# In[26]:


#Todas las funciones deben retornar un True en su primera componente de la tupla
#a retornar, y la segunda puede ser las características del jugador
#a modificar una vez complete el evento/ejemplo-->return(True,[HP,MP,OBJETO_ADQUIRIDO...])
#que se pueda almecenar en una variable que el evento ya fue completado 
# y así no volver a buscar en posibilidades
def funcion_ev1():
    """
    Esta zona hay que crear alguna funcion que le diga al usuario con cierta probabilidad que ha pisado una mina y le
    ha causado daño
    """
    posibilidad=np.random.choice(range(1,100))
    if(posibilidad<=40):
        texto_alerta='Boooooooom!!!'+'\n'+'Ha explotado, una mina donde has pisado'
        hp=-15
        agg=f'Te ha causado{hp}pts de daño'
        texto_alerta=texto_alerta+'\n'+agg+'\n'+'Te encuentras en un territorio minado es posible, que otra mina explote al dar un paso y te cause daño'
    else:
        texto_alerta=""
        hp=0
    
    return(None,hp,texto_alerta)

#def funcion_ev2():   
#     """
 #   esta funcion debe tratar sobre la temática al entrar a la sala del subjefe y luego desenvolver la batalla
  #  """

#def funcion_ev3():
   # """
    #esta funcion debe tratar sobre la temática en una habitacion trampa y batalla con enemigo o cualquier pluzzle
   # """
    

#def funcion_ev4():
    #"""
    #esta funcion debe tratar sobre la temática en una habitacion trampa y batalla con enemigo o cualquier pluzzle
    #"""

#def funcion_ev5():
    #"""
    #esta funcion debe tratar sobre la temática al entrar a la sala del otro subjefe y luego desenvolver la batalla
    #"""

#def funcion_ev6():
    #"""
    #esta funcion debe tratar sobre la temática en una habitacion trampa y batalla con enemigo o cualquier pluzzle
    #"""

#def funcion_ev7():
    #"""
    #esta funcion debe tratar sobre la temática al entrar a la sala del jefe y luego desenvolver la batalla
    #"""


# In[28]:


class Cofres():
    def __init__(self,nombre_objeto,coordenada,estrampa):
        self.nombre_objeto=nombre_objeto
        self.coordenada=coordenada
        self.estrampa=estrampa
        
    def __str__(self):
        return(f"Cofre con objeto: {self.nombre_objeto}")
    
    def __repr__(self):
        return(f"Cofre con objeto: {self.nombre_objeto}")
        


# In[29]:


# Definiendo los cofres con la clase anterior
cofre1=Cofres("Objetoespecial1",[6.5,8.5],False)
cofre5=Cofres("Objetoespecial3",[15.5,6.5],False)
cofre4=Cofres("Ninguno",[18.5,6.5],True)
cofre3=Cofres("Objetoespecial2",[23.5,12.5],False)
cofre2=Cofres("Ninguno",[22.5,18.5],True)


# In[30]:


#Diccionario de cofres para llamar generalizadamente
objetos_cofres={"1":cofre1.nombre_objeto,"2":cofre2.nombre_objeto,"3":cofre3.nombre_objeto,"4":cofre4.nombre_objeto,
               "5":cofre5.nombre_objeto}
coordenadas_cofres={"1":cofre1.coordenada,"2":cofre2.coordenada,"3":cofre3.coordenada,
                   "4":cofre4.coordenada,"5":cofre5.coordenada}
cofres_trampa={"1":cofre1.estrampa,"2":cofre2.estrampa,"3":cofre3.estrampa,"4":cofre4.estrampa,"5":cofre5.estrampa}
cofres_abiertos={"1":False,"2":False,"3":False,"4":False,"5":False}
    


# In[31]:


def cofre_encontrado(x,y,coordenadas_cofres,lista_cofres):
    for i in lista_cofres:
        j,k=coordenadas_cofres[str(i)]
        if(j==x and k==y):
            return(i)


# In[32]:


def pausa():
    os.system("cls")
    print("#######################################")
    print("               -PAUSA-                 ")
    print("---------------------------------------")
    print("   -[i] Inventario")
    print("   -[r] Reanudar juego")
    print("   -[s] Salvar partida")
    print("   -[q] Salir del juego")
    
    comando=input("> ")
    if comando=="i":
        print("inventario")
        #Llamar funcion que muestre y controle el inventario
    elif comando=="r":
        pass
    elif comando=="s":
        #LLamar funcion para guardara partida
        print("Partida guardada")
    elif comando=="q":
        print("#############################################################################")
        print("Si no ha salvado su partida, se le recomienda salvar antes de salir del juego")
        print("#############################################################################")
        print("                    ¿Desea abandonar el juego?")
        print("                    -[y] Si")
        print("                    -[n] No")
        respuesta=input("> ")
        if respuesta=="y":
            sys.exit()  
        elif respuesta=="n":
            pass
        while respuesta not in ["y","n"]:
            print("Por favor ingresar un comando valido (y:Si, n:No)")
            respuesta=input("> ")
            if respuesta=="y":
                sys.exit()  
            elif respuesta=="n":
                pass
            
    while comando not in ["i","r","s","q"]:
        print("Por favor ingresar un comando válido (i:inventario, r:reanudar juego, s:salvar partida, q, salir del juego")
        comando=input("> ")
        if comando=="i":
            print("inventario")
              #Llamar funcion que muestre y controle el inventario
        elif comando=="r":
            break
        elif comando=="s":
            #LLamar funcion para guardara partida
            print("Partida guardada")
        elif comando=="q":
            print("#############################################################################")
            print("Si no ha salvado su partida, se le recomienda salvar antes de salir del juego")
            print("#############################################################################")
            print("                    ¿Desea abandonar el juego?")
            print("                    -[y] Si")
            print("                    -[n] No")
            respuesta=input("> ")
            if respuesta=="y":
                sys.exit()  
            elif respuesta=="n":
                    break
            while respuesta not in ["y","n"]:
                print("Por favor ingresar un comando valido (y:Si, n:No)")
                respuesta=input("> ")
                if respuesta=="y":
                    sys.exit()  
                elif respuesta=="n":
                    pass
            if(respuesta=="n"):
                break
                      


# In[33]:


def zona_alrededor_mapa(mapa_caracteres,iup):
    lista_mapa=[]
    for caracter in mapa_caracteres:
        lista_mapa.append(caracter)
    
    
    limit_inf=iup-6
    limit_sup=iup+6
    for l in [-6,-5,-4,-3,-2,-1]:
        if(lista_mapa[iup+l]=='\n'):
            limit_inf=iup+l+1
    for l in [1,2,3,4,5,6]:
        if (lista_mapa[iup+l]=='\n'):
            limit_sup=iup+l-1
    
    lista_mapa_mostrar=[]
    for n in [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]:
        if (limit_sup+26*n<0):
            pass
        elif (limit_inf+26*n > len(lista_mapa)-1):
            pass
        else:
            lista_mapa_mostrar.append('   |')
            for indice in range(limit_inf+26*n,limit_sup+26*n+1):
                lista_mapa_mostrar.append(lista_mapa[indice])
            lista_mapa_mostrar.append('|')    
            lista_mapa_mostrar.append('\n')
            
    marco='   |'        
    for columna in range(limit_sup-limit_inf+1):
        add='-'
        marco=marco+add
    marco=marco+'|'+'\n'
    mapa_mostrar="".join(lista_mapa_mostrar)
    mapa_mostrar= marco+mapa_mostrar+marco
    return(mapa_mostrar)


# In[35]:


#PROBANDO MANIPULACIÓN
confirmacion_arranque=pantalla_titulo()
if(confirmacion_arranque==True):
    os.system("cls")
    print("                  -INSTRUCCIONES-                  ")
    print("\n")
    print("---------------------------------------------------")
    print("#################    MOVILIDAD     ################")
    print("---------------------------------------------------")
    print("   -Para moverser hacia delante presionar -w-")
    print("   -Para moverser hacia atrás presionar -s-")
    print("   -Para moverser hacia la derecha presionar -d-")
    print("   -Para moverser hacia la izquierda presionar -a-")
    print("\n")
    print("---------------------------------------------------")
    print("#################     Pausa       ################")
    print("---------------------------------------------------")
    print("   -Para pausar presione -p-")
    print("\n")
    print(" PRESIONE -r- si esta listo para empezar")
    listo=input("> ")
    while listo!="r":
        print("Por favor ingresar [r] para poder empezar la partida")
        listo=input("> ")
    
    os.system("cls")
    fig, axs = plt.subplots(1,figsize=(6,6))
    plt.ion()
    
    mapa(ubicacion_personaje_x,ubicacion_personaje_y,MUROX, MUROY)
    mapa_ch=actualizar_mapa(mapa_ch[0],0, 0)
    mapa_amostrar=zona_alrededor_mapa(mapa_ch[0],mapa_ch[1])
    print("   #-Muro del calabozo")
    print("   D-Cofre")
    print("   o-Tu")
    print(mapa_amostrar)
    
    cofres_no_abiertos=[1,2,3,4,5]
    eventos_faltantes=[1,2,3,4,5,6,7]
    print("Este es el inicio de tu aventura, ya puedes empezar a moverte")
    
    plt.pause(0.01)
    
    moverse=True
    while moverse:
        pas=caminar(ubicacion_personaje_x,ubicacion_personaje_y,eventos_faltantes)
        if pas!=None:
            pasox, pasoy=pas
            if(pasox==0 and pasoy==0):
                pausa()
            else:
                ubicacion_personaje_x=ubicacion_personaje_x+pasox
                ubicacion_personaje_y=ubicacion_personaje_y+pasoy
                plt.pause(0.01)
                plt.clf()
                os.system('cls')
                
                #####################Ejecición de posibilicad de encontrar cofre #########################
                cofres_no_abiertos=[]
                for i in range(len(objetos_cofres)):
                    if(cofres_abiertos[str(i+1)]):
                        pass
                    else:
                        cofres_no_abiertos.append(i+1)
                
                numero_cofre=cofre_encontrado(ubicacion_personaje_x,ubicacion_personaje_y,coordenadas_cofres,cofres_no_abiertos)
                
                if(numero_cofre==None):
                    pass
                else:
                    print("Ha encontrado un cofre, desea abrirlo")
                    print("[y]- Si")
                    print("[n]- No")
                    abrir=input("> ")
                    if(abrir=="y"):
                        if(cofres_trampa[str(numero_cofre)]):
                            print("trampa")
                            #Activar funcion trampa
                        
                        else:
                            print("Objeto conseguido")
                            #Añadir objeto del cofre al inventario
                        cofres_abiertos[str(numero_cofre)]=True
                    elif(abrir=="n"):
                        pass
                    else:
                        print("Ha ingresado un comando inválido")
                        
                num_cofre_econtrado=cofre_encontrado(ubicacion_personaje_x,ubicacion_personaje_y,coordenadas_cofres,[1,2,3,4,5])
                if(num_cofre_econtrado==None):
                    pass
                else:
                    ubicacion_personaje_x=ubicacion_personaje_x-pasox
                    ubicacion_personaje_y=ubicacion_personaje_y-pasoy
                    pasox=0
                    pasoy=0
                
                mapa(ubicacion_personaje_x,ubicacion_personaje_y,MUROX, MUROY)
                mapa_ch=actualizar_mapa(mapa_ch[0],pasox, pasoy)
                mapa_amostrar=zona_alrededor_mapa(mapa_ch[0],mapa_ch[1])
                print("   #-Muro del calabozo")
                print("   D-Cofre")
                print("   o-Tu")
                print(mapa_amostrar)
                
                ################# Ejecución de posibilidad de entrar en zona de evento ##############################
                eventos_faltantes=[]
                for i in range(len(eventos_nombres)):
                    if(eventos_completados[str(i+1)]):
                        pass
                    else:
                        eventos_faltantes.append(i+1)
                        
                numero_evento=posible_evento(ubicacion_personaje_x,ubicacion_personaje_y,eventos_coord,eventos_faltantes)
                funcion_evento={"1":funcion_ev1()}
                
                if(numero_evento==None):
                    pass
                else:
                    modificar=funcion_evento[str(numero_evento)]
                    if (modificar[0]):
                        evento_completado[str(numero_evento)]=True
                    elif(modificar[0]==None):
                        print(modificar[2])
                    else:
                        print("Has muerto")
                        print("Intentalo de nuevo desde el último punto de guardado")
                        #llamar funcion de guardado
                        
                ################ Ejecución de posibilidad de enemigo normal #################################        
                posibilidad_enemigo(ubicacion_personaje_x,ubicacion_personaje_y)
            
    


# In[34]:


mapa_ch


# mapa_ch[0]

# In[79]:


a='-------------------------'+'\n'
b=mapa_ch[0]
c=a+b
print(c)


# In[81]:


for i in range(2):
    print(i)


# In[65]:


+27


# In[72]:


701-25


# In[ ]:




