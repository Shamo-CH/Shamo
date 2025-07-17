productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    'GF75HD': [749990, 2],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'UWU131HD': [349990, 1]
}


def stock_marca():
    marca = input("Ingrese marca a consultar: ")
    total = 0
    for modelo in productos:
        if productos[modelo][0].lower() == marca.lower():
            total += stock[modelo][1]
    print(f"El stock es: {total}")


def busqueda_precio():
    while True:
        try:
            p_min = int(input("Ingrese precio mínimo: "))
            p_max = int(input("Ingrese precio máximo: "))
            break
        except:
            print("Debe ingresar valores enteros!!")

    resultados = []
    for modelo in stock:
        precio, cantidad = stock[modelo]
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            resultados.append(f"{marca}--{modelo}")

    
    for i in range(len(resultados)):
        for j in range(i + 1, len(resultados)):
            if resultados[i] > resultados[j]:
                resultados[i], resultados[j] = resultados[j], resultados[i]

    if len(resultados) > 0:
        print("Los notebooks entre los precios consultados son:", resultados)
    else:
        print("No hay notebooks en ese rango de precios.")


def actualizar_precio():
    def actualizar():
        modelo = input("Ingrese modelo a actualizar: ")
        try:
            nuevo_precio = int(input("Ingrese precio nuevo: "))
            if modelo in stock:
                stock[modelo][0] = nuevo_precio 
                print("Precio actualizado!!")
            else:
                print("El modelo no existe!!")
        except:
            print("Debe ingresar un precio válido.")

    while True:
        actualizar()
        repetir = input("Desea actualizar otro precio (s/n)?: ").lower()
        if repetir != 's':
            return


def salir():
    print("Programa finalizado.")
    exit()


def opcion_invalida():
    print("Debe seleccionar una opción válida!!")


def menu():
    opciones = {
        '1': stock_marca,
        '2': busqueda_precio,
        '3': actualizar_precio,
        '4': salir
    }

    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        opcion = input("Ingrese opción: ")

        accion = opciones.get(opcion, opcion_invalida)
        accion()


menu()