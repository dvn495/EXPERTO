import json
import os
import funciones.estudiantes as c

campus = {
    "campus":{
        "campers":{},
        "rutas":{},
        "pruebas":{},
        "salones":{},
        "camper":{}
    }
}
if __name__ == "__main__":
    c.NewCamper(campus)