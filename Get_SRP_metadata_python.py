# -*- coding: utf-8 -*-


import pandas as pd #Pandas se usara para leer el excel
import tkinter #Tkinter nos permite abrir el buscador de archivos para elegir el excel y obtener la ruta
from tkinter import filedialog
tk = tkinter.Tk()
tk.withdraw()  #Esta parte forma parte del import de tkinter 

def selec_archive_to_df(): #FUNCIÓN PARA SELECCIONAR EL ARCHIVO CON LOS METADATOS
    try:
        file_path = filedialog.askopenfilename() #Guardamos en esta variable la ruta del excel seleccionado por el usuario
        file_path_clean = "" #Creamos una variable vacía que contendrá la ruta sin / y con \

        for a in range(len(file_path)):
            if file_path[a] != "/":
                file_path_clean = file_path_clean + file_path[a]
            elif file_path[a] == "/":
                file_path_clean = file_path_clean + "\\" #Hace falta poner \\ porque sino lo interpreta como un carácter de escape
            
        data_frame = pd.read_csv(file_path_clean) #Guardamos usando pandas la infomación del archivo .csv en un data frame
        
        #Ahora vamos a añadirle al data frame una columna con lo que contiene Experiment + fa.gz
        fagz = []
        for fil in range(len(data_frame)):
            fagz.append((str(data_frame.iloc[fil]["Experiment"]))+".fa.gz")
        data_frame["Experiment.fa.gz"] =  fagz

        #Luego vamos a modificar el data frame para que se elimine la información de las columnas que esté entre paréntesis y se modifiquen los espacios por _
        data_frame = data_frame.replace(r" \(.*\)", "", regex=True) #Mediante regex, que se usa para buscar en el texto patrones, borramos todo lo que se encuentre en texto cruto (r) entre paréntesis
        data_frame = data_frame.replace(r" ", "_", regex=True) #Mediante este comando se reemplazan los " " por _

        return(data_frame)
    except:
        print("\nHa ocurrido un error, por favor inténtelo de nuevo.")

    
def ask_user_cabe(): #FUNCIÓN PARA PREGUNTARLE AL USUARIO SI HAY ALGUNA VARIABLE QUE QUIERE Y QUE ESA SE AÑADA A LA BUSQUEDA
    Flag = True
    nuevas_cabeceras = [] #AQUÍ PUEDES AÑADIR CABECERAS QUE TE INTERESA QUE BUSQUE SIEMPRE
    posibles_columnas = "" #Vamos a hacer una varaible de texto que tenga el nombre de todas las columnas para que el usuario las vea.
    for p in df.columns:
        posibles_columnas = posibles_columnas + str(p) + ", "
    print("Introduzca el nombre exacto de la columna que quiere:\n\n{0}\n\nUna vez termine pulse Intro.".format(posibles_columnas))
    while Flag == True:
        colum = input()
        nuevas_cabeceras.append(colum)
        if colum == "":
            Flag = False
            nuevas_cabeceras.pop()
    for n in range(len(nuevas_cabeceras)-1): #Revisamos si hay alguna cabecera repetida y en ese caso se elimina una copia
        cabeza = nuevas_cabeceras[n]
        if nuevas_cabeceras.count(cabeza) != 1:
            del nuevas_cabeceras[n]
            
    return(nuevas_cabeceras) #Devuelve una lista con las cabeceras nuevas que quiere probar el usuario


def table(df,cabecera):
    String_Cabecera = "" #El string para la cabecera de la tabla que se va a guardar en el .txt
    String_Table = "" #El string que contiene los contenidos del data frame
    cabecera_nueva = ["Experiment.fa.gz","Experiment","Run"] #Pongo de base las 3 primeras columnas que siempre serán las mismas
    ajuste = 5 #Se puede modificar para cambiar la distancia entre columnas al tabular
    justificacion = {} #Un diccionario que guardará la justificación del texto para la tabla dependiendo de la longitud
    
    for cabeza in cabecera: #Primero comprobamos que las columnas que quiere el usuario existan en el archivo y en caso de que estén guardamos el nombre en la lista cabezera_nueva
        if cabeza in df.columns:
            if cabeza not in cabecera_nueva:
                cabecera_nueva.append(cabeza)
    
    for cabeza in cabecera_nueva: #Ajustamos el diccionario para que contenga todas las columnas que usaremos
        justificacion[cabeza] = len(cabeza)
    
    for cabeza in cabecera_nueva: #Recorremos todos los datos buscando lo larga que es cada frase para ajustar la justificacion acorde
        for fil in range(len(df)):
            if len(str(df.iloc[fil][cabeza])) > int(justificacion[cabeza]):
                justificacion[cabeza] = len(str(df.iloc[fil][cabeza]))
        justificacion[cabeza] = int(justificacion[cabeza]) + ajuste
       
    
    for fil in range(len(df)): #Luego, hacemos la tabla de la info, .iloc nos permite acceder por posición numerica
 
        for cabeza in cabecera_nueva:
            String_Table = String_Table + str(df.iloc[fil][cabeza]).ljust(int(justificacion[cabeza]))
                             
        String_Table = String_Table + "\n" #Pongo el espacio separado para que los condicionales puedan comprobarse antes de pasar de linea
  
    
    String_Cabecera = String_Cabecera + "File".ljust(int(justificacion["Experiment.fa.gz"])) + "Name".ljust(int(justificacion["Experiment"])) + "Experiment".ljust(int(justificacion["Run"])) #Terminos de cabecera estandar que tendrán todos los archivos
    for col in range(len(cabecera_nueva)): #Por último hacemos la cabecera
        if col > 2:
            String_Cabecera= String_Cabecera + cabecera_nueva[col].ljust(int(justificacion[(cabecera_nueva[col])]))
    String_Cabecera = String_Cabecera + "\n" #Pasamos a la siguiente linea para separar la cabecera de la información de la tabla
    
    return(String_Cabecera, String_Table) #FUNCIÓN PARA CRER LA TABLA DE TEXTO QUE APARECERÁ EN EL ARCHIVO QUE CREARÁ EL PROGRAMA
    

df = selec_archive_to_df() #Nos da el data frame con toda la información del excel seleccionado
    
SRA_Study = df["SRA Study"][0]+".tsv" #Guardamos el nombre del estudio para crear el txt con ese nombre

cabecera = ask_user_cabe() #Términos nuevos de la cabecera que quiera añadir el usuario

String_Cabecera, String_Table = table(df,cabecera)

with open(SRA_Study, "w") as txt:
    txt.write(String_Cabecera)
    txt.write(String_Table)

