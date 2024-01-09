import json
import os
import ui.estudiantes as c
import funciones.campers as camp
import ui.menu as menu
import ui.rutas as rutas
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
    isActive = True
    while isActive:

        os.system("cls")
        menu.MenuPrincipal()
        try:
            mainmenu = int(input(":)_"))
        except ValueError:
            print("ERROR EN EL DATO INGRESADO")
        else:
            if(mainmenu == 1):
                c.Newstudent(campus)
                data = campus.get('campus').get("campers")
                camp.NewCamper(data)
                os.system("pause")
            elif(mainmenu == 2):
                pass
            elif(mainmenu ==3):
                rutas.creacionrutas(campus)
                data = campus.get('campus').get("rutas")
                camp.Newruta(data)
            elif(mainmenu ==2):
                pass
            elif(mainmenu ==2):
                pass
            elif(mainmenu ==2):
                pass
    
    