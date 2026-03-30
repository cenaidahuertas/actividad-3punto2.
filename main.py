from datetime import date

from catalogo import Catalogo
from cesion import Cesion
from museo import Museo
from obraArte import Cuadro, Escultura, OtroObjeto
from restauracion import Restauracion
from sala import Exposicion, Sala
from usuario import Director, RestauradorJefe, Visitante


def crear_datos():
    catalogo = Catalogo(1, "Catalogo del museo")
    museo = Museo(1, "Museo Central", "Bogota")

    sala_1 = Sala(1, "Sala Renacimiento", "Primer piso")
    sala_2 = Sala(2, "Sala Moderna", "Segundo piso")
    museo.agregar_sala(sala_1)
    museo.agregar_sala(sala_2)

    cuadro = Cuadro(
        1,
        "La Mona Lisa",
        "Leonardo da Vinci",
        "Renacimiento",
        1000000,
        date(1503, 1, 1),
        date(2020, 1, 1),
        "Cuadro famoso del museo",
        tecnica="Oleo",
        estilo="Renacentista",
    )

    escultura = Escultura(
        2,
        "El Pensador",
        "Auguste Rodin",
        "Moderno",
        700000,
        date(1904, 1, 1),
        date(2018, 5, 10),
        "Escultura representativa",
        material="Bronce",
        estilo="Realista",
    )

    objeto = OtroObjeto(
        3,
        "Vasija Antigua",
        "Autor desconocido",
        "Antiguo",
        250000,
        date(1700, 1, 1),
        date(2016, 6, 20),
        "Objeto historico",
        estado="danada",
        tipo_objeto="Ceramica",
    )

    sala_1.asignarObra(cuadro)
    sala_2.asignarObra(escultura)
    sala_2.asignarObra(objeto)

    catalogo.agregarObra(cuadro)
    catalogo.agregarObra(escultura)
    catalogo.agregarObra(objeto)

    museo.recibir_obra(cuadro)
    museo.recibir_obra(escultura)
    museo.recibir_obra(objeto)
    museo.agregar_museo_colaborador("Museo del Oro")
    museo.agregar_museo_colaborador("Museo de Arte Moderno")

    exposicion = Exposicion(date(2026, 3, 1), date(2026, 5, 30), sala_1)

    restauracion_inicial = Restauracion(1, "Limpieza", date(2026, 3, 10), "Dano por humedad")
    objeto.enviarARestauracion(restauracion_inicial)

    return museo, catalogo, exposicion


def formatear_cop(valor):
    return f"COP {valor:,.0f}"


def mostrar_detalle_obra(obra):
    print(f"Id: {obra.id}")
    print(f"Titulo: {obra.titulo}")
    print(f"Autor: {obra.autor}")
    print(f"Valor economico: {formatear_cop(obra.valor_economico)}")
    print(f"Fecha de creacion: {obra.fecha_creacion}")
    print(f"Fecha de entrada: {obra.fecha_entrada}")
    print(f"Estado: {obra.estado}")


def pausar():
    input("Presiona Enter para continuar...")


def escoger_obra(lista_obras):
    if not lista_obras:
        return None

    for indice, obra in enumerate(lista_obras, start=1):
        print(f"{indice}. {obra.titulo}")

    opcion = input("Escoge una obra: ").strip()
    if not opcion.isdigit():
        return None

    posicion = int(opcion) - 1
    if posicion < 0 or posicion >= len(lista_obras):
        return None

    return lista_obras[posicion]


def crear_usuario():
    print("=== REGISTRO DEL USUARIO ===")
    nombre = input("Escribe tu nombre: ").strip()
    print("Escoge tu rol:")
    print("1. Director")
    print("2. Restaurador")
    print("3. Visitante")
    opcion = input("Opcion: ").strip()
    clave = input("Crea tu clave: ").strip()

    if opcion == "1":
        return Director(1, nombre, clave)
    if opcion == "2":
        return RestauradorJefe(2, nombre, clave)
    return Visitante(3, nombre, clave)


def autenticar_usuario(usuario):
    print()
    print("=== INGRESO AL SISTEMA DEL MUSEO ===")
    clave = input("Escribe tu clave para ingresar: ").strip()
    return usuario.autenticar(clave)


def menu_director(usuario, museo, catalogo):
    while True:
        print()
        print(usuario.mostrar_datos())
        print("1. Ver catalogo")
        print("2. Ver valor total")
        print("3. Gestionar cesion")
        print("4. Ver obras en restauracion")
        print("5. Ver obras cedidas")
        print("6. Ver solicitudes de cesion")
        print("0. Salir")
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            for obra in museo.obras:
                mostrar_detalle_obra(obra)
                print("-" * 30)
            pausar()
        elif opcion == "2":
            total = usuario.calcularValorTotal(museo.obras)
            print(f"Valor total del museo: {formatear_cop(total)}")
            pausar()
        elif opcion == "3":
            cesion = Cesion(
                len(museo.cesiones) + 1,
                museo.obras[0],
                museo.museos_colaboradores[0],
                150000,
                date(2026, 4, 1),
                date(2026, 6, 1),
            )
            usuario.gestionarCesion(museo, cesion)
            print(f"Cesion creada para: {cesion.obra.titulo}")
            pausar()
        elif opcion == "4":
            obras = usuario.verObrasEnRestauracion(museo)
            if obras:
                for obra in obras:
                    print(obra.titulo)
            else:
                print("No hay obras en restauracion.")
            pausar()
        elif opcion == "5":
            obras = usuario.verObrasCedidas(museo)
            if obras:
                for obra in obras:
                    print(f"{obra.titulo} -> {obra.museo_cedido_actual}")
            else:
                print("No hay obras cedidas en este momento.")
            pausar()
        elif opcion == "6":
            if museo.solicitudes_cesion:
                for titulo, destino in museo.solicitudes_cesion:
                    print(f"{titulo} -> {destino}")
            else:
                print("No hay solicitudes de cesion pendientes.")
            pausar()
        elif opcion == "0":
            print("Saliendo del menu del director.")
            break
        else:
            print("Opcion no valida.")
            pausar()


def menu_restaurador(usuario, museo, catalogo):
    while True:
        print()
        print(usuario.mostrar_datos())
        print("1. Ver obras que necesitan restauracion")
        print("2. Iniciar restauracion")
        print("3. Finalizar restauracion")
        print("4. Consultar historial")
        print("0. Salir")
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            pendientes = usuario.revisarRestauraciones(museo.obras, date.today())
            if pendientes:
                for obra in pendientes:
                    print(obra.titulo)
            else:
                print("No hay obras para restaurar.")
            pausar()
        elif opcion == "2":
            pendientes = usuario.revisarRestauraciones(museo.obras, date.today())
            if pendientes:
                print("Obras disponibles para restauracion:")
                obra = escoger_obra(pendientes)
                if obra is None:
                    print("No escogiste una obra valida.")
                    pausar()
                    continue
                restauracion = Restauracion(
                    len(obra.restauraciones) + 1,
                    "Limpieza",
                    date.today(),
                    "Revision programada o dano",
                )
                print(usuario.decidir_envio_restauracion(obra, True, restauracion))
            else:
                print("No hay obras disponibles para iniciar restauracion.")
            pausar()
        elif opcion == "3":
            obras_en_restauracion = museo.listar_obras_en_restauracion()
            if obras_en_restauracion:
                print("Obras en restauracion:")
                obra = escoger_obra(obras_en_restauracion)
                if obra is None:
                    print("No escogiste una obra valida.")
                    pausar()
                    continue
                usuario.finalizarRestauracion(obra, date.today())
                print(f"Restauracion terminada de: {obra.titulo}")
            else:
                print("No hay obras en restauracion para finalizar.")
            pausar()
        elif opcion == "4":
            print("Escoge la obra para consultar historial:")
            obra = escoger_obra(museo.obras)
            if obra is None:
                print("No escogiste una obra valida.")
                pausar()
                continue
            historial = usuario.consultarHistorial(obra)
            if historial:
                for item in historial:
                    print(f"{item.tipo} | Inicio: {item.fecha_inicio} | Fin: {item.fecha_fin}")
            else:
                print("La obra no tiene historial de restauracion.")
            pausar()
        elif opcion == "0":
            print("Saliendo del menu del restaurador.")
            break
        else:
            print("Opcion no valida.")
            pausar()


def menu_visitante(usuario, catalogo, exposicion):
    while True:
        print()
        print(usuario.mostrar_datos())
        print("1. Buscar obra")
        print("2. Listar obras")
        print("3. Consultar obras por sala")
        print("4. Fecha de exposicion")
        print("5. Estado de la exposicion")
        print("0. Salir")
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            titulo = input("Titulo de la obra: ").strip()
            obra = catalogo.buscarObra(titulo)
            if obra:
                mostrar_detalle_obra(obra)
            else:
                print("Obra no encontrada.")
            pausar()
        elif opcion == "2":
            obras = catalogo.listarObras()
            if obras:
                for obra in obras:
                    print(obra)
            else:
                print("No hay obras registradas.")
            pausar()
        elif opcion == "3":
            sala = input("Nombre de la sala: ").strip()
            obras = usuario.consultarObrasPorSala(catalogo, sala)
            if obras:
                for obra in obras:
                    print(obra)
            else:
                print("No hay obras en esa sala.")
            pausar()
        elif opcion == "4":
            print(catalogo.FechaDeExposicion(exposicion))
            pausar()
        elif opcion == "5":
            if exposicion.estaActiva(date.today()):
                print(exposicion.iniciarExposicion())
            else:
                print(exposicion.finalizarExposicion())
            pausar()
        elif opcion == "0":
            print("Saliendo del menu del visitante.")
            break
        else:
            print("Opcion no valida.")
            pausar()


def main():
    museo, catalogo, exposicion = crear_datos()
    usuario = crear_usuario()

    if not autenticar_usuario(usuario):
        print("Acceso denegado.")
        return

    if usuario.rol == "director":
        menu_director(usuario, museo, catalogo)
    elif usuario.rol == "restaurador jefe":
        menu_restaurador(usuario, museo, catalogo)
    else:
        menu_visitante(usuario, catalogo, exposicion)


if __name__ == "__main__":
    main()
