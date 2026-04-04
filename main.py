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
from encargadoCatalogo import EncargadoCatalogo

# Crear los datos iniciales del sistema
def crear_datos_iniciales():
    catalogo = Catalogo(1, "Catalogo de museo")

    # Crear salas —------------
    sala1 = Sala("Sala de Pinturas", "Primer piso")
    sala2 = Sala("Sala de Esculturas", "Segundo piso")
    sala3 = Sala("Sala de Objetos", "Tercer piso")

# crear Obras -------------
    cuadro1 = Cuadro(
        id_obra=1,
        titulo="La Mona Lisa",
        autor="Leonardo da Vinci",
        periodo="Renacimiento",
        valor_economico=850000000,
        fecha_creacion=date(1503, 10, 1),
        fecha_entrada=date(2020, 1, 1),
        descripcion="Retrato de Lisa Gherardini, esposa de un comerciante florentino.",
        estado="disponible",
        tecnica="Óleo sobre tabla",
        estilo="Renacentista",
    )

# crear Esculturas -------------
    escultura1 = Escultura(
        id_obra=2,
        titulo="El Pensador",
        autor="Auguste Rodin",
        periodo="Modernismo",
        valor_economico=12000000,
        fecha_creacion=date(1902, 1, 1),
        fecha_entrada=date(2021, 6, 15),
        descripcion="Escultura de un hombre sentado en profunda reflexion.",
        estado="disponible",
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
        fecha_creacion=date(1503, 10, 1),
        fecha_entrada=date(2020, 1, 1),
        descripcion="Reloj de sol antiguo utilizado para medir el tiempo mediante la posición del sol.",
        estado="deteriorada",
    )

# Registrar obras en el catálogo
    catalogo.registrar_obra(cuadro1)
    catalogo.registrar_obra(escultura1)
    catalogo.registrar_obra(objeto1)

# Asignar obras a las salas
    sala1.asignar_obra(cuadro1)
    sala2.asignar_obra(escultura1)
    sala3.asignar_obra(objeto1)

# Crear museo
    museo = Museo("Museo de Arte e Historia", "Calle Principal 123, Ciudad")
    museo.recibir_obra(cuadro1)
    museo.recibir_obra(escultura1)
    museo.recibir_obra(objeto1)
    return museo, catalogo, sala1, sala2, sala3

# Mostrar detalle de una obra

def mostrar_detalle_obra(obra):
    print(f"  ID: {obra.id_obra}")
    print(f"  Titulo: {obra.titulo}")
    print(f"  Autor: {obra.autor}")
    print(f"  Periodo: {obra.periodo}")
    print(f"  Valor economico: COP {obra.valor_economico:,}")
    print(f"  Fecha de creacion: {obra.fecha_creacion}")
    print(f"  Fecha de entrada: {obra.fecha_entrada}")
    print(f"  Descripcion: {obra.descripcion}")
    

# Pausar y esperar que el usuario presione Enter
def pausar():
    input("Presione Enter para continuar...")

# Crear usuario según el rol elegido
def crear_usuario():
    print("\n=== REGISTRO DEL USUARIO ===")
    nombre = input("Ingrese su nombre: ").strip()
    apellido = input("Ingrese su apellido: ").strip()
    email = input("Ingrese su correo electronico: ").strip()
    contrasena = input("Ingrese su contrasena: ").strip()

    print("\nSeleccione su rol:")
    print("1. Director")
    print("2. Restaurador Jefe")
    print("3. Visitante")
    print("4. Encargado de Catalogo")
    rol = input("Ingrese el numero de su rol: ").strip()

    if rol == "1":
        return Director(1, nombre, apellido, email, contrasena)
    elif rol == "2":
        return RestauradorJefe(2, nombre, apellido, email, contrasena)
    elif rol == "3":
        return Visitante(3, nombre, apellido, email, contrasena)
    elif rol == "4":
        return EncargadoCatalogo(4, nombre, apellido, email, contrasena,)
    else:
        return Visitante(3, nombre, apellido, email, contrasena)
    

# Autenticar usuario
def autenticar_usuario(email, contrasena, usuarios):
    for usuario in usuarios:
        if usuario.email == email and usuario._contrasena == contrasena:
            print(f"Autenticación exitosa. Bienvenido, {usuario.nombre} {usuario.apellido}.")
            return usuario
    print("Autenticación fallida. Email o contrasena incorrectos.")
    return None

# Menú del Director
def menu_director(usuario, museo, catalogo):
    while True:
        print("=== MENU DEL DIRECTOR ===")
        print("1. Ver catalogo de obras")
        print("2. Ver valor total en cesion")
        print("3. Gestionar cesion de una obra")
        print("4. Ver cesiones activas")
        print("0. Salir")  
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n=== CATÁLOGO DE OBRAS ===")
            for obra in catalogo.obras:
                print(f"ID: {obra.id_obra} - Título: {obra.titulo} - Autor: {obra.autor}")
            pausar()
        
        elif opcion == "2":
            total = usuario.calcular_valor_total()
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
                        usuario.gestionar_cesion(cesion)
                        cesion.iniciar_cesion()

        elif opcion == "4":
            usuario.ver_cesiones_activas()
            pausar()
        
        elif opcion == "0":
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
            opcion_obra = input("Seleccione el número de la obra que desea restaurar: ").strip()    
            if not opcion_obra.isdigit() or int(opcion_obra) < 1 or int(opcion_obra) > len(deterioradas):
                print("Opción inválida. Por favor, seleccione un número válido.")
                pausar()
                continue
            
            posicion = int(opcion_obra) - 1
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
            for r in usuario.restauraciones:
                if r.obra == obra and r.estado == "en proceso":
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
            

# Menú del Encargado de Catálogo
def menu_encargado(usuario, catalogo, sala1, sala2, sala3):
    while True:
        print(f"\n=== MENU DEL ENCARGADO DE CATALOGO: {usuario.nombre} {usuario.apellido} ===")
        print("1. Ver catalogo")
        print("2. Registrar obra")
        print("3. Eliminar obra")
        print("4. Clasificar obra")
        print("5. Asignar obra a sala")
        print("0. Salir")
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            catalogo.listar_obras()
            pausar()

        elif opcion == "2":
            print("Funcion de registrar obra proximamente.")
            pausar()

        elif opcion == "3":
            if not catalogo.obras:
                print("No hay obras en el catalogo.")
                pausar()
                continue
            for i, obra in enumerate(catalogo.obras, start=1):
                print(f"{i}. {obra.titulo}")
            opcion_obra = input("Seleccione el numero de la obra a eliminar: ").strip()
            if not opcion_obra.isdigit() or int(opcion_obra) < 1 or int(opcion_obra) > len(catalogo.obras):
                print("Opcion invalida.")
                pausar()
                continue
            obra = catalogo.obras[int(opcion_obra) - 1]
            usuario.eliminar_obra(obra.id_obra)
            pausar()

        elif opcion == "4":
            if not catalogo.obras:
                print("No hay obras en el catalogo.")
                pausar()
                continue
            for i, obra in enumerate(catalogo.obras, start=1):
                print(f"{i}. {obra.titulo} | Periodo actual: {obra.periodo}")
            opcion_obra = input("Seleccione el numero de la obra: ").strip()
            if not opcion_obra.isdigit() or int(opcion_obra) < 1 or int(opcion_obra) > len(catalogo.obras):
                print("Opcion invalida.")
                pausar()
                continue
            obra = catalogo.obras[int(opcion_obra) - 1]
            nuevo_periodo = input("Ingrese el nuevo periodo: ").strip()
            usuario.clasificar_obra(obra.id_obra, nuevo_periodo)
            pausar()

        elif opcion == "5":
            if not catalogo.obras:
                print("No hay obras en el catalogo.")
                pausar()
                continue
            for i, obra in enumerate(catalogo.obras, start=1):
                print(f"{i}. {obra.titulo}")
            opcion_obra = input("Seleccione el numero de la obra: ").strip()
            if not opcion_obra.isdigit() or int(opcion_obra) < 1 or int(opcion_obra) > len(catalogo.obras):
                print("Opcion invalida.")
                pausar()
                continue
            obra = catalogo.obras[int(opcion_obra) - 1]
            print(f"1. {sala1.nombre}")
            print(f"2. {sala2.nombre}")
            print(f"3. {sala3.nombre}")
            opcion_sala = input("Seleccione la sala: ").strip()
            if opcion_sala == "1":
                usuario.asignar_sala(obra.id_obra, sala1)
            elif opcion_sala == "2":
                usuario.asignar_sala(obra.id_obra, sala2)
            elif opcion_sala == "3":
                usuario.asignar_sala(obra.id_obra, sala3)
            else:
                print("Opcion invalida.")
            pausar()

        elif opcion == "0":
            print("Saliendo del menu del Encargado.")
            break

        else:
            print("Opcion no valida.")
            pausar()

# Menú del Visitante
def menu_visitante(usuario, museo, catalogo, sala1, sala2, sala3):
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
                    print(f"  - {obra.titulo}")
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
            print(f"  Autor: {obra.autor}")
            print(f"  Periodo: {obra.periodo}")
            print(f"  Año de creacion: {obra.fecha_creacion}")
            
            # Buscamos en qué sala está
            for sala in [sala1, sala2, sala3]:
                if obra in sala.obras:
                    print(f"  Sala: {sala.nombre}")
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
            contrasena = input("Ingrese su contrasena: ")
            usuario = autenticar_usuario(email, contrasena, usuarios)
            if usuario:
                if isinstance(usuario, Director):
                    menu_director(usuario, museo, catalogo)
                elif isinstance(usuario, RestauradorJefe):
                    menu_restaurador(usuario, museo, catalogo)
                elif isinstance(usuario, Visitante):
                    menu_visitante(usuario, museo, catalogo, sala1, sala2, sala3)
                elif isinstance(usuario, EncargadoCatalogo):
                    menu_encargado(usuario, catalogo, sala1, sala2, sala3)
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