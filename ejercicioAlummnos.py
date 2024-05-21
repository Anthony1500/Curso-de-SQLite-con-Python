import sqlite3


def conectar():
    con = sqlite3.connect('alumnos.db')
    cursor = con.cursor()
    return con, cursor


def crearTabla(conexion, cursor):
    sentencia = """
          CREATE TABLE IF NOT EXISTS alumnos
          (ID INTEGER PRIMARY KEY NOT NULL,
          NOMBRE TEXT NOT NULL,
          EMAIL TEXT NOT NULL,
          NOTA INTEGER NOT NULL)
          """
    cursor.execute(sentencia)
    conexion.close()
    return True


def insertarDatos(conexion, cursor):
    nombre = input("Dime el nombre del alumno : ")
    email = input("Dime el email del alumno : ")
    nota = int(input("Que nota tiene : "))
    sentencia = f"""
    INSERT INTO alumnos VALUES(null,?,?,?);
    """
    datos = (nombre, email, nota)
    cursor.execute(sentencia, datos)
    conexion.commit()
    conexion.close()
    print('Registro creado correctamente')


def consultaAlumnos(conexion, cursor):
    sentencia = f"""
    SELECT * FROM alumnos
    """
    resultado = cursor.execute(sentencia)
    for fila in resultado:
        print(fila)
    conexion.close()


def consultarDatoswhere(conexion, cursor, id):
    sentencia = f"""
    SELECT * FROM alumnos WHERE id={id}
     """
    cursor.execute(sentencia)
    resultado = cursor.fetchone()
    if resultado:
        return True
    else:
        return False


def consultarDatos(conexion, cursor, id):
    sentencia = f"""
    SELECT * FROM alumnos WHERE id={id}
    """
    resultado = cursor.execute(sentencia)
    for fila in resultado:
        print(fila)
   


def modificarNota(conexion, cursor):
    id = input('Dime el idetificador del alumno : ')
    nota = 0
    if consultarDatoswhere(conexion, cursor, id):
        nota = int(input('Dame la nota : '))
    else:
        print('Dame un identificador valido')
        modificarNota(conexion, cursor)

    sentencia = f"""
    UPDATE alumnos set nota={nota} WHERE id={id}
    """
    cursor.execute(sentencia)
    conexion.commit()
    conexion.close()
    return True


def BorrarAlumno(conexion, cursor):
    id = input('Dime el idetificador del alumno : ')
    if consultarDatoswhere(conexion, cursor, id):
        print('Alumno econtrado')
        consultarDatos(conexion, cursor, id)
    else:
        print('Dame un identificador valido')
        BorrarAlumno(conexion, cursor)

    mensaje = input(
        'Estas seguro?, que deseas borrar al alumno encontrado s/n: ')
    while True:
        if mensaje == 's':
            sentencia = f"""
              DELETE from alumnos WHERE id=?
              """
            cursor.execute(sentencia, (id,))
            conexion.commit()
            
            print("Registro borrado correctamente")
            break
        else:
            print("Operación cancelada.")
            break
        conexion.close()
    return True


def menu():
    menu = """
          1. Insertar Dato alumno
          2. Consultar Alumnos
          3. Modificar Nota.
          4. Borrar alumno.
          0. Salir
          """
    print(menu)
    opcion = int(input())
    con, cursor = conectar()
    crearTabla(con, cursor)
    while True:

        if opcion == 1:
            con, cursor = conectar()
            insertarDatos(con, cursor)
        elif opcion == 2:
            con, cursor = conectar()
            consultaAlumnos(con, cursor)
        elif opcion == 3:
            con, cursor = conectar()
            modificarNota(con, cursor)
        elif opcion == 4:
            con, cursor = conectar()
            BorrarAlumno(con, cursor)
        elif opcion == 0:
            con.close()
            print("Adios, hasta pronto")
            break
        else:
            print("Indica una opcion valida")
        print(menu)
        opcion = int(input())


def principal():
    menu()


if __name__ == '__main__':
    con, cursor = conectar()
    principal()
