def validarCodigo(codigo):
    codigo=input('Ingrese un nombre y apellido:')
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
    