lista_producto= []
#producto={ "nombre":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
#codigo tiene que tener 2 validaciones
#el codigo debe tener un minimo de 5 caracteres
#el codigo debe tener al menos 2 mayusculas
#el codigo debe tener al menos 1 numero


opcion="0"
"""
Sacar las funciones del while
Cambiar la listas par crear el producto por dicconarios
Agregar un codigo al diccionario de precios Productos
Agregar una lista para almacenar los diccionario de productos 
Modificar las funciones para que utilicen la nueva estructura de diccionario
Agregar las funciones faltantes
    Actualizar cantidad/precio
    Mostrar inventario completo
    Eliminar producto
"""
def validarCodigo(codigo):
    codigo="diego"
    contador_mayuscula = 0
    contador_numeros = 0
    for l in codigo:
        if l.isupper():
            contador_mayuscula +=1
        if l.isnumeric():
            contador_numeros +=1
        
    if contador_mayuscula <2:
        print("el codigo debe tener al menos 2 Mayusculas")
        return False
    elif contador_numeros == 0:
        print("El codigo debe tener al menos 1 numero")
        return False
    elif len(codigo) <5:
        print("El codigo debe tener al menos 5 caracteres")
        return False
    else:
        return True
    






def solicitarProducto():
    nombre=input("Ingrese el nombre del producto: ")
    while True:
        codigo=input('Ingrese el codigo para el producto:')
        if validarCodigo(codigo)==True:
            print("Codigo Correcto")
            break
        else:
            print("El Codigo es incorrecto. Debe volver a ingresarlo")    
    try:
        stock=int(input("Ingrese el stock del producto: "))
        precio=int(input("Ingrese el precio del producto: "))
        
        if stock<0 or precio <0:
            raise ValueError
            
        else:
            producto=[nombre,precio,stock,codigo]
            return producto

    except ValueError:
        print("Debe ingresar valores enteros positivos")

def guardarProducto(nombre,precio,stock,codigo):
    #producto={ "nombre":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
    productoBuscado=buscarProducto(codigo)
    if productoBuscado!=None:
            print("Ese producto ya fue registrado")
            return False
    
    producto={ "nombre":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
    lista_producto.append(producto)
    return True
        
   

def buscarProducto(codigo):
    for dicProducto in lista_producto:
        if codigo == dicProducto["codigo"]:
           return dicProducto
        


    return None



def mostra_producto (codigo):
    productoBuscado  = buscarProducto(codigo)
    if productoBuscado!= None:
        print("-"*60)
        print(f"Cod:{productoBuscado["codigo"]} Nombre: {productoBuscado["nombre"]} \t Precio: ${productoBuscado["precio"]} \t Stock: {productoBuscado["stock"]} unidades")
        print("-"*60)
        #return [nombre,precio,stock]
    #print("No existe un producto con ese nombre")

while opcion!="6":
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea(1-6): ")

    

    
    match opcion:

        case "1":
            nuevoProducto=solicitarProducto()
            if nuevoProducto!= None:
                guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])
        case "2":
            nombreProducto=input("Ingrese el nombre del producto a buscar: ")
            buscarProducto(nombreProducto)

