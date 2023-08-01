import os #libreria de python
CARPETA = 'contactos/'  #cra una variable que en mayusculas significa que no se debe modificar su valor
EXTENSION = '.txt' #variable para  la extension de archivos

class Contacto : 
    def __init__(self, nombre, telefono,categoria): 
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():

    crear_directorio()

    mostrar_menu()

    preguntar = True
    while preguntar : 
        opcion = input('Seleccione una opción \r\n')
        opcion = int (opcion)
        
        if opcion == 1 :
            agregar_contacto()
            preguntar == False
        elif opcion == 2 :
            editar_contacto()
            preguntar == False
        elif opcion == 3 :
            mostrar_contactos()
            preguntar == False
        elif opcion == 4 :
            buscar_contacto()
            preguntar == False
        elif opcion == 5 :
            eliminar_contacto()
            preguntar == False
        else : 
            print('Opción no válida')
        mostrar_menu()


def eliminar_contacto():

    nombre = input('Escriba el nombre del contacto a eliminar: \r\n')

    try: 
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n')
        print ('El contacto fue eliminado correctamente')
        print('\r\n')
    except :
        print('Error! No se pudo eliminar el contacto! \r\n')
        print('\r\n')

    app()



def buscar_contacto():

    nombre = input('Escriba el contacto que desea buscar: \r\n')

    try: 
        with open (CARPETA + nombre + EXTENSION) as contacto: 
            print('\r\n Información del contacto: \r\n' )
            for linea in contacto: 
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe!')

    app()
def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open (CARPETA + archivo) as contacto: 
            for linea in contacto: 
                print (linea.rstrip())

            print('|-|-|-|-|-|-|-|-|-|-|-|-|')

def editar_contacto():
    print('Escribe el nombre del contacto que desea editar \r\n')
    nombre_anterior = input ('Nombre del contacto que desea editar : \r\n')

    existe = existe_contacto(nombre_anterior)

    if existe:
        with open (CARPETA + nombre_anterior + EXTENSION, 'w') as archivo :  

            nombre_contacto = input('Nuevo Nombre del contacto : \r\n')
            telefono_contacto = input('Nuevo Teléfono del contacto : \r\n')
            categoria_contacto = input('Nuevo Categoría del contacto: \r\n')

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre : '+ contacto.nombre + '\r\n')
            archivo.write('Teléfono : '+ contacto.telefono + '\r\n')
            archivo.write('Categoría : '+ contacto.categoria + '\r\n')

        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
        print('¡¡¡Contacto editado correctamente!!!')

    else: 
        print('No puedes editar el contacto!')

def agregar_contacto(): 
    print ('Escribe los datos para agregar nuevo contacto \r\n')
    nombre_contacto = input('Nombre del contacto \r\n')

    existe = existe_contacto(nombre_contacto)

    if not existe :
        with open (CARPETA + nombre_contacto + EXTENSION, 'w') as archivo : 
            
            telefono_contacto = input('Agrega el teléfono del contacto : \r\n')
            categoria_contacto = input('Agrega la categoría del contacto: \r\n')
        

                #instancia la clase

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: '+ contacto.nombre + '\r\n') 
            archivo.write('Teléfono: '+ contacto.telefono + '\r\n')   
            archivo.write('Categoria: '+ contacto.categoria + '\r\n')
            
        print('¡¡¡ Contacto creado correctamente !!!')
    else: 
        print ('El contacto ya existe')
    
def mostrar_menu():
    print ('Seleccione la opción deseada')
    print('1->  Agregar Nuevo Contacto')
    print('2->  Editar Contacto')
    print('3->  Ver Contacto')
    print('4->  Buscar Contacto')
    print('5->  Eliminar Contacto')
    
def crear_directorio():
    if not os.path.exists (CARPETA): #niega la busqueda de la carpeta

        os.makedirs(CARPETA) #la crea en caso de no existir

def existe_contacto (nombre): 
    return os.path.isfile(CARPETA + nombre + EXTENSION)    

app()