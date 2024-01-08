campers={   

}
isActive = True
while isActive:
    id= int(input("ID: "))
    nombre= (input("Nombre: "))
    apellidos =(input("Apellidos: "))
    camper={
        
        id :{
            "id" : id,
            "nombre" : nombre ,
            "apellidos" : apellidos
        }
        
    }
    print(camper)
    apellidos = input("Apellidos: ")
    camper[id].update(apellidos)
    campers.update(camper)
    print(campers)
    
