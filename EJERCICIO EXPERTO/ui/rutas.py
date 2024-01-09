import os
import funciones.campers as camp

rutas = ["Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)", "Programación Web (HTML, CSS y Bootstrap)", "Programación formal (Java, JavaScript, C#)", "Bases de datos (Mysql, MongoDb y Postgresql). Cada ruta tiene un SGDB principal y un alternativo", "Backend (NetCore, Spring Boot, NodeJS y Express)"]

def creacionrutas(campus:dict):
    camp.cf.checkFile(camp.campus)
    isActive = True
    
    while isActive:
        data = campus.get('campus').get("rutas")
        os.system("cls")
        header="""
        ╔═════════════════════════════╗
        ║    CREACION   DE   RUTAS    ║
        ╚═════════════════════════════╝
        """
        print (header)
        ruta = input("INGRESE LA NUEVA RUTA: ")
        ruta ={
            
            'fundamentos':[],
            "programacion.web":[],
            "programacion.formal":[],
            "bases.datos":[],
            "backend":[]
                
            
            }
                    
        print ("\nSeleccione las materias a ingresar por cada modulo en su ruta")
        for i, item in enumerate(rutas):
            ismaterias = True
            print(f"{(i+1)}-{item}")
            if (i+1)==1:
                while ismaterias:
                    materias = input("Registre las materias: ") 
                    ruta["fundamentos"].append(materias)
                    rta = input("Desea registrar otra materia(S/N): ").upper() 
                    if rta != "S":
                        ismaterias = False

            elif (i+1)==2:
                while ismaterias:
                    materias = input("Registre las materias: ") 
                    ruta["programacion.web"].append(materias)
                    rta = input("Desea registrar otra materia(S/N): ").upper() 
                    if rta != "S":
                        ismaterias = False
            elif (i+1)==3:
                while ismaterias:
                    materias = input("Registre las materias: ") 
                    ruta["programacion.formal"].append(materias)
                    rta = input("Desea registrar otra materia(S/N): ").upper() 
                    if rta != "S":
                        ismaterias = False
            elif (i+1)==4:
                while ismaterias:
                    materias = input("Registre las materias: ") 
                    ruta["bases.datos"].append(materias)
                    rta = input("Desea registrar otra materia(S/N): ").upper() 
                    if rta != "S":
                        ismaterias = False
            elif (i+1)==5:
                while ismaterias:
                    materias = input("Registre las materias: ") 
                    ruta["backend"].append(materias)
                    rta = input("Desea registrar otra materia(S/N): ").upper() 
                    if rta != "S":
                        ismaterias = False
        
        data.update(ruta)
        rta2 = input(f"► ¿desea registrar otra ruta?(S/N): ").upper()
        if rta2 != "S":
            isActive= False
        print(ruta)
        os.system("pause")
            
                        
                        
                        
                
       
        
        
        
        
        
        
        