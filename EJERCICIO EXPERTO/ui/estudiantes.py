import funciones.corefile as cf
import funciones.campers as camp
import json
import os
import ui.menu as menu


rojo = '\033[91m'
amarillo = '\033[33m'
azul = '\033[34m'
reset = '\033[0m'
def Newstudent(campus : dict):
        camp.cf.checkFile(camp.campus)
        isactive = True
        camp.cf.ReadFile()
        while isactive:
                os.system("cls")
                menu.MenuCampers()
                eleccion = int(input(":)_"))
                data = campus.get('campus').get("campers")
                if eleccion == 1:
                        os.system("cls")
                        telefono = {    
                        }
                        istelefonoactive = True
                        title= """
                        ╔═══════════════════════╗
                        ║     NUEVO CAMPER      ║
                        ╚═══════════════════════╝
                        """
                        print(title)
                        try:
                                id = int(input("\n► Reigistre el id del estudiante: "))
                        except ValueError:
                                print("ERROR AL REGISTRAR EL ID")
                        
                        idregistro = id

                        nombre = input("► nombre: ")
                        apellidos = input("► apellidos: ")
                        direccion = input("► direccion: ")
                        os.system("cls")
                        title=f"""{rojo}
                        ╔═══════════════════════╗
                        ║   REGISTRO ACUDIENTE  ║
                        ╚═══════════════════════╝
                        {reset}
                        """
                        print(title)
                        try:
                                idacu = int(input("  ► Reigistre el id del acudiente: "))
                        except ValueError:
                                print("ERROR AL REGISTRAR EL ID")
                        nombreacudiente = input("  ► nombre del acudiente: ")
                        try: 
                                telefonoacudiente = int(input("  ► telefono del acudiente: "))
                        except ValueError:
                                print("ERROR AL INGRESAR EL TELEFONO")
                        emailacudiente = input("  ► email del acudiente: ")
                        os.system("cls")
                        title=f"""{rojo}
                        ╔═══════════════════════╗
                        ║   REGISTRO ACUDIENTE  ║
                        ╚═══════════════════════╝
                        {reset}
                        """
                        print(title)
                        while istelefonoactive:
                                telefonokey = input("\n► que numero desea registrar(personal, empresarial, etc.): ")
                                telefonovalue = int(input("►  nuemero de telefono: "))
                                telefono.update({telefonokey:telefonovalue})

                                rta = input(f"{azul}► ¿desea registrar otro telefono?(S/N): {reset}").upper()
                                if rta != "S":
                                        istelefonoactive = False

                        acudiente = {
                                "id": idacu,
                                "Nombre": nombreacudiente,
                                "Telefono": telefonoacudiente,
                                "email":emailacudiente,
                        }

                        idregistro ={
                                "id":id,
                                "Nombre": nombre,
                                "Apellidos":apellidos,
                                "Direccion":direccion,
                                "Acudiente":acudiente,
                                "Telefono" : telefono,
                                "estado":' ',
                        }
                        
                        data.update({idregistro["id"]:idregistro})
                        rta2 = input(f"►{azul} ¿desea registrar otro estudiante?(S/N): {reset}").upper()
                        if rta2 != "S":
                                isactive= False
                elif eleccion == 2:
                        title= """
                        ╔═══════════════════════╗
                        ║     BORRAR CAMPER     ║
                        ╚═══════════════════════╝
                        """
                        print(title)
                        camp.deleteCamper()  
                elif eleccion == 3:
                        isactive = False   
        
