import sqlite3

def conectar():
    conexion  = sqlite3.connect('articulos.db')
    cursor= conexion.cursor()
    return conexion,cursor

def cerrar_conexion(conexion):
    conexion.close()
    
def crearTabla():
    conexion,cursor =conectar()
    cursor.execute('CREATE TABLE IF NOT EXISTS articulos (identificador INT PRIMARY KEY ,nombre VARCHAR(20),cantidad INT, importe FLOAT TEXT)')
    #print('Tabla creada')

def insertarDatos(conexion, cursor):
    articulos= [(12345,'Cuaderno',25,2.36),
                (1254,'boligrafo',100,0.90),
                (1345,'goma',75,0.75)]
    cursor.executemany('INSERT INTO articulos VALUES(?,?,?,?)',articulos)
    conexion.commit()
    

def insertarDatosArticulos(conexion, cursor,dato):    
    cursor.execute('INSERT INTO articulos VALUES(?,?,?,?)',dato)
    conexion.commit()    
    print('Datos insertados')  
     
def consultarDatos(conexion, cursor):
    cursor.execute('SELECT * FROM articulos')
    articulos=cursor.fetchall()    
    return articulos  

def actulizarDatos(conexion,cursor,id,nombre,cantidad,importe):
    cursor.execute(f"UPDATE articulos SET nombre='{nombre}',cantidad='{cantidad}',importe={importe} WHERE identificador={id}")
    conexion.commit()    
    print('Datos actulizados')
    
def borrarDatos(conexion,cursor,id):
    cursor.execute(f"DELETE FROM articulos WHERE identificador={id}")
    conexion.commit()    
    print('Dato borrado con exito')
    
if __name__ == '__main__':
    con, cursor = conectar()
    crearTabla()
    insertarDatos(con, cursor)
    dato= (234,'lapiz',150,0.60)
    insertarDatosArticulos(con, cursor,dato)
    articulos = consultarDatos(con, cursor)
    for articulos in articulos:
        print('\n')
        print(articulos[0])
        print("*"*30)
            
    actulizarDatos(con,cursor,234,"Lapiz",159,0.69)
    borrarDatos(con,cursor,12345)
    
    cerrar_conexion(con)
    