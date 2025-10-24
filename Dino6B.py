#🦖Biblioteca de dinosaurios N

#Lista prellenada de dinosaurios con su informacion
dinosaurios=[
    ("Tiranosaurio Rex","Carnivoro","12 metros","Cretácito","Tenia brazos muy cortos pero mandibulas poderosas")
    ("Triceratops","9 metros","Cretácico","Tenia 3 cuernos y una gran volante ósea")
    ("Velociraptor","Carnívoro","2 metros","Cretácico","Tenia una garra en forma de hoz en cada pata")  
    ("Brachiosaurus","Herbívoros","25 metros","Jurásico","Tenía un cuello laguísimo para alcanzar hojas altas")
    ("Stegosaurio","Herbíboro","9 metros","Jurásico","Tenía placas en la espalda y púas en la cola")
    ("Spinosaurus","Carnívoro","15 metros","Cretácico","Tenía una vela en la espada y era semiacuático")
    ("Ankylosaurus","Herbívoro","o metros","Cretácico","Estaba acorazado y tenía una maza en la cola")
    ("Pteranodon","Carnívoro","7 metros de ala a ala","Cretácico","Era un reptil volador, pero no era un dinosaurio")
    ("Diplodocus","Herbívoros","10 metros","Uno de los dinosaurios mas largo que existieron")
    ("Parasaurolophus","Herbívoros","10 metros","Cretácico","Tenía una cresta hueca para hacer sonidos")
]  

print("="*60)
print("🦖 Bienvenido a la biblioteca de dinosaurios🦕")
print("="*60)
print("Pregunta por cualquier dinosaurio y te daré su información")
print("Escribe 'lista'para ver todos los dinosaurio disponible.")
print("Escribe 'salir' para terminar. \n")

while True:
     consulta=input("¿Qué dinosaurio quieres consultar? ").strip().lower()

     if consulta=="salir":
        print("👋¡Hasta luego,  explorador de dinosaurios")
        break
        
     if consulta=="lista":
         print("\n📝 Dinosaurios disponibles")
         for i,(nombre,_,_,_,_)
             print(f"{i}. {nombre}")
         print()

         continue
         
    encontrado=False
    for nombre,dieta,tamaño,periodo,dato_curioso in dinosaurios:
        if consulta in nombre.lower(:)
            print("\n" + "="*60)
            print(f"🦕 {nombre}")
            print("=*60")
            print(f"🍖dieta: {dieta}")
            print(f"Tamaño:  {tamaño}")
            print(f"Perido:  Dato curioso: {dato_curioso}")
            print("="*60 + "\n")
            encontrado=True

    if not encontrado:
        print(f"❌No encontré informacion sobre '{consulta}'.")
        print("💡 Intenta escribir 'lista'para ver los dinosaurios disponibles. \n")