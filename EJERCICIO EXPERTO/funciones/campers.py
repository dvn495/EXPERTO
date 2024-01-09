import funciones.corefile as cf
import os
campus = {
    "campus":{
        "campers":{},
        "rutas":{},
        "pruebas":{},
        "salones":{},
        "camper":{}
    }
    
}
cf.MY_DATABASE='data/campers.json'
def NewCamper(data : dict):
    campus["campus"]["campers"].update(data)
    cf.AddData(campus)

def validarArchivoCampers():
    if(cf.checkFile()):
        print('ok')
        os.system("pause")
    else:
        cf.NewFile(campus)

def searchCamper()->dict:
    idbusqueda=input('Ingrese el numero id a editar')
    return campus.get(idbusqueda,{})

def deleteCamper():
    idbusqueda = int(input("Ingrese el id a buscar: "))
    cf.Eliminarcamper(idbusqueda,campus)
    




    