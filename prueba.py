usuarios = {}

def contraseña_valida(codigo):
    tiene_letras=False
    tiene_numero=False
    for c in codigo:
        if c.isalpha():
            tiene_letras = True
        elif c.isdigit():
            tiene_numero = True
    if len(codigo) <= 8 and tiene_letras and tiene_numero:
        return True
    return False

def ingresar_usuario():
    nombre=input("Ingrese un nombre:")
    if nombre in usuarios:
        print("Ya existe este usuario.") 
        return
    sexo=input("Ingrese su sexo  M o F (Masculino,Femenino):").strip()
    if sexo not in ['M','F']:
        print("Sexo no valido. Debe ser M o F.")
        
    while True:
        codigo=input("Ingrese una contraseña de 8 caracteres(debe tener 1 letra y un digito numerico):").strip()
        if contraseña_valida(codigo):
           print("Codigo registrado exitosamente.")
           usuarios[nombre]=[sexo,codigo]
           break
        else:
              print("Codigo no valido. Debe tener 8 caracteres, al menos una letra y un digito numerico.")

def buscar_usuario():
    nombre = input('Ingrese el nombre del usuario: ')
    if nombre in usuarios:
        datos = usuarios[nombre]
        print(datos)
        print(f" El sexo del Usuario es : {datos[0]}, Contraseña: {datos[1]}")
    else:
        print("Usuario no encontrado.")  
def eliminar_usuario():
    nombre = input("Ingrese el nombre:").strip()
    if nombre in usuarios:
        del usuarios[nombre]
        print(f"Usuario eliminado {nombre}.")
    else:
        print("usuario no encontrado.")

def main():
    while True:
       
        print('1. Ingresar Usuario')
        print('2. Buscar Usuario')
        print('3. Eliminar usuario')
        print('4. Salir')
       
        opcion = input('Seleccione una opción: ')

        match opcion:
            case '1':
                ingresar_usuario()
            case '2':
                buscar_usuario()
            case '3':
                eliminar_usuario()
            case'4':
                print("Saliendo del programa.")
                break
            case default:
                print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    main()