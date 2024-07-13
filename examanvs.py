from statistics import mean , geometric_mean
from random import randint
nombres=['Juan Pérez','María García','Carlos López','Ana Martínez',
                'Pedro Rodríguez','Laura Hernández','Miguel Sánchez',
                'Isabel Gómez','Francisco Díaz','Elena Fernández']
trabajadores=[]
sueldos=[]
reporte=[]
def asignar_sueldos():
    for trabajador in nombres:
        print(f"{trabajador.ljust(20)}{str(randint(300000,2500000)).ljust(10)}")
        trabajadores.append({"nombre":trabajador,"sueldo":(randint(300000,2500000))})
        #sueldos.append(f"{trabajador.ljust(20)}{str(randint(300000,2500000)).ljust(10)}")       
    pass
    
def clasificar_sueldos():
    for trabajador in trabajadores:
        if trabajador["sueldo"]<800000:
            print("Sueldos menores a 800.000")
            print(f"{trabajador["nombre"].ljust(20)}{trabajador["sueldo"]}")
    
    for trabajador in trabajadores:
        if trabajador["sueldo"]>800000 and trabajador["sueldo"]<2000000 :
            print("Sueldos entre 800.000 y 2.000.000")
            print(f"{trabajador["nombre"].ljust(20)} {trabajador["sueldo"]}")
            
    for trabajador in trabajadores:
        if trabajador["sueldo"]>2000000:
            print("Sueldos mayores a 2.000 000")
            print(f"{trabajador["nombre"].ljust(20)}{trabajador["sueldo"]}")
    pass

def estadisticas():
    for trabajador in trabajadores:
        sueldos.append(trabajador["sueldo"])
    print(min(sueldos))
    print(max(sueldos))
    print(mean(sueldos))
    print(geometric_mean(sueldos))
    pass
def reporte_sueldos():
    for trabajador in trabajadores:
        salud=trabajador["sueldo"]*0.7
        afp=trabajador["sueldo"]*0.12
        sueldo_liquido=trabajador["sueldo"]-salud-afp
        reporte.append({"nombre":trabajador,"salud":salud,"afp":afp,"sueldo_liquido":sueldo_liquido})
        print(f"{reporte}")
    
    pass
def menu():
    print("##############################")
    print("1) Asignar sueldos aleatorias")
    print("2) Clasificar sueldos ")
    print("3) Ver estadisticas ")
    print("4) Reporte de sueldos ")
    print("5) Salir del programa")
    print("################################")

opcion=0
while opcion!=5:
    menu()
    opcion=int(input("ingresa una de las opciones"))
    if opcion==1:
        asignar_sueldos()
        print ("##### SUELDO INGRESADO #####")
    elif opcion==2:
        clasificar_sueldos()
        
    elif opcion==3:
        estadisticas()
        
    elif opcion==4:
        reporte_sueldos()
    
    else:
        
        print ("finalizando programado \n Desarrollado por Victor Silva \n rut 17.081.687")
        exit()
        
    
    
    pass
