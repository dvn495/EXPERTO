import funciones.corefile as cf
import json
cf.MY_DATABASE='data/campers.json'
def NewCamper(campus : dict):
        data = campus.get('campus').get("campers")
                   
        camper ={
                "id":' ',
                "Nombre": ' ',
                "Apellidos":' ',
                "Direccion":' ',
                "Acudiente":{},
                "Telefono":{},
                "estado":' ',
        }
        acudiente = {
                "id":'1 ',
                "Nombre":'acudiente1',
                "Telefono":'6666 ',
                "email":' acudiente@gmail.com',
        }
        telefono = {
                "id":' 1',
                "Numero":'444 ',
                "ubicacion":'casa ',
        }
        camper1 = {
                "id":'123 ',
                "Nombre":' AAAA',
                "Apellidos":'BBBB ',
                "Direccion":'cra ',
                "Acudiente":{}, 
                "Telefono":{},
                "estado":' I',
        }
        camper1["Acudiente"].update({str((len(camper1["Acudiente"])+1)).zfill(3):acudiente})
        data.update({camper1["id"]:camper1})
        print(json.dumps(data, indent=4))
