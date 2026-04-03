from datetime import date
from catalogo import Catalogo
from cesion import Cesion
from museo import Museo
from cuadro import Cuadro
from escultura import Escultura
from objeto import Objeto
from restauracion import Restauracion
from sala import Sala
from usuario import Usuario
from director import Director
from restauradorJefe import RestauradorJefe
from visitante import Visitante

# Crear los datos iniciales del sistema
def crear_datos_iniciales():
    Catalogo = Catalogo(1, "Catalogo de museo")

# crear Salas ------------
    sala1 = Sala(1, "Sala de Pinturas")
    sala2 = Sala(2, "Sala de Esculturas")
    sala3 = Sala(3, "Sala de Objetos")

# crear Obras -------------
    cuadro1 = Cuadro(
        id_obra=1,
        titulo="La Mona Lisa",
        autor="Leonardo da Vinci",
        periodo="Renacimiento",
        valor_economico=850000000,
        fecha_creacion="1503-10-01",
        fecha_entrada="2020-01-01",
        descripcion="Retrato de Lisa Gherardini, esposa de un comerciante florentino.",
        estado="en exhibición",
        tecnica="Óleo sobre tabla",
        estilo="Renacentista",
    )

# crear Esculturas -------------
    Escultura1 = Escultura(
        id_obra=2,
        titulo="El Pensador",
        autor="Auguste Rodin",
        periodo="Modernismo",
        valor_economico=12000000,
        fecha_creacion="1503-10-01",
        fecha_entrada="2020-01-01",
        descripcion="Escultura de un hombre sentado en profunda reflexión.",
        estado="en exhibición",
        material="Bronce",
        estilo="Modernista",
    )

# crear Objetos -------------
    objeto1 = Objeto(
        id_obra=3,
        titulo="Reloj de Sol",
        autor="Desconocido",
        periodo="Antiguo",
        valor_economico=5000,
        fecha_creacion="1503-10-01",
        fecha_entrada="2020-01-01",
        descripcion="Reloj de sol antiguo utilizado para medir el tiempo mediante la posición del sol.",
        estado="deteriorada",
    )

# Registrar obras en el catálogo
    Catalogo.registrar_obra(cuadro1)
    Catalogo.registrar_obra(Escultura1)
    Catalogo.registrar_obra(objeto1)

# Asignar obras a las salas
    sala1.agregar_obra(cuadro1)
    sala2.agregar_obra(Escultura1)
    sala3.agregar_obra(objeto1)

# Crear museo
    museo = Museo(
        id_museo=1,
        nombre="Museo de Arte e Historia",
        direccion="Calle Principal 123, Ciudad",
        catalogo=Catalogo,
        salas=[sala1, sala2, sala3]
    )
    return museo, Catalogo, sala1, sala2, sala3

# Mostrar detalle de una obra

def mostrar_detalle_obra(obra):
    print(f"ID de la obra: {obra.id_obra}")
    print(f"Título: {obra.titulo}")
    print(f"Autor: {obra.autor}")
    print(f"Periodo: {obra.periodo}")
    print(f"Valor económico: {obra.valor_economico}")
    print(f"Fecha de creación: {obra.fecha_creacion}")
    print(f"Fecha de entrada al museo: {obra.fecha_entrada}")
    print(f"Descripción: {obra.descripcion}")
    print(f"Estado: {obra.estado}")
    if isinstance(obra, Cuadro):
        print(f"Técnica: {obra.tecnica}")
        print(f"Estilo: {obra.estilo}")
        elif isinstance(obra, Escultura):
    print(f"Material: {obra.material}")
    print(f"Estilo: {obra.estilo}")

# Pausar y esperar que el usuario presione Enter
def pausar():
    input("Presione Enter para continuar...")

# Crear usuario según el rol elegido
def crear_usuario():
    print("\n=== REGISTRO DEL USUARIO ===")
    nombre = input("Ingrese su nombre: ")   
    apellido = input("Ingrese su apellido: ")
    email = input("Ingrese su correo electrónico: ")
    contraseña = input("Ingrese su contraseña: ")

    print("\nSeleccione su rol:")
    print("1. Director")
    print("2. Restaurador Jefe")
    print("3. Visitante")
    rol = input("Ingrese el número correspondiente a su rol: ")

    if rol == "1":
        return Director(1, nombre, apellido, email, contraseña, "director")
    elif rol == "2":
        return RestauradorJefe(2, nombre, apellido, email, contraseña, "restaurador_jefe")
    elif rol == "3":
        return Visitante(3, nombre, apellido, email, contraseña, "visitante")
    else:
        print("Rol no reconocido. Creando un usuario genérico.")
        return Usuario(4, nombre, apellido, email, contraseña, "visitante")

# Autenticar usuario
def autenticar_usuario(email, contraseña, usuarios):
    for usuario in usuarios:
        if usuario.email == email and usuario.contraseña == contraseña:
            print(f"Autenticación exitosa. Bienvenido, {usuario.nombre} {usuario.apellido}.")
            return usuario
    print("Autenticación fallida. Email o contraseña incorrectos.")
    return None

# Menú del Director
def menu_director(usuario, museo, catalogo):
    while True:
        print("\n=== MENÚ DEL DIRECTOR ===")
        print("1. Ver catálogo de obras")
        print("2. Agregar nueva obra")
        print("3. Modificar obra existente")
        print("4. Eliminar obra")
        print("5. Ver salas del museo")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n=== CATÁLOGO DE OBRAS ===")
            for obra in catalogo.obras:
                print(f"ID: {obra.id_obra} - Título: {obra.titulo} - Autor: {obra.autor}")
            pausar()
        
        elif opcion == "2":
            total = usuario.calcular_valor()
            print(f"Valor total de obras en cesion: COP {total:,}")
            pausar()
        
        elif opcion == "3":
            if not catalogo.obras:
                print("No hay obras disponibles para ceder en el catálogo.")
            else:
                print("\n=== obra disponibles ===")
                for i, obra in enumerate(catalogo.obras, start=1):
                    print(f"{i}. {obra.titulo} | Estado: {obra.estado}")

                opcion_obra = input("Seleccione el número de la obra que desea ceder: ").strip()
                if not opcion_obra.isdigit() or int(opcion_obra) < 1 or int(opcion_obra) > len(catalogo.obras):
                    print("Opción inválida. Por favor, seleccione un número válido.")
                else:
                    posicion = int(opcion_obra) - 1
                    if posicion < 0 or posicion >= len(catalogo.obras):
                        print("Posición inválida. Por favor, seleccione un número válido.")
                    else:
                        obras = catalogo.obras[posicion]
                        cesion = Cesion(
                            obra=obras,
                            museo=museo,
                            fecha_inicio=date.today(),
                            fecha_fin=date(2026, 12, 31),
                            importe=5000000
                        )
                        usuario.gestionar_cesiones(cesion)
                        cesion.iniciar_cesion()

        elif opcion == "4":
            usuario.ver_cesiones_activas()
            pausar()
        
        elif opcion == "6":
            print("Saliendo del menú del Director.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
            pausar()


# Menú del Restaurador Jefe
def menu_restaurador(usuario, museo, catalogo):
    while True:
        print(f"\nBienvenido Restaurador: {usuario.nombre} {usuario.apellido}")
        print("1. Ver obras que necesitan restauracion")
        print("2. Iniciar restauracion")
        print("3. Finalizar restauracion")
        print("4. Consultar historial")
        print("0. Salir")
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            # Buscamos obras deterioradas
            deterioradas = [o for o in catalogo.obras if o.estado == "deteriorada"]
            if deterioradas:
                print("Obras que necesitan restauracion:")
                for obra in deterioradas:
                    print(f"  - {obra.titulo}")
            else:
                print("No hay obras que necesiten restauracion.")
            pausar()


        elif opcion == "2":
            deterioradas = [o for o in catalogo.obras if o.estado == "deteriorada"]
            if not deterioradas:
                print("No hay obras que necesiten restauracion.")
                pausar()
                continue
            print("Obras disponibles para restauracion:")
            for i, obra in enumerate(deterioradas, start=1):
                print(f"{i}. {obra.titulo} | Estado: {obra.estado}")
            pausar()
            opcion_obra = input("Seleccione el número de la obra que desea restaurar: ").strip()    
            if not opcion_obra.isdigit() or int(opcion_obra) < 1 or int(opcion_obra) > len(deterioradas):
                print("Opción inválida. Por favor, seleccione un número válido.")
            
            obra = deterioradas[posicion]
            restauracion = Restauracion(obra=obra, tipo="limpieza", motivo="Restauracion preventiva")
            usuario.iniciar_restauracion(restauracion)
            pausar()

        elif opcion == "3":
            # Buscamos obras en restauracion
            en_restauracion = [o for o in catalogo.obras if o.estado == "en restauracion"]
            if not en_restauracion:
                print("No hay obras en restauracion.")
                pausar()
                continue
            print("Obras en restauracion:")
            for i, obra in enumerate(en_restauracion, start=1):
                print(f"{i}. {obra.titulo} | Estado: {obra.estado}")
            
            opcion_obra = input("Seleccione el número de la obra que desea finalizar restauracion: ").strip()
            if not opcion_obra.isdigit():
                print("Opción inválida. Por favor, seleccione un número válido.")
                pausar()
                continue

            posicion = int(opcion_obra) - 1
            if posicion < 0 or posicion >= len(en_restauracion):
                print("Opción inválida. Por favor, seleccione un número válido.")
                pausar()
                continue

            # Buscamos la restauracion en el historial del restaurador
            obra = en_restauracion[posicion]
            restauracion = None
            for r in usuario.historial_restauraciones:
                if r.obra == obra and r.estado == "en curso":
                    restauracion = r
                    break
            
            if restauracion: 
                usuario.finalizar_restauracion(restauracion)
            else:
                print("No se encontró una restauración en curso para la obra seleccionada.")
                pausar()

        elif opcion == "4":
            usuario.consultar_historial()
            pausar()
        elif opcion == "0":
            print("Saliendo del menú del Restaurador Jefe.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
            pausar()
            

# Menú del Visitante
def menu_visitante(usuario, museo, catalogo):
    while True:
        print(f"\nBienvenido Visitante: {usuario.nombre} {usuario.apellido}")
        print("1. Ver obras disponibles")
        print("2. Consultar información de una obra")
        print("0. Salir")
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            if catalogo.obras:
                print("Obras disponibles en el museo:")
                for obra in catalogo.obras:
                    print(f"  - {obra.titulo} | Estado: {obra.estado}")
            else:
                print("No hay obras disponibles en el museo.")
            pausar()

        elif opcion == "2":
            if not catalogo.obras:
                print("No hay obras disponibles para consultar.")
                pausar()
                continue
            print("Obras disponibles:")
            for i, obra in enumerate(catalogo.obras, start=1):
                print(f"{i}. {obra.titulo}")
            opcion_obra = input("Seleccione el número de la obra que desea consultar: ").strip()
            if not opcion_obra.isdigit():
                print("Opción inválida. Por favor, seleccione un número válido.")
                pausar()
                continue
            posicion = int(opcion_obra) - 1
            if posicion < 0 or posicion >= len(catalogo.obras):
                print("Opción inválida. Por favor, seleccione un número válido.")
                pausar()
                continue
            obra = catalogo.obras[posicion]
            print(f"Información de la obra '{obra.titulo}':")
            print(f"  Artista: {obra.artista}")
            print(f"  Año: {obra.anio}")
            print(f"  Estado: {obra.estado}")
            pausar()

        elif opcion == "0":
            print("Saliendo del menú del Visitante.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
            pausar()

# Función principal
def main():
    museo, catalogo, sala1, sala2, sala3 = crear_datos_iniciales()
    usuarios = []
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE MUSEO ===")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("0. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            usuario = crear_usuario()
            usuarios.append(usuario)
            print(f"Usuario '{usuario.nombre} {usuario.apellido}' registrado exitosamente.")
            pausar()

        elif opcion == "2":
            email = input("Ingrese su correo electrónico: ")
            contraseña = input("Ingrese su contraseña: ")
            usuario = autenticar_usuario(email, contraseña, usuarios)
            if usuario:
                if isinstance(usuario, Director):
                    menu_director(usuario, museo, catalogo)
                elif isinstance(usuario, RestauradorJefe):
                    menu_restaurador(usuario, museo, catalogo)
                elif isinstance(usuario, Visitante):
                    menu_visitante(usuario, museo, catalogo)
                else:
                    print("Rol de usuario no reconocido. No se puede acceder al menú.")
                    pausar()

            elif opcion == "0":
                print("Saliendo del sistema de gestión de museo. ¡Hasta luego!")
                break
    
            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")
                pausar()
    
    if __name__ == "__main__":
        main()