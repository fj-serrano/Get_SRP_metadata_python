# -*- coding: utf-8 -*-


import pandas as pd #Pandas se usara para leer el excel
import tkinter #Tkinter nos permite abrir el buscador de archivos para elegir el excel y obtener la ruta
from tkinter import filedialog
tk = tkinter.Tk()
tk.withdraw()  #Esta parte forma parte del import de tkinter 

def selec_archive_to_df(): #FUNCIÓN PARA SELECCIONAR EL ARCHIVO CON LOS METADATOS
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
    data_frame["file"] = fagz

    data_frame.rename(columns={"Experiment":"name"}, inplace=True) #Renombramos en el dataframe la columna Experiments para que sea la de name

    #Luego vamos a modificar el data frame para que se elimine la información de las columnas que esté entre paréntesis y se modifiquen los espacios por _
    data_frame = data_frame.replace(r" \(.*\)", "", regex=True) #Mediante regex, que se usa para buscar en el texto patrones, borramos todo lo que se encuentre en texto cruto (r) entre paréntesis
    data_frame = data_frame.replace(r" ", "_", regex=True) #Mediante este comando se reemplazan los " " por _

    return(data_frame)


    
def ask_user_cabe(df): #FUNCIÓN PARA PREGUNTARLE AL USUARIO SI HAY ALGUNA VARIABLE QUE QUIERE Y QUE ESA SE AÑADA A LA BUSQUEDA
    Flag = True
    nuevas_cabeceras = ["file","name"] #AQUÍ PUEDES AÑADIR CABECERAS QUE TE INTERESA QUE BUSQUE SIEMPRE
    posibles_columnas = "" #Vamos a hacer una varaible de texto que tenga el nombre de todas las columnas para que el usuario las vea.
    for p in df.columns:
        posibles_columnas = posibles_columnas + str(p) + ", "
    print("Introduzca el nombre exacto de la columna que quiere:\n\n{0}\n\nUna vez termine pulse Intro.".format(posibles_columnas))
    while Flag == True:
        colum = input()
        if colum in df.columns: #Solo se añadirán las columnas que indique el usuario y que existan en el data frame
            nuevas_cabeceras.append(colum)
        if colum == "":
            Flag = False
    for n in range(len(nuevas_cabeceras)-1, -1, -1): #Revisamos si hay alguna cabecera repetida y en ese caso se elimina una copia, para ello se recorrerá la lista al revés
        cabeza = nuevas_cabeceras[n]
        if nuevas_cabeceras.count(cabeza) != 1:
            del nuevas_cabeceras[n]
            
    return(nuevas_cabeceras) #Devuelve una lista con las cabeceras nuevas que quiere probar el usuario

try:
    df = selec_archive_to_df() #Nos da el data frame con toda la información del excel seleccionado
    
    SRA_Study = df["SRA Study"][0]+".tsv" #Guardamos el nombre del estudio para crear el txt con ese nombre

    cabecera = ask_user_cabe(df) #Términos nuevos de la cabecera que quiera añadir el usuario

    df.to_csv(SRA_Study,sep="\t", columns=cabecera, float_format=str, mode="w", index=False)  #Con esto guardamos el archivo en el formato que queremos directamente desde el data frame

except:
    print("\nHa ocurrido un error, por favor inténtelo de nuevo.")
