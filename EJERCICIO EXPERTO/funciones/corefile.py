import json
import os
MY_DATABASE = ''

def NewFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def AddData(*param):
    with open(MY_DATABASE,"r+") as rwf:
        data_file=json.load(rwf)
        if (len(param) > 1):
            data_file.update({param[0]:param[1]})
        else:
            data_file.update(param[0])
        # data_file[llavePrincipal].update({codigo:info})
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)
        rwf.close()

def ReadFile():
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)
    
def checkFile(*param):
    data = list(param)
    if(os.path.isfile(MY_DATABASE)):
        if(len(param)):
            data[0].update(ReadFile())
    else:
        if(len(param)):
            NewFile(data[0])
        
def EliminarCamper(clave : int, *param):
    campersdict = param[0]
    if str(clave) in campersdict['campus']['campers']:
        del campersdict['campus']['campers'][str(clave)]
        NewFile(campersdict)
        print(f"El camper con id {clave} fue eliminado satisfactoriamente")
    else:
        print(f"No se encontro un camper registrado con la id {clave}")
    os.system("pause")    





    
    