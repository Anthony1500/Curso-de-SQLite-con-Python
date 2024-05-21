import sqlite3


def conectar():
    # se crea en memoria  con = sqlite3.connect(':memory') y cuando se cierra se elimina
    con = sqlite3.connect('pruebas.db')
    cursor = con.cursor()
    return con, cursor


def creartabla(conexion, cursor):
    sentencia = """
    CREATE TABLE IF NOT EXISTS usuarios
    (ID INTEGER PRIMARY KEY NOT NULL,
    USUARIO TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    CLAVE TEXT NOT NULL);
    """
    cursor.execute(sentencia)
    conexion.close()
    print('Tabla creada correctamente')


def insertarDatos(conexion, cursor, datos):
    sentencia = """
    INSERT INTO usuarios VALUES(null,?,?,?);
    """
    # cursor.execute(sentencia,datos) # un dato
    cursor.executemany(sentencia, datos)  # muchos datos
    conexion.commit()
    conexion.close()
    print('Registro creado correctamente')


def consultarDatos(conexion, cursor):
    sentencia = """
    SELECT * FROM usuarios
    """
    resultado = cursor.execute(sentencia)
    for fila in resultado:
        print(fila)
    conexion.close()
    # print(cursor.fetchall())


def consultarDatosunoauno(conexion, cursor):
    sentencia = """
     Select id,usuario,email FROM usuarios
     """
    resultado = cursor.execute(sentencia)

    # for fila in resultado:
    #    print("*"*30)
    #    #print("\n")
    #    print("Id: ", fila[0])
    #    print("Nombre: ", fila[1])
    #    print("Email: ", fila[2])
    # print("\n")
   

    return resultado

def consultarDatoslimit(conexion, cursor):
    sentencia = """
     Select id,usuario,email FROM usuarios LIMIT 2
     """
    resultado = cursor.execute(sentencia)
    return resultado

def consultarDatoswhere(conexion, cursor,id):
    sentencia = f"""
     Select usuario,email FROM usuarios WHERE id={id}
     """
    resultado = cursor.execute(sentencia)
    return resultado

def actulizarDatos(conexion,cursor,id,nombre):
    
    sentencia=  f"""
     UPDATE usuarios set usuario='{nombre}' WHERE id={id}
     """
    cursor.execute(sentencia)
    conexion.commit()   
    print("Datos actulizados correctamente")    
    
    resultado = consultarDatoswhere(conexion,cursor,id)
    for fila in resultado:
        print("\n")
        print("*"*30)
        print("\n")
        #print("Id: ", fila[0])
        print("Nombre: ", fila[0])
        print("Email: ", fila[1])
        print("\n")
    conexion.close()
    
    
    return True
     
def borrarDatos(conexion,cursor,id):
    sentencia=  f"""
     DELETE from usuarios WHERE id={id}
     """
    cursor.execute(sentencia)
    conexion.commit()  
    print("Registro borrado correctamente") 
    
    resultado = consultarDatosunoauno(conexion, cursor)
    for fila in resultado:
        print("\n")
        print("*"*30)
        print("\n")
        print("Id: ", fila[0])
        print("Nombre: ", fila[1])
        print("Email: ", fila[2])
        print("\n")       
    conexion.close()
    
    return True


if __name__ == '__main__':
    con, cursor = conectar()
    # creartabla(con, cursor)
    datos = [('AnthonyA', 'anta@yahoo.com', '12345'),
             ('jun', 'juan@yahoo.com', '12345@'),
             ('Perez', 'pCevalos@yahoo.com', '145@')]
    #insertarDatos(con, cursor,datos)
    # consultarDatos(con, cursor)

    #resultado = consultarDatoswhere(con, cursor,2)
    #for fila in resultado:
    #    print("*"*30)
    #    print("\n")
    #    #print("Id: ", fila[0])
    #    print("Nombre: ", fila[0])
    #    print("Email: ", fila[1])
    #    print("\n")
    #con.close()
    
    # print(con)
    # print(cursor)
    #actulizarDatos(con,cursor,2,"JUAN JJ")
    borrarDatos(con,cursor,3)