import os

menu = ["Registro de campers","Registro de prueba","Creacion de rutas de entranmiento","Gestor de matriculas", "Modulo de reportes"]
submenu= ["Nuevo camper","Borrar camper", "Editar camper","Buscar","Regesar al menu"]


def MenuPrincipal():
    header= """
        ╔═════════════════════════════╗
        ║      MENU   PRINCIPAL       ║
        ╚═════════════════════════════╝

    """
    print(header)
    for i, item in enumerate(menu):
        print (f"{i+1} - {item}")
    
def MenuCampers():
    header="""
        ╔═════════════════════════════╗
        ║   ADMINISTRACION CAMPERS    ║
        ╚═════════════════════════════╝
        """
    
    print (header)
    for i, item in enumerate(submenu):
        print(f"{(i+1)}-{item}")
        

    
    
    
        
        
    
    
       
    
