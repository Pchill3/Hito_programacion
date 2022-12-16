#para productos necesitamos los datos de cada producto (id,nombre,unidades,precio,fechafabricacion)

#creamos la clase producto
class producto:
#definimos la funcion
    def __init__(self,id,nombre,unidades,precio,fechafabricacion):
        self.id=id
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio
        self.fechafabricacion=fechafabricacion
#introducimos los datos de cada producto
producto1=producto(1,'cordero',15,50.75,'24/09/2022')
producto2=producto(2,'gambas',200,21.35,'20/01/2022')
producto3=producto(3,'cochinillo',20,60.50,'16/04/2022')
producto4=producto(4,'pulpo',50,35.25,'12/11/2021')





